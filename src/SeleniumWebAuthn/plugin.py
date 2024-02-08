from SeleniumLibrary.base import LibraryComponent, keyword
from SeleniumLibrary import SeleniumLibrary


class SeleniumWebAuthn(LibraryComponent):
    def __init__(self: "SeleniumWebAuthn", ctx: SeleniumLibrary, configfile: str | None = None)-> None:
        LibraryComponent.__init__(self, ctx)

    @keyword
    def initial_webauthn_keyword(self: "SeleniumWebAuthn") -> None:
        pass
