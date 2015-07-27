from controllers import ListReviewsController

def _init_controllers(bot):
    list_reviews_controller = ListReviewsController(
        reddit=bot.reddit,
        database=bot.get_database(),
        list_length=10
    )
    fetch_reviews_controller = FetchReviewsController(
        reddit=bot.reddit,
        database=bot.get_database()
    )
    bot.attach_controller(list_reviews_controller)
    bot.attach_controller(fetch_reviews_controller)

def register(bot):
    _init_controllers(bot)
    bot.register_callback(
        'submission',
        r'.', # match anything
        'FetchReviewsController@add_review'
    )

    bot.register_callback(
        ['message', 'submission'],
        # match name mentions not followed by `(any ) ['"`]`
        r'''/u/cigar_bot (?!(?:any )?['`"])''',
         'ListreviewsController@list_reviews'
    )
    bot.register_callback(
        ['message', 'submission'],
        r'''/u/cigar_bot [`'"](.+?)[`'"]''',
        'ListreviewsController@search_reviews'
    )
    bot.register_callback(
        ['message, submission'],
        r'''/u/cigar_bot any [`'"](.+?)[`'"]''',
        'ListReviewsController@list_any'
    )
