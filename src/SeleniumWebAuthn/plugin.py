from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary import SeleniumLibrary

# from selenium.webdriver.common.virtual_authenticator import Credential
from selenium.webdriver.common.virtual_authenticator import VirtualAuthenticatorOptions

from pathlib import Path
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

        if self.config:
            for account_name in self.config.keys():
                account = self.config[account_name]
                if "autoAdd" in account and account["autoAdd"]:
                    if not self.virtauthopts:
                        self.virtauthopts = VirtualAuthenticatorOptions(
                            VirtualAuthenticatorOptions.Protocol.CTAP2,
                            VirtualAuthenticatorOptions.Transport.USB,
                            True,
                            True,
                            True,
                            True,
                        )

    @keyword
    def add_authenticator(self) -> None:
        if self.virtauthopts:
            self.ctx.driver.add_virtual_authenticator(self.virtauthopts)

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
