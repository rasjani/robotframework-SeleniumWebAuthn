from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary import SeleniumLibrary


class SeleniumWebAuthn(LibraryComponent):
    def __init__(self: "SeleniumWebAuthn", ctx: SeleniumLibrary, configfile) -> None:
        LibraryComponent.__init__(self, ctx)


    @keyword
    def initial_webauthn_keyword(self: "SeleniumWebAuth") -> None:
        pass
