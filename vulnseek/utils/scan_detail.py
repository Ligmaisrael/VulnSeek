from model.loot import LootStore
from model.structure.history import HistoryStructure
from prettytable import PrettyTable

loot_id = "Loot id"
scan_id = "Scan id"
endpoint = "Endpoint"
payload = "Payload"
resp_headers = "Response headers"
resp_body = "Response body"
resp_code = "Response code"


class ScanDetail:
    headers = [
        loot_id,
        scan_id,
        endpoint,
        payload,
        resp_code,
        resp_headers,
        resp_body,
    ]

    def __init__(self, scan_history: HistoryStructure) -> None:
        self.scan_id = scan_history.scan_id
        self.loot_store = LootStore()

    def view(self):
        loots = self.loot_store.get_by_scan_id(self.scan_id)
        loots = shorten_resp_body(loots)
        loots = add_newline_after_each_row(loots)

        tbl = PrettyTable(ScanDetail.headers)
        tbl.add_rows(loots)
        tbl.del_column(loot_id)
        tbl.del_column(scan_id)
        tbl._max_width = {resp_headers: 50, resp_body: 50}
        tbl.align[resp_headers] = "l"
        tbl.align[resp_body] = "l"

        print(tbl)
        input()


def shorten_resp_body(loots: list) -> list:
    shorteneds = []
    for loot in loots:
        loot_as_list = list(loot)
        loot_as_list[-1] = shorten_with_ellipsis(loot_as_list[-1], 300)
        shorteneds.append(loot_as_list)
    return shorteneds


def shorten_with_ellipsis(string: str, max_len: int) -> str:
    if len(string) > max_len:
        return string[:max_len] + "..."
    return string


def add_newline_after_each_row(loots: list) -> list:
    with_newlines = []
    for loot in loots:
        loot_as_list = list(loot)
        loot_as_list[-1] = loot_as_list[-1] + "\n"
        loot_as_list[-2] = loot_as_list[-2] + "\n"
        with_newlines.append(loot_as_list)
    return with_newlines
