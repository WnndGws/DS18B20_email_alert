#!/usr/bin/python3
##
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #the route to the url
def homepage():
    data = [[0,3],[4,5],[8,1],[9,3]]
    return render_template("main.html", list_of_data=data)

if __name__ == "__main__":
    app.run()
