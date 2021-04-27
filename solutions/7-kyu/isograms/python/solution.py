def is_isogram(string):
    return True if len([i.lower() for i in string]) == len(set([i.lower() for i in string])) else False