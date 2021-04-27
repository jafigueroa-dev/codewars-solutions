def sort_array(arr):
    sorted_odds = sorted(i for i in arr if i % 2 != 0)
    evens = [i if i % 2 == 0 else -1 for i in arr]
    return [i if i != -1 else sorted_odds.pop(0) for i in evens]