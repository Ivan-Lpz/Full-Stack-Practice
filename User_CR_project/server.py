from flask_app import app
from flask_app.controllers import main
#this is also where you would add more controllers, currently we only have one controller and it's called "main.py" but we only
#need to import the name.

if __name__ == "__main__":
    app.run(debug=True)


#everything starts running from server.py
#this is where it begins and thats it.