from app import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

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

    def __init__(self, date, price, open, high, low, change_percent, difference, label):
        self.date = date
        self.price = price
        self.open = open
        self.high = high
        self.low = low
        self.change_percent = change_percent
        self.difference = difference
        self.label = label

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
            "label": self.label
        }

class Forex_News(db.Model):
    __table_name__ = "forexnews"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    title = db.Column(db.String())
    article = db.Column(db.String())

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




