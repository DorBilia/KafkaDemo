from abc import abstractmethod
from DB.DB_handler import DBHandler


class AbstractRepo:
    def __init__(self, conn: DBHandler):
        self.conn = conn

    @abstractmethod
    def add(self, toAdd):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete_by_id(self, id):
        pass

    @abstractmethod
    def update_column(self, id, column, newValue):
        pass