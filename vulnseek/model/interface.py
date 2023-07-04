import psycopg2


class AttackStoreInterface:
    """Storage of loot from an Attack"""

    def __init__(self, dsn_dict, table_name):
        self.conn = psycopg2.connect(**dsn_dict)
        self.cur = self.conn.cursor()
        self.table_name = table_name
        self.ensure_table_exists()

    def ensure_table_exists(self):
        """
        Ensures that the table table_name exists
        This will be called by __init__()
        """
        raise NotImplementedError

    def store_one(self):
        """
        Stores 1 row of loot to db
        """
        raise NotImplementedError
