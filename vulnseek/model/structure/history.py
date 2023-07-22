from textwrap import dedent


class HistoryStructureBuilder:
    def __init__(self) -> None:
        self.history_structure = HistoryStructure()

    def build(self):
        return self.history_structure

    def scan_id(self, scan_id):
        self.history_structure.scan_id = scan_id
        return self

    def scan_type(self, scan_type):
        if scan_type not in HistoryStructure.supported_scan_types:
            raise AttributeError(scan_type)
        self.history_structure.scan_type = scan_type
        return self

    def timestamp(self, timestamp):
        self.history_structure.timestamp = timestamp
        return self

    def target_url(self, target_url):
        self.history_structure.target_url = target_url
        return self


SCAN_TYPE_TO_SCAN_NAME = {
    "dir_bf": "Directory brute force",
}


class HistoryStructure:
    supported_scan_types = ["dir_bf"]

    def __init__(self):
        self.scan_id = None
        self.scan_type = None
        self.timestamp = None
        self.target_url = None

    @staticmethod
    def builder() -> HistoryStructureBuilder:
        return HistoryStructureBuilder()

    @staticmethod
    def from_row(row):
        return (
            HistoryStructure.builder()
            .scan_id(row[0])
            .scan_type(row[1])
            .timestamp(row[2])
            .target_url(row[3])
            .build()
        )

    def export_as_md(self) -> str:
        return dedent(
            f"""
            # Scan Overview

            - Scan type: {SCAN_TYPE_TO_SCAN_NAME.get(self.scan_type)}
            - Time of scan: {self.timestamp}
            - Scan target: {self.target_url}
            
            """
        )
