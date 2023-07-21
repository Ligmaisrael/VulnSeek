from model.history import HistoryStore
from model.structure.history import HistoryStructure
from prettytable import PrettyTable


class ScanHistory:
    headers = ["Scan id", "Scan type", "Time of scan", "Scan target"]

    def __init__(self):
        self.history = HistoryStore()

    def get_last(self) -> HistoryStructure:
        db_row = self.history.view_latest_one()
        history_row = HistoryStructure.from_row(db_row)
        return history_row

    def view_history(self):
        db_rows = self.history.view_latest_n(50, 0)
        tbl = PrettyTable(ScanHistory.headers)
        tbl.add_rows(db_rows)
        tbl.del_column(ScanHistory.headers[0])

        print(tbl)
        input()
