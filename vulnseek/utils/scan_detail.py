import os

from model.history import HistoryStore
from model.loot import LootStore
from model.structure.history import HistoryStructure
from model.structure.loot import LootStructure
from prettytable import PrettyTable
from utils.print import clear_screen_with_message
from utils.prompt import prompt_param_required, validate_number_selection

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

        scan_detail_menu(tbl.get_string())


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


def scan_detail_menu(detail_view: str):
    print(detail_view)
    print("1. Save full scan result to file")
    print("0. Back to main menu")

    while True:
        choice = validate_number_selection(max=1)

        if choice == 0:
            break
        elif choice == 1:
            success = export_to_md_file()
            if success:
                break


def export_to_md_file() -> bool:
    filename = prompt_param_required("desired filename without extension")
    if os.path.isfile(filename):
        print(f'File "{filename}.md" exists, please input a different name')
        return False
    output_file = open(filename + ".md", "w")

    scan = _export_scan_history(output_file)
    _export_scan_loots(output_file, scan)

    output_file.close()
    print(f'Successfully saved to "{filename}.md"')
    print("Now returning you to the main menu")
    input()
    return True


def _export_scan_history(output_file):
    history_store = HistoryStore()
    scan_from_db = history_store.view_latest_one()
    scan = HistoryStructure.from_row(scan_from_db)
    output_file.write(scan.export_as_md())
    return scan


def _export_scan_loots(output_file, scan: HistoryStructure):
    loot_store = LootStore()
    loots_from_db = loot_store.get_by_scan_id(scan.scan_id)
    output_file.write("## Successful Payloads\n\n")
    if len(loots_from_db) == 0:
        output_file.write("No payloads were successful in this attack\n")
    else:
        for loot_from_db in loots_from_db:
            loot = LootStructure.from_row(loot_from_db)
            output_file.write(loot.export_as_md())
