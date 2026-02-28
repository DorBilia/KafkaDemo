import psycopg2


class DBConnection:  # Singleton class
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="mypassword",
                host='localhost',
                port=5555,
            )
        return self._instance

    @staticmethod
    def get_instance():
        if DBConnection._instance is None:
            DBConnection._instance = DBConnection()
        return DBConnection._instance

