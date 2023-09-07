from flask import Flask # from the flask module import the Flask class

# OOP -> Object oriented paradigm

app = Flask(__name__)     # Creates an instance of the Flask class.
# object


@app.get("/")           #Flask decorator that maps view functions to routes
def about_me():         #Our view function
    me ={               # Python dictionary
        "first_name": "Rafael",
        "last_name":   "GPL",
        "hobbies":     "DIY stuff",
        "is_active": True
    }
    return me           # Return statement (returned caller)

