def Xbonacci(sig,n):
    result = sig
    length = len(result)
    while len(result) < n:
        result.append(sum(result[-length:]))
    return result[:n]