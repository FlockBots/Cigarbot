from models import Review

class FetchReviewsController:
    def __init__(self, database, reddit):
        self.database = database
        self.reddit = reddit

    def __del__(self):
        self.database.commit()
        self.database.close

    def add_review(self, editable, match):
        blacklist = ['content', 'weekly']
        for word in blacklist:
            if word in editable.title.lower():
                return
        entry = Review(
            id=editable.id,
            author=editable.author.name.lower(),
            date=int(editable.original.created_utc),
            url=editable.permalink,
            title=editable.original.title
        )
        self.database.add(entry)
        self.database.commit()

    def fetch_reviews(self, author):
        reviews = self.reddit.search(
            query="author:{}".format(author),
            subreddit="cigarreview",
            sort="new",
            limit=None
        )
        for review in reviews:
            if Review.get(self.database, review.id):
                break
            entry = Review(
                id=review.id,
                author=review.author.name.lower(),
                date=int(review.created_utc),
                url=review.permalink,
                title=review.title
            )
            self.database.add(entry)
        self.database.commit()
