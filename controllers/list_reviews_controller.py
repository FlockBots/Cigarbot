from controllers import FetchReviewsController
from flockbot.decorators import callback
from models import Review
import views

class ListReviewsController():
    def __init__(self, database, reddit, list_length):
        self.database = database
        self.fetcher  = FetchReviewsController(database, reddit)
        self.list_length = list_length

    def __del__(self):
        self.database.commit()
        self.database.close()

    def list_reviews(self, editable, match):
        author = editable.author.name.lower()
        self.fetcher.fetch_reviews(author)

        reviews = Review.get_by(
            session=self.database,
            author=author,
            limit=self.list_length
        )

        return views.reviewlist(editable.author, reviews)

    def search_reviews(self, editable, match):
        author = editable.author.name.lower()
        self.fetcher.fetch_reviews(author)
        keywords = match[0] 
        reviews = Review.get_by(
            session=self.database,
            author=author,
            title=keywords,
            limit=self.list_length,
        )
        return views.searchresults(editable.author, reviews, keywords)

    def list_any(self, editable, match):
        self.fetcher.fetch_reviews()
        keyword = match[0]
        reviews = Review.get_by(
            session=self.database,
            title=keywords
        )
        return views.anyresults(reviews)
