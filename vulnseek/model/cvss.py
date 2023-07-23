from config.config import config_parse
from model.interface import StoreInterface
from model.structure.history import HistoryStructure


class CvssStore(StoreInterface):
    """Storage of CVSS scores of all Attacks"""

    def __init__(self):
        super().__init__("cvss")

    def ensure_table_exists(self):
        self.cur.execute(
            f"""
            DROP TABLE IF EXISTS {self.table_name};

            CREATE TABLE {self.table_name} (
                scan_type TEXT PRIMARY KEY,
                score REAL NOT NULL
            );

            INSERT INTO
                cvss_score (scan_type, score)
            VALUES
                ('dir_bf', 5.3);
            """
        )
        self.conn.commit()

    def get_by_scan_type(self, scan_type: str) -> float:
        self.cur.execute(
            f"""
            SELECT score
            FROM {self.table_name}
            WHERE
                scan_type = %s
            """,
            (scan_type,),
        )
        return self.cur.fetchone()[0]
