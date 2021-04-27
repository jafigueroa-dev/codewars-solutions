import math
from operator import itemgetter

def order_weight(strng):
    new_weights = []
    weights = list(map(int, strng.split()))
    for value in weights:
        key_pair = {}
        cal_attribute = [(value//(10**i))%10 for i in range(math.ceil(math.log(value, 10))-1, -1, -1)]
        key_pair['weight'] = str(value)
        key_pair['attribute'] = sum(cal_attribute)
        new_weights.append(key_pair)
    result = sorted(new_weights, key=itemgetter('attribute', 'weight'))
    return " ".join([d['weight'] for d in result])