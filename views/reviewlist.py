def reviewlist(author, reviews):
    if not reviews:
        return 'Sorry buddy, I cannot find any of your reviews in /r/CigarReview\n\n'
    string = "{}'s latest reviews:\n\n".format(author)
    string += _create_list(reviews)
    string += '\n\n'
    return string

def searchresults(author, reviews, keyword):
    if not reviews:
        return 'Sorry {}, I cannot find any of your `{}` reviews.\n\n'.format(author, keyword)
    string = "{}'s latest `{}` reviews:\n\n".format(author, keyword)
    string += _create_list(reviews)
    string += '\n\n'
    return string

def anyresults(reviews, keyword):
    string = "Most recent `{}` reviews in /r/CigarReview\n\n".format(keyword)
    string += _create_any_list(reviews)
    string += '\n\n'
    return string

def _create_any_list(reviews):
    string = ''
    for review in reviews:
        string += '* [{title}]({url}) (*{author}*)\n'.format(
            author  = review.author,
            profile = 'https://reddit.com/u/' + review.author,
            title   = review.title,
            url     = review.url
        )
    return string

def _create_list(reviews):
    string = ''
    for review in reviews:
        string += '* [{title}]({url})\n'.format(
            title = review.title,
            url   = review.url
        )
    return string
