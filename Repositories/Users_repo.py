from DB.DB_handler import DBHandler


class UsersRepo:
    def __init__(self):
        self.conn = DBHandler()

    def get_user_id_by_name(self, user_name):  # to be changed
        sql = f"""SELECT id FROM users WHERE username = %s """
        return self.conn.execute(sql,(user_name,), fetch=True)[0][0]
