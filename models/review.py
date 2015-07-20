from flockbot.models import Base
from helpers.functions import match
from sqlalchemy import Column, Integer, String

class Review(Base):
    __tablename__ = 'review'

    id     = Column(String, primary_key=True)
    author = Column(String)
    date   = Column(Integer)
    url    = Column(String)
    title  = Column(String)

    def __init__(self, id, author, date, url, title):
        self.id = id
        self.author = author
        self.date = date
        self.url = url
        self.title = title

    @staticmethod
    def get(session, ident):
        return session.query(Review).filter(Review.id == ident).first()

    @staticmethod
    def get_by(session, author=None, title=None, limit=50):
        query = session.query(Review)
        if author:
            query.filter(Review.author == author.lower())
        query.order_by(Review.date.desc())
        if title:
            scores = []
            for row in query.all():
                score = match(row.title, title)
                scores.append( (score, row) )
            scores.sort(key=lambda x: x[0], reverse=True)
            return [score[1] for score in scores[0:limit] if score[0] > 66]
        return query.limit(limit).all()



        