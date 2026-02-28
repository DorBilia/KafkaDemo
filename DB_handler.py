import psycopg2


class DBConnection:  # Singleton class
    conn = None

    def __new__(self):
        if self.conn is None:
            self.conn = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="mypassword",
                host='localhost',
                port=5555,
            )
        return self.conn

    def execute(self, query, params=None, fetch=False):
        cur = self.conn.cursor()
        cur.execute(query, params)
        if fetch:
            return cur.fetchall()
        self.conn.commit()
        cur.close()
