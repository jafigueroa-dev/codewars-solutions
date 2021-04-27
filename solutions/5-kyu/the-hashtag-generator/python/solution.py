def generate_hashtag(s):
    return False if len(''.join(s)) >= 140 or len(''.join(s)) == 0 else '#' + ''.join(i.capitalize() for i in s.split())