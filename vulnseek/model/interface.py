import psycopg2
from psycopg2.extensions import connection
from config.config import config_parse


class StoreInterface:
    """Interface for storage to db"""

    def __init__(self, table_name_key):
        self.conn = self._connect()
        self.cur = self.conn.cursor()
        self.table_name = config_parse("config/db.conf", "table_names").get(
            table_name_key
        )
        self.ensure_table_exists()

    def _connect(self) -> connection:
        """
        Wrapper function for type definition
        """
        dsn_dict = config_parse("config/db.conf", "postgresql")
        return psycopg2.connect(**dsn_dict)

    def ensure_table_exists(self):
        """
        Ensures that the table in context exists
        This will be called by __init__()
        """
        raise NotImplementedError

    def store_one(self):
        """
        Stores 1 row of loot to db
        """
        raise NotImplementedError
