from config.config import config_parse
from model.interface import StoreInterface
from model.structure.history import HistoryStructure


class HistoryStore(StoreInterface):
    """Storage of all Attacks ran on all targets"""

    def __init__(self):
        super().__init__("history")

    def ensure_table_exists(self):
        self.cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                scan_id SERIAL PRIMARY KEY,
                scan_type TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                target_url TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def store_one(self, scan_structure: HistoryStructure):
        self.cur.execute(
            f"""
            INSERT INTO {self.table_name}
                (scan_type, target_url)
            VALUES
                (%s, %s)
            RETURNING
                scan_id
            """,
            (
                scan_structure.scan_type,
                scan_structure.target_url,
            ),
        )
        self.conn.commit()
        return self.cur.fetchone()[0]

    def view_latest_one(self) -> tuple:
        self.cur.execute(
            f"""
            SELECT *
            FROM {self.table_name}
            ORDER BY
                timestamp
                DESC
            LIMIT 1
            """
        )
        return self.cur.fetchone()

    def view_latest_n(self, n: int, offset: int) -> list[tuple]:
        self.cur.execute(
            f"""
            SELECT *
            FROM {self.table_name}
            ORDER BY
                timestamp
                DESC
            LIMIT {n}
            OFFSET {offset}
            """
        )
        return self.cur.fetchall()
