from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary import SeleniumLibrary

from selenium.webdriver.common.virtual_authenticator import Credential
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions as VAOpts

from pathlib import Path
from base64 import b64encode, b64decode
import sys
import json


class SeleniumWebAuthn(LibraryComponent):
    def __init__(self: "SeleniumWebAuthn", ctx: SeleniumLibrary, config_file: str | None = None) -> None:
        LibraryComponent.__init__(self, ctx)
        self.config = None
        self.virtauthopts = None

        if config_file:
            self.config_file = Path(config_file)
        else:
            self.config_file = Path(".").resolve() / Path("webauthnconfig.json")

        self.load_webauthn_configs(self.config_file)

        if self.config and "authenticators" in self.config:
            for authenticator in self.config["authenticators"]:
                if "autoAdd" in authenticator and authenticator["autoAdd"]:
                    if not self.virtauthopts:
                        self.virtauthopts = VAOpts(
                            getattr(VAOpts.Protocol, authenticator["protocol"]),
                            getattr(VAOpts.Transport, authenticator["transport"]),
                            authenticator["has_resident_key"],
                            authenticator["has_user_verification"],
                            authenticator["is_user_consenting"],
                            authenticator["is_user_verified"],
                        )


        if self.config and "credentials" in self.config:
            for cred_id in self.config["credentials"]:
                cred_data = self.config["credentials"][cred_id]
                new_cred = None
                if not cred_data["autoAdd"]:
                    continue

                cred_id = bytearray.fromhex(cred_data["id"])
                rp_id = cred_data["rp_id"]
                private_key = b64decode(cred_data["private_key"])
                sign_count = cred_data["sign_count"]
                if cred_data["resident"]:
                    user_handle = b64encode(bytearray(cred_data["user_handle"], encoding="utf-8"))
                    try:
                        self.new_cred = Credential.create_resident_credential(cred_id, rp_id, user_handle, private_key, sign_count)
                    except Exception as e:
                        print(f"!!! 1: {e}", file=sys.stderr)
                else:
                    try:
                        self.new_cred = Credential.create_non_resident_credential(cred_id, rp_id, private_key, sign_count)
                    except Exception as e:
                        print(f"!!! 2: {e}", file=sys.stderr)

                if new_cred:
                    print(f"XXX: {new_cred.to_dict()}", file=sys.stderr)



    @keyword
    def add_authenticator(self) -> None:
        if self.virtauthopts and self.new_cred:
            self.ctx.driver.add_virtual_authenticator(self.virtauthopts)
            print(f"XXX: {self.new_cred.to_dict()}", file=sys.stderr)
            self.ctx.driver.add_credential(self.new_cred)

    @keyword
    def load_webauthn_configs(self, config_file: str | None = None) -> None:
        # Move some stuff around, as a keyword, this should *throw*
        if config_file:
            self.config_file = Path(config_file)

        print(f"Loading {self.config_file}", file=sys.stderr)
        try:
            self.config = json.loads(self.config_file.read_text(encoding="utf-8"))
            if self.config:
                self.accounts = self.config.keys()
        except Exception as e:
            print(f"Unable to load config from {str(self.config_file)}: {e}", file=sys.stderr)

    @keyword
    def initial_webauthn_keyword(self: "SeleniumWebAuthn") -> None:
        pass
