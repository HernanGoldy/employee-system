from flask import Flask
from flask import render_template
from flaskext import MySQL

app = Flask()
mysql = MySQL()

if __name__ == '__main__':
    app.run(debug=True)
