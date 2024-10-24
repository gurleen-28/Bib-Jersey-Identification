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

# Create the Object of Flask
# Which represents a Web Application
web_app = Flask("AirTrack")
db = MongoDBHelper()

@web_app.route("/") # Decorator
def index():

    # either you can return plain text
    # message = "Welcome to AC Management System. Its {}".format(datetime.datetime.now())

    # OR you can return HTML
    message = """
    <html>
    <head>
        <title>AirTrack</title>
    </head>
    <body>
        <center>
            <h3>Welcome to AC Management System</h3>
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

@web_app.route("/add-customer", methods=["POST"])
def add_customer_in_db():

    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }

    # Save user in DataBase i.e. MongoDB
    result = db.insert(customer_data)
    # message = "Welcome to Home Page. User ID is: {}".format(result.inserted_id)
    # return message

    # Write the data in the Session Object
    # This data can now be used anywhere in the project
    session['customer_id'] = str(result.inserted_id)
    session['name'] = customer_data["name"]
    session['email'] = customer_data["email"]

    # return render_template("home.html", name=session['name'], email=session['email'])
    return render_template("home.html", email=session['email'])


@web_app.route("/fetch-customer", methods=["POST"])
def fetch_customer_from_db():

    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }

    # Fetch customer in DataBase i.e. MongoDB
    result = db.fetch(query=customer_data)
    
    if len(result)>0:
         return render_template("home.html", email=session['email'])
    else:
        return "Customer Not Found. Please Try Again"


def main():

    # Run the App infinitely, till user wont quite
    web_app.run()
    # web_app.run(port=5001) # optionally you can give the port number

if __name__ == "__main__":
    main()