from model.loot import LootStore
from model.structure.history import HistoryStructure
from prettytable import PrettyTable


class ScanDetail:
    loot_id = "Loot id"
    scan_id = "Scan id"
    headers = [
        loot_id,
        scan_id,
        "Endpoint",
        "Payload",
        "Response code",
        "Response headers",
        "Response body",
    ]

    def __init__(self, scan_history: HistoryStructure) -> None:
        self.scan_id = scan_history.scan_id
        self.loot_store = LootStore()

    def view(self):
        loots = self.loot_store.get_by_scan_id(self.scan_id)
        tbl = PrettyTable(ScanDetail.headers)
        tbl.add_rows(loots)
        tbl.del_column(ScanDetail.loot_id)
        tbl.del_column(ScanDetail.scan_id)

        print(tbl)
        input()
