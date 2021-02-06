import psycopg2 as psql
import psycopg2.extras


class HumansDatabaseManager:
    DB_NAME = 'human_api_db'
    USER = 'postgres'
    PASSWORD = 'postgres'
    HOST = 'db'

    def __init__(self):
        self._database = psql.connect(dbname=self.DB_NAME,
                                      user=self.USER,
                                      password=self.PASSWORD,
                                      host=self.HOST,
                                      cursor_factory=psycopg2.extras.RealDictCursor)

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, '_instance'):
            return cls._instance
        cls._instance = super().__new__(cls)
        return cls._instance

    def close_db(self):
        if self._database:
            self._database.close()

    def insert_data(self, data_dict, table_name='human'):
        query_fields = list(data_dict.keys())
        query_values = list(data_dict.values())
        query = (f'INSERT INTO {table_name} ({", ".join(query_fields)}) '
                 f'VALUES ({", ".join(["%s" for _ in range(len(query_values))])})')
        with self._database.cursor() as cursor:
            cursor.execute(query, query_values)
        self._database.commit()

    def get_all_data_dict(self, table_name='human'):
        with self._database.cursor() as cursor:
            cursor.execute(f'SELECT * FROM {table_name}')
            return cursor.fetchall()

    def get_data_by_id(self, identifier):
        with self._database.cursor() as cursor:
            cursor.execute(f'SELECT * FROM human WHERE id = {identifier} ORDER BY id')
            return cursor.fetchone()

    def remove_data_by_id(self, identifier):
        with self._database.cursor() as cursor:
            cursor.execute(f'DELETE FROM human WHERE id = {identifier}')
        self._database.commit()

    def __del__(self):
        self.close_db()


db_manager = HumansDatabaseManager()
