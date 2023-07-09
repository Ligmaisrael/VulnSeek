from config.config import config_parse
from model.interface import StoreInterface
from model.structure.history import HistoryStructure


class HistoryStore(StoreInterface):
    """Storage of all Attacks ran on all targets"""

    def __init__(self):
        self.table_name = config_parse("config/db.conf", "tables").get("history")
        super().__init__()

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

    def get_new_scan_id(self):
        self.cur.execute(
            f"""
            SELECT
                scan_id
            FROM
                {self.table_name}
            ORDER BY
                scan_id
                DESC
            LIMIT 1
            """
        )
        last_scan_id = self.cur.fetchone()[0]
        return last_scan_id + 1
