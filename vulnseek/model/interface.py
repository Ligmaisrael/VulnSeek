import psycopg2
from config.config import config_parse


class StoreInterface:
    """Interface for storage to db"""

    def __init__(self):
        dsn_dict = config_parse("config/db.conf", "postgresql")
        self.conn = psycopg2.connect(**dsn_dict)
        self.cur = self.conn.cursor()
        self.ensure_table_exists()

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
