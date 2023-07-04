import psycopg2
from model.interface import AttackStoreInterface


class DirectoryBruteForceStore(AttackStoreInterface):
    def __init__(self, dsn_dict, table_name):
        super().__init__(dsn_dict, table_name)

    def ensure_table_exists(self):
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS dir_bf (
                id serial PRIMARY KEY,
                scan_id integer,
                endpoint text NOT NULL,
                content text NOT NULL
            )
            """
        )

    def store_one(self, endpoint, content):
        self.cur.execute(
            "INSERT INTO dir_bf (scan_id, endpoint, content) VALUES (%s, %s, %s)",
            (123, endpoint, content),
        )
        self.conn.commit()
