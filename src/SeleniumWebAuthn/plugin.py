from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary import SeleniumLibrary

from selenium.webdriver.common.virtual_authenticator import Credential
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions as VAOpts

from pathlib import Path
from base64 import b64encode, b64decode
from base64 import urlsafe_b64decode, urlsafe_b64encode
from typing import Dict
import sys
import json

class SeleniumWebAuthn(LibraryComponent):

    def __init__(self: "SeleniumWebAuthn", ctx: SeleniumLibrary, config_file: str | None = None) -> None:
        LibraryComponent.__init__(self, ctx)
        self.config = None
        self.config_file = None
        self.virtual_authenticator_options = None
        self.passive_credentials = []

        if config_file:
            self.config_file = Path(config_file)
            self.load_webauthn_configs(self.config_file)

    @keyword
    def add_virtual_authenticator(self, protocol: str, transport: str, hasResidentKey: bool, hasUserVerification: bool, isUserConcenting: bool, isUserVerified: bool, config_file: str | None = None,
                                  auto_save: bool = True) -> None:

        if self.config_file and self.virtual_authenticator_options and auto_save:
            self.save_webauthn_configs(self.config_file)

        self.virtual_authenticator_options = VAOpts(
            getattr(VAOpts.Protocol, protocol.upper()),
            getattr(VAOpts.Transport, transport.upper()),
            hasResidentKey,
            hasUserVerification,
            isUserConcenting,
            isUserVerified
        )



    @keyword
    def activate_virtual_authenticator(self) -> None:
        if self.virtual_authenticator_options:
            self.ctx.driver.add_virtual_authenticator(self.virtual_authenticator_options)
            if self.passive_credentials:
                for c in self.passive_credentials:
                    credentialId = urlsafe_b64decode(c['credentialId'])
                    privateKey = urlsafe_b64decode(c['privateKey'])
                    userHandle = urlsafe_b64decode(c['userHandle'])
                    if c["isResidentCredential"]:
                        cred = Credential.create_resident_credential( credentialId, c['rpId'], userHandle, privateKey, c['signCount'])
                    else:
                        cred = Credential.create_non_resident_credential( credentialId, c['rpId'], privateKey, c['signCount'])

                    self.ctx.driver.add_credential(cred)
                self.passive_credentials = []
        else:
            raise RuntimeError("Virtual Authenticator has not been defined.\nEither: \n * Load one from config file \n * Create one with `Add Virtual Authenticator` keyword ")


    @property
    def active_virtual_authentication_configs(self) -> Dict:
        payload = {}
        if self.virtual_authenticator_options:
            payload['authenticator'] = self.virtual_authenticator_options.to_dict()

        if self.passive_credentials:
            payload['credentials'] = self.passive_credentials
        else:
            payload['credentials'] = list( map(lambda cred: cred.to_dict(), self.ctx.driver.get_credentials()))

        return payload

    @keyword
    def save_webauthn_configs(self, config_file: str | None = None) -> None:
        cfg = config_file or self.config_file
        if not cfg:
            raise RuntimeError("Neither argument to keyword or activate VirtualAuthenticator provided location to store configurations")


        payload = self.active_virtual_authentication_configs

        print(f"XXXX: {cfg}", file=sys.stderr)
        Path(cfg).write_text(json.dumps(payload, indent=2))


    @keyword
    def load_webauthn_configs(self, config_file: str | None = None) -> None:
        auto_save = False
        load_config_from = self.config_file

        if config_file:
            load_config_from = Path(config_file)
            if self.config_file != config_file:
                auto_save = True

        payload = json.loads(load_config_from.read_text(encoding="utf-8"))

        if "authenticator" in payload:
            opts = payload["authenticator"]
            self.add_virtual_authenticator(opts["protocol"], opts["transport"], opts["hasResidentKey"], opts["hasUserVerification"], opts["isUserConsenting"], opts["isUserVerified"], load_config_from, auto_save = auto_save)

        if "credentials" in payload:
            self.passive_credentials = payload["credentials"]
