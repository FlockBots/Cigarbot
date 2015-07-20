def reviewlist(author, reviews):
    string = "{}'s latest reviews:\n\n".format(author)
    for review in reviews:
        string += '* [{title}]({url})'.format(
            title = review.title,
            url   = review.url
        )
    string += '\n\n'
    return string