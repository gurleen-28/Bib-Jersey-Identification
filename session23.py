from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class MongoDBHelper:

    def __init__(self, collection="users"):
        uri = "mongodb+srv://Gurleen:atpl@cluster0.rerlhj8.mongodb.net/?appName=Cluster0"



        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1')) 

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        # Get reference to the database
        self.db = client['Python']
        self.collection = self.db[collection]

    def insert(self, document):
        result = self.collection.insert_one(document)
        print("Document inserted in Collection:", self.collection.name)
        # print("result is:", result, result.__inserted_id)
        print("result is:", result)
        return result

    # query as input will act as condition
    # what to delete, what to fetch, what to update 
    def fetch(self, query=""):
        documents = self.collection.find(query)
        return list(documents)
    
    def delete(self, query=""):
        result = self.collection.delete_one(query)
        print("result is:", result)
        return result

    def update(self, document, query):
        document_to_upate = {'$set': document}
        result = self.collection.update_one(query, document_to_upate)
        print("result is:", result)
        return result