from DB.DB_handler import DBHandler
from Abstract.AbstractRepo import AbstractRepo


class UsersRepo(AbstractRepo):
    def __init__(self):
        self.conn = DBHandler()

    def get_user_id_by_name(self, user_name):  # to be changed
        sql = """SELECT id FROM users WHERE username = %s """
        return self.conn.execute(sql, (user_name,), fetch=True)[0][0]

    def get_all(self):
        sql = """SELECT * FROM users"""
        return self.conn.execute(sql, fetch=True)

    def get_by_id(self, user_id):
        sql = """SELECT * FROM users WHERE id = %s"""
        return self.conn.execute(sql, (user_id,), fetch=True)

    def add(self, user):
        sql = """INSERT INTO users (username, password) VALUES (%s, %s)"""
        self.conn.execute(sql, (user['username'], user['password']))

    def update_column(self, user_id, column, newValue):
        sql = """UPDATE users SET %s = %s
            WHERE id = %s """
        self.conn.execute(sql, params=(column, newValue, user_id))

    def delete_by_id(self, user_id):
        sql = """DELETE FROM users WHERE id = %s"""
        self.conn.execute(sql, (user_id,))
