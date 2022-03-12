from models import Book, Forex_Data, Forex_News
from dbmanager import db
import datetime
from flask import jsonify

def addBook(name, author, published):
    try:
        book=Book(
            name=name,
            author=author,
            published=published
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
	    return(str(e))

def addForexData(date, price, open, high, low, change_percent, difference, label):
    try:
        date = date.split("-")
        date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        forexData=Forex_Data(
            date=date,
            price=price,
            open=open,
            high=high,
            low=low,
            change_percent=change_percent,
            difference=difference,
            label=label
        )
        db.session.add(forexData)
        db.session.commit()
        return "Forex Data Added. data id={}".format(forexData.id)
    except Exception as e:
        return (str(e))

def addForexNews(date, title, article):
    try:
        date = date.split("-")
        date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        forexNews = Forex_News(
            date=date,
            title=title,
            article=article
        )
        db.session.add(forexNews)
        db.session.commit()
        return "Forex News Added. news id={}".format(forexNews.id)
    except Exception as e:
        return (str(e))

def getFXData(start_date, end_date):
    try:
        qry2 = Forex_Data.query.filter(Forex_Data.date.between(start_date, end_date)).all()
        result = []
        for forexData in qry2:
            result.append(forexData.serialize())
        return jsonify(result)
    except Exception as e:
        return (str(e))

def getNewsData(limit):
    try:
        qry = Forex_News.query.order_by(Forex_News.date.desc()).limit(limit).all()
        result = []
        for forexNews in qry:
            result.append(forexNews.serialize())
        return jsonify(result)
    except Exception as e:
        return (str(e))
        
