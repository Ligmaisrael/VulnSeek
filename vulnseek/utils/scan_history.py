from model.history import HistoryStore
from model.structure.history import HistoryStructure
from prettytable import PrettyTable
from utils.prompt import validate_number_selection
from utils.scan_detail import ScanDetail


class ScanHistory:
    headers = ["Scan id", "Scan type", "Time of scan", "Scan target"]

    def __init__(self):
        self.history = HistoryStore()
        self.db_rows = None

    def get_last(self) -> HistoryStructure:
        db_row = self.history.view_latest_one()
        history_row = HistoryStructure.from_row(db_row)
        return history_row

    def view_history(self):
        self.db_rows = self.history.view_latest_n(50, 0)
        tbl = PrettyTable(ScanHistory.headers)
        tbl.add_rows(self.db_rows)
        tbl.del_column(ScanHistory.headers[0])
        add_numbers_col(tbl)

        self.scan_history_menu(tbl.get_string())

    def scan_history_menu(self, history_view: str):
        row_count = len(self.db_rows)
        while True:
            print(history_view)
            print(f"1-{row_count}. View scan detail")
            print("0. Back")
            choice = validate_number_selection(max=row_count)

            if choice == 0:
                break
            else:
                scan = HistoryStructure.from_row(self.db_rows[choice - 1])
                scan_detail = ScanDetail(scan)
                scan_detail.view()


def add_numbers_col(tbl: PrettyTable) -> PrettyTable:
    fieldname = "No"
    tbl._field_names.insert(0, fieldname)
    tbl._align[fieldname] = "c"
    tbl._valign[fieldname] = "t"
    for i, _ in enumerate(tbl._rows):
        tbl._rows[i].insert(0, i + 1)
