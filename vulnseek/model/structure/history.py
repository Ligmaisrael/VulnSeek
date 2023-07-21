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
