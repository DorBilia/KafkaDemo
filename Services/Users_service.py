import hashlib


class UsersService:
    def __init__(self, repo):
        self.repo = repo

    def authenticate(self, username, password):
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        user = self.repo.get_by_username_and_password(username, hashed_password)  # array of tuples
        if not user:
            return False
        return user[0][0]
