from controllers import ListReviewsController

def _init_controllers(bot):
    list_reviews_controller = ListReviewsController(
        reddit=bot.reddit,
        database=bot.get_database(),
        list_length=10
    )

    bot.attach_controller(list_reviews_controller)


def register(bot):
    _init_controllers(bot)
    bot.register_callback('message', r'''/u/cigar_bot [^'"`]''', 'ListreviewsController@list_reviews')
    bot.register_callback('message', r'''/u/cigar_bot [`'"](.+?)[`'"]''', 'ListreviewsController@search_reviews')
