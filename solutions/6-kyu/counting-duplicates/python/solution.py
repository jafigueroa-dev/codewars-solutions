def duplicate_count(t):
    return len([i for i in [t.lower().count(i) for i in set(t.lower())] if i > 1])