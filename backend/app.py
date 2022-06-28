from email.policy import default
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/blog_flask_react'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    date = db.Column(db.DateTime, default = datetime.datetime.now())
    
    def __init__(self, title, body) -> None:
        self.title = title
        self.body = body


@app.route('/get', methods= ['GET'])
def get_articles():
    return jsonify({"Hello":"World"})


if __name__ == '__main__':
    app.run(debug=True)