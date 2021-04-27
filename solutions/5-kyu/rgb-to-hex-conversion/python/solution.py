def rgb(r, g, b):
    def min_max(x): 
        return max(0, min(x, 255))
    return f"{min_max(r):02x}{min_max(g):02x}{min_max(b):02x}".upper()