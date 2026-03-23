from Abstract.AbstractRepo import AbstractRepo
from psycopg2 import sql


class UsersRepo(AbstractRepo):

    def get_all(self):
        sql = """SELECT * FROM users"""
        return self.conn.execute(sql, fetch=True)

    def get_by_id(self, user_id):
        sql = """SELECT * FROM users WHERE id = %s"""
        return self.conn.execute(sql, (user_id,), fetch=True)

    def get_by_username_and_password(self, username, password):
        sql = """SELECT * FROM users WHERE username = %s AND password = %s"""
        return self.conn.execute(sql, (username, password), fetch=True)

    def add(self, user):
        sql = """INSERT INTO users (username, password) VALUES (%s, %s)"""
        self.conn.execute(sql, (user['username'], user['password']))

    def update_column(self, user_id, column, newValue):
        table = 'users'
        query = sql.SQL("UPDATE {table} SET {column} = %s WHERE id = %s").format(
            table=sql.Identifier(table),
            column=sql.Identifier(column)
        )
        self.conn.execute(query, (newValue, user_id))

    def delete_by_id(self, user_id):
        sql = """DELETE FROM users WHERE id = %s"""
        self.conn.execute(sql, (user_id,))
