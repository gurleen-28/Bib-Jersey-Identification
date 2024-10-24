"""
    Web Application Development with Flask
    https://flask.palletsprojects.com/en/3.0.x/

    1. Install Flask in Virtual Env
       pip install Flask

    2. Create Object of Flask

    3. Create a Function, with route as /

    4. In main function run the Flas App using run()

    5. Return the HTML webapge as a template from function
"""

from flask import *
import datetime
import hashlib
from Session17c import MongoDBHelper
from bson.objectid import ObjectId

# Create the Object of Flask
# Which represents a Web Application
web_app = Flask("AirTrack")

db_helper = MongoDBHelper()

@web_app.route("/") # Decorator
def index():

    # either you can return plain text
    # message = "Welcome to AC Management System. Its {}".format(datetime.datetime.now())

    # OR you can return HTML
    message = """
    <html>
    <head>
        <title>AIRTRACK</title>
    </head>
    <body>
        <center>
            <h3>We are the AirTrack</h3>
        </center>
    </body>
    </html>
    """

    # return message

    # render_template is used to return web pages (html pages)
    return render_template("index.html")

@web_app.route("/register")
def register():
    return render_template("register.html")

@web_app.route("/home")
def home():
    if len(session["email"]) != 0:
        return render_template("home.html", name=session["name"], email=session["email"])
    else:
        return redirect("/")

@web_app.route("/success")
def success():
    return render_template("success.html", name=session["name"], email=session["email"])

@web_app.route("/error")
def error():
    return render_template("error.html", name=session["name"], email=session["email"])

@web_app.route("/logout")
def logout():
    # Reset the Data in Session Object
    session["email"] = ""
    session["name"] = ""
    return redirect("/")


@web_app.route("/add-customer", methods=["POST"])
def add_customer_in_db():


    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["customers"]
    # Save user in DataBase i.e. MongoDB
    result = db_helper.insert(customer_data)
    # message = "Welcome to Home Page. User ID is: {}".format(result.inserted_id)
    # return message

    # Write the data in the Session Object
    # This data can now be used anywhere in the project
    session['name'] = customer_data["name"]
    session['email'] = customer_data["email"]

    # return render_template("home.html", name=session['name'], email=session['email'])
    return render_template("home.html", name=session['name'], email=session['email'])

@web_app.route("/fetch-customer", methods=["POST"])
def fetch_customer_from_db():

    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    db_helper.collection = db_helper.db["customers"]
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=customer_data)

    print("result:", result)
    
    if len(result)>0:
        customer_data = result[0] # Get the dictionary from List 
        session['email'] = customer_data["email"]
        session['name'] = customer_data["name"]
        return render_template("home.html", name=session['name'], email=session['email'])
    else:
        return render_template("error.html", message="User Not Found. Please Try Again",
                               name=session["name"], email=session["email"])
    
    


@web_app.route("/add-customer", methods=["POST"])
def add_customer_in_db():

    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "AirTracker_email": session['email'],
        "AirTracker_name": session['name'],
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["customer"]
    # Save customer in DataBase i.e. MongoDB
    result = db_helper.insert(customer_data)
    return render_template("success.html", message = "Customer Added Successfully",
                           name=session["name"], email=session["email"])


@web_app.route("/update-customer/<id>")
def update_customer(id):
    print("Customer to be updated:", id)
    
    # Save customer ID in Session, which needs to be updated
    session["id"] = id
    
    # Fetch document from patient collection, where id matches
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["customers"]
    
    # result is a list
    result = db_helper.fetch(query=query)
    
    # As we will get the list of documents, and 0th index will be our document
    # with customer id matching the one we have passed
    customer_AT = result[0]

    return render_template("update-customer.html",
                           name=session["name"], 
                           email=session["email"], 
                           customer=customer_AT)


@web_app.route("/delete-customer/<id>")
def delete_customer(id):
    print("Customer to be deleted:", id)
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["customers"]
    db_helper.delete(query)
    return render_template("success.html", message = "Customer Deleted Successfully",
                           name=session["name"], email=session["email"])


@web_app.route("/update-customer-in-db", methods=["POST"])
def update_customer_in_db():

    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "AirTracker_email": session['email'],
        "AirTracker_name": session['name'],
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["patients"]

    query = {"_id": ObjectId(session["id"])}
    # Save customer in DataBase i.e. MongoDB
    result = db_helper.update(customer_data, query)
    return render_template("success.html", message = "Customer Updated Successfully",
                           name=session["name"], email=session["email"])


@web_app.route("/add-consultation/<id>")
def add_consultation(id):
    # Store the customer ID in Session, temporarily
    session["customer_id"] = id
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["patients"]
    
    # result is a list
    result = db_helper.fetch(query=query)
    
    # As we will get the list of documents, and 0th index will be our document
    # with customer id matching the one we have passed
    customer_AT = result[0]
    session["customer_name"] = customer_AT["name"]
    return render_template("add-consultation.html",
                           name=session["name"], email=session["email"],
                           customer_name = session["customer_name"]
                           )


@web_app.route("/add-consultation-in-db", methods=["POST"])
def add_consultation_in_db():

    # Create a Dictionary with Data from HTML Register Form
    consultation_data = {
        "complaints": request.form["complaints"],
        "temperature": request.form["temperature"],
        "noises": request.form["noises"],
        "service": request.form["service"],
        "water leakage": request.form["water leakage"],
        "remarks": request.form["remarks"],
        "followup": request.form['followup'],
        "AirTracker_email": session['email'],
        "AirTracker_name": session['name'],
        "customer_id": session["customer_id"],
        "customer_name": session["customer_name"],
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["consultations"]
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.insert(consultation_data)
    return render_template("success.html", message = "Consultation Added Successfully",
                           name=session["name"], email=session["email"])


@web_app.route("/fetch-customers")
def fetch_patients_from_db():

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "AirTracker": session["email"]
    }

    db_helper.collection = db_helper.db["customers"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=customer_data)
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("customers.html", customers=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message="Customers Not Found. Please Try Again",
                               name=session["name"], email=session["email"])


@web_app.route("/fetch-consultations")
def fetch_consultations_from_db():

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "AirTracker_email": session["email"]
    }

    db_helper.collection = db_helper.db["consultations"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=customer_data)
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("consultations.html", consultations=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message="Consultations Not Found. Please Try Again",
                               name=session["name"], email=session["email"])


@web_app.route("/fetch-consultations-of-customer/<id>")
def fetch_consultations_of_customer_from_db(id):

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "AirTracker_email": session["email"],
        "customer_id": id
    }

    db_helper.collection = db_helper.db["consultations"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=customer_data)
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("consultations.html", consultations=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message="Consultations Not Found. Please Try Again",
                               name=session["name"], email=session["email"])


@web_app.route("/search-customer")
def search_customer():
    return render_template("search.html", name=session["name"], email=session["email"])

@web_app.route("/search-customer-from-db", methods=["POST"])
def search_customer_from_db():
    customer_data = {
        "email": request.form["email"],
        "AirTracker_email": session["email"],
    }

    db_helper.collection = db_helper.db["customers"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=customer_data)
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        # Since, we will have only 1 customer searched, we will pass result[0]
        return render_template("customer-card.html", customer=result[0], 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message="Customer Not Found. Please Try Again",
                               name=session["name"], email=session["email"])


def main():
    
     # In order to use Session Tracking, create a Secret Key
    web_app.secret_key = "airtrack-key-v1"

    # Run the App infinitely, till user wont quite
    web_app.run()
    # web_app.run(port=5001) # optionally you can give the port number

if __name__ == "__main__":
    main()