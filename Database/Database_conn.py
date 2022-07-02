import pymongo


class databaseConn:

    def __init__(self):
        self.mongo_url = "mongodb://localhost:27017/"
        self.database = "BackOrder"
        self.collection = "BackOrder"

    def DatabaseConn(self,data):
        client = pymongo.MongoClient(self.mongo_url)
        dataBase = client[self.database]
        collection = dataBase[self.collection]
        collection.insert_one(data)

