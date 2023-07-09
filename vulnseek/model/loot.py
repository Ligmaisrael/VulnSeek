import psycopg2
from config.config import config_parse
from model.structure.loot import LootStructure
from model.interface import StoreInterface


class LootStore(StoreInterface):
    """Storage of loot from an Attack"""

    def __init__(self):
        self.table_name = config_parse("config/db.conf", "tables").get("loot")
        super().__init__()

    def ensure_table_exists(self):
        self.cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                loot_id SERIAL PRIMARY KEY,
                scan_id INTEGER,
                endpoint TEXT NOT NULL,
                payload TEXT NOT NULL,
                response_code INTEGER NOT NULL,
                response_headers TEXT NOT NULL,
                response_body TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def store_one(self, loot_structure: LootStructure):
        self.cur.execute(
            f"""
            INSERT INTO {self.table_name}
                (scan_id, endpoint, payload, response_code, response_headers, response_body)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                loot_structure.scan_id,
                loot_structure.endpoint,
                loot_structure.payload,
                loot_structure.response_code,
                loot_structure.response_headers,
                loot_structure.response_body,
            ),
        )
        self.conn.commit()
