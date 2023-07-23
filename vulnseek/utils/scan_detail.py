from model.loot import LootStore
from model.structure.history import HistoryStructure
from prettytable import PrettyTable
from utils.export import export_to_md_file
from utils.print import clear_screen_with_message
from utils.prompt import validate_number_selection

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
        tbl = view_as_table(loots)

        if len(tbl) > 0:
            self.scan_detail_menu(tbl)

    def scan_detail_menu(self, detail_view: str):
        print(detail_view)
        while True:
            print("1. Save full scan result to file")
            print("0. Back")
            choice = validate_number_selection(max=1)

            if choice == 0:
                break
            elif choice == 1:
                success = export_to_md_file(self.scan_id)
                if success:
                    break


def view_as_table(loots: list) -> str:
    if len(loots) == 0:
        clear_screen_with_message("No payloads were successful during that scan")
        return ""

    loots = shorten_resp_body(loots)
    loots = add_newline_after_each_row(loots)

    tbl = PrettyTable(ScanDetail.headers)
    tbl.add_rows(loots)
    tbl.del_column(loot_id)
    tbl.del_column(scan_id)
    tbl._max_width = {resp_headers: 50, resp_body: 50}
    tbl.align[resp_headers] = "l"
    tbl.align[resp_body] = "l"

    return tbl.get_string()


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
