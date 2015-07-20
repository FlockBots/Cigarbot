from controllers import FetchReviewsController
from flockbot.controllers import ControllerMeta
from flockbot.decorators import callback
from models import Review
import views

class ListReviewsController(metaclass=ControllerMeta):
    def __init__(self, database, reddit, list_length):
        self.database = database
        self.fetcher  = FetchReviewsController(database, reddit)
        self.list_length = list_length

    def __del__(self):
        self.database.commit()
        self.database.close()

    @callback('message', r'/u/cigar_bot')
    def list_reviews(self, match, editable):
        author = editable.author.name.lower()
        self.fetcher.fetch_reviews(author)

        reviews = Review.get_by(
            session=self.database,
            author=author,
            limit=self.list_length
        )

        return views.reviewlist(editable.author, reviews)

    @callback('message', r'/u/cigar_bot [`\'"](.+?)[`\'"]')
    def search_reviews(self, match, editable):
        author = editable.author.name.lower()
        self.fetcher.fetch_reviews(author)
        reviews = Review.get_by(
            session=self.database,
            author=author,
            title=match.group(1),
            limit=self.list_length,
        )
        return views.reviewlist(editable.author, reviews)
