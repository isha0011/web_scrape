from bookstore_scraper.helpers import conn_db
from bookstore_scraper.configs import credentials


class Database:
    def __init__(self):
        self.engine = conn_db(credentials.db_cred)
        self.conn = self.engine.connect()

    def create_table(self):
        try:
            self.conn.execute("""
                          CREATE TABLE IF NOT EXISTS sqlalch2 (
                              index int() not null
                              Category VARCHAR(100) NOT NULL,
                              Book_name VARCHAR(100) NOT NULL,
                              Price DECIMAL(10, 2) NOT NULL
                          )
                      """)

        except Exception as err:
            # self.Conn_obj.rollback()
            print(err)

    def insert(self, val):
        try:
            val.to_sql(con=self.engine, name='sqlalch2', if_exists='append')
        except Exception as err:
            print(err)


    def __del__(self):
        self.conn.close()
