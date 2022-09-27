from flask import Flask
app = Flask(__name__)
app.secret_key = "it's a secret to everybody!"

#init.py is basically importing Flask, get this app variable loaded up "app = Flask(__name__)" and setup the secret key, 
#and its also taking the variable "app" and importing it into server.py