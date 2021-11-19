from pymongo import MongoClient


class MongoDB:

    def __init__(self):
        self.database_name = 'myenglish'
        self.client = MongoClient()

    def connect(self):
        return self.client[self.database_name]
