import pprint

from requests.structures import CaseInsensitiveDict


class LootStructureBuilder:
    def __init__(self) -> None:
        self.loot_structure = LootStructure()

    def build(self):
        return self.loot_structure

    def scan_id(self, scan_id):
        self.loot_structure.scan_id = scan_id
        return self

    def endpoint(self, endpoint):
        self.loot_structure.endpoint = endpoint
        return self

    def payload(self, payload):
        self.loot_structure.payload = payload
        return self

    def response_code(self, response_code):
        self.loot_structure.response_code = response_code
        return self

    def response_headers(self, response_headers: CaseInsensitiveDict):
        pretty_headers = (
            pprint.pformat(dict(response_headers))
            .removeprefix("{")
            .removesuffix("}")
            .replace(",", "")
            .replace("\n ", "\n")
        )
        self.loot_structure.response_headers = pretty_headers
        return self

    def response_body(self, response_body):
        self.loot_structure.response_body = response_body
        return self


class LootStructure:
    def __init__(self):
        self.scan_id = None
        self.endpoint = None
        self.payload = None
        self.response_code = None
        self.response_headers = None
        self.response_body = None

    @staticmethod
    def builder() -> LootStructureBuilder:
        return LootStructureBuilder()
