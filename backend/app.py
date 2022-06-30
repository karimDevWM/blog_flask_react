from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_marshmallow import Marshmallow
import os

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/blog_flask_react'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'body', 'date')

# for one article
article_schema = ArticleSchema()
# for many articles
articles_schema = ArticleSchema(many=True)

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
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    
    return jsonify(results)


@app.route('/get/<int:id>', methods= ['GET'])
def post_details(id):
    article = Articles.query.get(id)
    result = article_schema.dump(article)
    
    return jsonify(result)

@app.route('/add', methods= ['POST'])
def add_article():
    title = request.json['title']
    body = request.json['body']
    
    articles = Articles(title, body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)


@app.route('/update/<int:id>', methods= ['PUT'])
def update_article(id):
    # get the article from model
    article = Articles.query.get(id)
    
    
    title = request.json['title']
    body = request.json['body']
    
    # set object fields by requested json values
    article.title = title
    article.body = body
    
    # commit the database
    db.session.commit()
    
    return article_schema.jsonify(article)


@app.route('/delete/<int:id>', methods= ['DELETE'])
def delete_article(id):
    article = Articles.query.get(id)
    
    db.session.delete(article)
    
    db.session.commit()
    
    return article_schema.jsonify(article)


if __name__ == '__main__':
    app.run(debug=True)