import pprint
from textwrap import dedent


class LootStructureBuilder:
    def __init__(self) -> None:
        self.loot_structure = LootStructure()

    def build(self):
        return self.loot_structure

    def loot_id(self, loot_id):
        self.loot_structure.loot_id = loot_id
        return self

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

    def response_headers(self, response_headers):
        self.loot_structure.response_headers = response_headers
        return self

    def response_body(self, response_body):
        self.loot_structure.response_body = response_body
        return self


class LootStructure:
    def __init__(self):
        self.loot_id = None
        self.scan_id = None
        self.endpoint = None
        self.payload = None
        self.response_code = None
        self.response_headers = None
        self.response_body = None

    @staticmethod
    def builder() -> LootStructureBuilder:
        return LootStructureBuilder()

    @staticmethod
    def from_row(row):
        return (
            LootStructure.builder()
            .loot_id(row[0])
            .scan_id(row[1])
            .endpoint(row[2])
            .payload(row[3])
            .response_code(row[4])
            .response_headers(row[5])
            .response_body(row[6])
            .build()
        )

    def export_as_md(self) -> str:
        return (
            f"### {self.payload}\n"
            + dedent(
                f"""
                - Endpoint: {self.endpoint}
                - Payload: {self.payload}
                - Response code: {self.response_code}
                """
            )
            + "- Response headers:\n\n```\n"
            + self.response_headers
            + "\n```\n\n"
            + "- Response body:\n\n```html\n"
            + self.response_body
            + "\n```\n\n"
        )
