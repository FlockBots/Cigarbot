from fuzzywuzzy import fuzz

def match(a, b):
    """ Returns the percentage that matches """
    return fuzz.partial_ratio(a.lower(), b.lower())