import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dbmanager import db
from controller import addBook, addForexData, addForexNews, deleteFXData, getFXData, getNewsData
from util.forex_data_schema import forex_data_schema
from util.forex_news_schema import forex_news_schema
from util.fx_get_schema import fx_get_schema
from util.fx_delete_schema import fx_delete_schema
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# adding cors 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
db.init_app(app)

@app.route("/")
@cross_origin()
def hello():
    return "Hello World!"

@app.route("/add")
@cross_origin()
def add_book():
    print("incoming request")
    name=request.args.get('name')
    author=request.args.get('author')
    published=request.args.get('published')
    return addBook(name, author, published)

@app.route("/data", methods=["POST"])
@cross_origin()
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
        sma=request.json["sma"]
        ema=request.json["ema"]
        macd=request.json["macd"]
        macd_s=request.json["macd_s"]
        macd_h=request.json["macd_h"]
        roc=request.json["roc"]
        rsi=request.json["rsi"]
        bollinger_up=request.json["bollinger_up"]
        bollinger_down=request.json["bollinger_down"]
        cci=request.json["cci"]
        try:
            date, price, open, high, low, change_percent, difference, label, sma, ema, macd, macd_s, macd_h, roc, rsi, bollinger_up, bollinger_down, cci = forex_data_schema(date, price, open, high, low, change_percent, difference, label, sma, ema, macd, macd_s, macd_h, roc, rsi, bollinger_up, bollinger_down, cci)
            return addForexData(date, price, open, high, low, change_percent, difference, label, sma, ema, macd, macd_s, macd_h, roc, rsi, bollinger_up, bollinger_down, cci)
        except Exception as e:
            return str(e)

@app.route("/news", methods=["POST", "GET"])
@cross_origin()
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

@app.route("/fx", methods=["GET", "DELETE"])
@cross_origin()
def get_fx_data():
    if request.method == "GET":
        start_date=request.args.get('start')
        end_date=request.args.get("end")
        try:
            start_date, end_date = fx_get_schema(start_date, end_date)
            return getFXData(start_date, end_date)
        except Exception as e:
            return str(e)
    elif request.method == "DELETE":
        date = request.args.get("date")
        try:
            date = fx_delete_schema(date)
            return deleteFXData(date)
        except Exception as e:
            return str(e)

if __name__ == '__main__':
    app.run()