from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary import SeleniumLibrary
from selenium.webdriver.common.virtual_authenticator import Credential, VirtualAuthenticatorOptions

from pathlib import Path
import sys
import json


class SeleniumWebAuthn(LibraryComponent):
    def __init__(self: "SeleniumWebAuthn", ctx: SeleniumLibrary, config_file: str | None = None)-> None:
        LibraryComponent.__init__(self, ctx)
        self.config_file = config_file
        self.config = None
        self.virtauthopts = None


        if config_file:
            self.config_file = Path(config_file)
        else:
            self.config_file = Path("webauthnconfig.json")

        self.load_webauthn_configs(self.config_file)

        if self.config:
            for account in self.accounts:
                if getattr(self.accounts, "autoAdd", False):
                    if not self.virtauthopts:
                        self.virtauthopts = VirtualAuthenticatorOptions()

            pass


    @keyword
    def load_webauthn_configs(self, config_file: str | None = None) -> None:
        # Move some stuff around, as a keyword, this should *throw*
        if config_file:
            self.config_file = Path(config_file)

        try:
            self.config = json.loads(self.config_file.read_text(encoding="utf-8"))
            self.accounts = self.config.keys()
        except Exception:
            print(f"Unable to load config from {str(self.config_file)}", file=sys.stderr)



    @keyword
    def initial_webauthn_keyword(self: "SeleniumWebAuthn") -> None:
        pass
