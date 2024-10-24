from Session17c import MongoDBHelper
from Session17A import User
from bson.objectid import ObjectId # import ObjectId, if you wish to fetch doc based on HashCode
import datetime
from tabulate import tabulate

def main():

    print("Welcome to MongoDB Test App")
    dbHelper = MongoDBHelper()

    """
    customer = Customer()
    customer.add_customer_details()
    document = vars(customer)

    dbHelper.insert(document)
    """

    # query = {"email": "john@example.com"}
    # query = {"email": "john@example.com", "phone": "8976532786"}

    # Fetch on the basis of Unique ID -> ObjectId
    # query = {"_id": ObjectId("668b8ca7bd74b1f9ef70d485")}

    # dbHelper.delete(query)

    query = {"email": "george@example.com"}
    document_data_to_update = {"name": "George W", "age": 32, "created_on":datetime.datetime.now()}

    # dbHelper.update(document=document_data_to_update, query=query)

    users = dbHelper.fetch()
    # users = dbHelper.fetch(query)
    # for user in users:
    #     print(user)