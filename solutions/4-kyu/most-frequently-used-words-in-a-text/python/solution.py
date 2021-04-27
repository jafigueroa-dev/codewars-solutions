from collections import Counter
import re

def top_3_words(t):
    return [i for i, j in Counter(re.sub(r"[^a-zA-Z' ]+", ' ', t).lower().split()).most_common(3) if i != len(i) * "'"]