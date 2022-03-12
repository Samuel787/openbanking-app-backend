import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dbmanager import db
from controller import addBook, addForexData, addForexNews, getFXData, getNewsData
from util.forex_data_schema import forex_data_schema
from util.forex_news_schema import forex_news_schema
from util.fx_get_schema import fx_get_schema

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
db.init_app(app)
# from models import Book
# from models import Forex_Data

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_book():
    print("incoming request")
    name=request.args.get('name')
    author=request.args.get('author')
    published=request.args.get('published')
    return addBook(name, author, published)

@app.route("/data", methods=["POST"])
def add_forex_data():
    if request.method == "POST":
        date=request.json["date"]
        price=request.json["price"]
        open=request.json["open"]
        high=request.json["high"]
        low=request.json["low"]
        change_percent=request.json["change_percent"]
        difference=request.json["difference"]
        label=request.json["label"]
        try:
            date, price, open, high, low, change_percent, difference, label = forex_data_schema(date, price, open, high, low, change_percent, difference, label)
            return addForexData(date, price, open, high, low, change_percent, difference, label)
        except Exception as e:
            return str(e)

@app.route("/news", methods=["POST", "GET"])
def add_forex_news():
    if request.method == "POST":
        date=request.json["date"]
        title=request.json["title"]
        article=request.json["article"]
        try:
            date, title, article = forex_news_schema(date, title, article)
            return addForexNews(date, title, article)
        except Exception as e:
            return str(e)
    elif request.method == "GET":
        num = request.args.get("limit")
        try:
            if int(num) <= 0:
                raise Exception("limit should be at least 1")
            return getNewsData(num)
        except Exception as e:
            return str(e)

@app.route("/fx", methods=["GET"])
def get_fx_data():
    if request.method == "GET":
        start_date=request.args.get('start')
        end_date=request.args.get("end")
        try:
            start_date, end_date = fx_get_schema(start_date, end_date)
            return getFXData(start_date, end_date)
        except Exception as e:
            return str(e)

@app.route("/getall")
def get_all():
    try:
        books=Book.query.all()
        return  jsonify([e.serialize() for e in books])
    except Exception as e:
	    return(str(e))

@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        book=Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
	    return(str(e))




if __name__ == '__main__':
    app.run()