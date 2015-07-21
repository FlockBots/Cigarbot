from flockbot import Bot
from flockbot import Callback
from controllers import ListReviewsController
from config import credentials
import routes

def setup_bot():
    cigarbot = Bot(
        databasefile='storage/bot.db', 
        configfile='storage/log/bot.log'
    )
    cigarbot.config.subreddits = ['flockbots']
    cigarbot.login(
        'Review Lister for /r/CigarReview',
        credentials.oauth_info,
        credentials.refresh_token
    )

    routes.register(cigarbot)
    return cigarbot

def main():
    cigarbot = setup_bot()
    cigarbot.run(check_comments=False, check_submissions=False)

if __name__ == '__main__':
    main()
    

