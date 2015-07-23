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

def _create_list(review):
    string = ''
    for review in reviews:
        string += '* [{title}]({url})'.format(
            title = review.title,
            url   = review.url
        )
    return string
