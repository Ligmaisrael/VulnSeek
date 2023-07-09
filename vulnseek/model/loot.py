import psycopg2
from config.config import config_parse
from model.structure.loot import LootStructure


class LootStore:
    """Storage of loot from an Attack"""

    def __init__(self):
        dsn_dict = config_parse("config/db.conf", "postgresql")
        self.conn = psycopg2.connect(**dsn_dict)
        self.cur = self.conn.cursor()
        self.table_name = config_parse("config/db.conf", "tables").get("loot")
        self.ensure_table_exists()

    def ensure_table_exists(self):
        """
        Ensures that the "loot" table exists
        This will be called by __init__()
        """

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
        """
        Stores 1 row of loot to db
        """

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
