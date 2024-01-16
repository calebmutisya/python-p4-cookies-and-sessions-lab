#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles')
def index_articles():
    #Placeholder for index_articles route
    return jsonify({'message':'Welcome to the articles index page!'})

@app.route('/articles/<int:id>')
def show_article(id):
    #Initialize 'page_views' in session if not present
    session['page_views']= session.get('page_views',0)
    #Increase page views for each request
    session['page_views']+=1
    #Check if the user has viewed 3 or fewer pages
    if session['page_views'] <= 3:
        #Replace the following line with your actual logic to fetch article data
        article_data={'id':id, 'title':f'Article{id}', 'content': f'Content for Article {id}'}
        return jsonify({'article': article_data})
    else:
        #If the user has viewed more than 3 pages , return an error message
        return jsonify ({'message': 'Maximum pageview limit reached'}), 401
    

if __name__ == '__main__':
    app.run(port=5555)
