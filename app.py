from flockbot import Bot
from flockbot import Callback
from controllers import ListReviewsController
from config import credentials

def load_controllers(cigarbot):
    list_reviews = ListReviewsController(
        cigarbot.get_database(),
        cigarbot.reddit,
        list_length=10
    )
    return [list_reviews]

def setup_bot():
    cigarbot = Bot()
    cigarbot.config.set_subscriptions(['flockbots'])
    cigarbot.login(
        'Review Lister for /r/CigarReview',
        credentials.oauth_info,
        credentials.refresh_token
    )

    for controller in load_controllers(cigarbot):
        cigarbot.attach_controller(controller)
    return cigarbot

def main():
    cigarbot = setup_bot()
    cigarbot.run(check_comments=False, check_submissions=False)

if __name__ == '__main__':
    main()
    

