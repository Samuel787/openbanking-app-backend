#  from app import db
from dbmanager import db
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())
    db.UniqueConstraint(name, author)

    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'author': self.author,
            'published':self.published
        }

class Forex_Data(db.Model):
    __tablename__ = 'forexdata'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    price = db.Column(db.Float())
    open = db.Column(db.Float())
    high = db.Column(db.Float())
    low = db.Column(db.Float())
    change_percent = db.Column(db.Float())
    difference = db.Column(db.Float())
    label = db.Column(db.Float())
    sma = db.Column(db.Float())
    ema = db.Column(db.Float())
    macd = db.Column(db.Float())
    macd_s = db.Column(db.Float())
    macd_h = db.Column(db.Float())
    roc = db.Column(db.Float())
    rsi = db.Column(db.Float())
    bollinger_up = db.Column(db.Float())
    bollinger_down = db.Column(db.Float())
    cci = db.Column(db.Float())
    db.UniqueConstraint(date)

    def __init__(self, date, price, open, high, low, change_percent, difference, label, sma, ema, macd, macd_s, macd_h, roc, rsi, bollinger_up, bollinger_down, cci):
        self.date = date
        self.price = price
        self.open = open
        self.high = high
        self.low = low
        self.change_percent = change_percent
        self.difference = difference
        self.label = label
        self.sma = sma
        self.ema = ema
        self.macd = macd
        self.macd_s = macd_s
        self.macd_h = macd_h
        self.roc = roc
        self.rsi = rsi
        self.bollinger_up = bollinger_up
        self.bollinger_down = bollinger_down
        self.cci = cci

    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "price": self.price,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "change_percent": self.change_percent,
            "difference": self.difference,
            "label": self.label,
            "sma": self.sma,
            "ema": self.ema,
            "macd": self.macd,
            "macd_h": self.macd_h,
            "roc": self.roc,
            "rsi": self.rsi,
            "bollinger_up": self.bollinger_up,
            "bollinger_down": self.bollinger_down,
            "cci": self.cci
        }

class Forex_News(db.Model):
    __table_name__ = "forexnews"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    title = db.Column(db.String())
    article = db.Column(db.String())
    db.UniqueConstraint(date, title)

    def __init__(self, date, title, article):
        self.date = date
        self.title = title
        self.article = article
    
    def __repr__(self):
        return "<id {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date,
            "title": self.title,
            "article": self.article
        }




