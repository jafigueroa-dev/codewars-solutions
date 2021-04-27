def solve_runes(runes):
    final = -1
    nums = [ int(x) for x in [x for x in runes] if x.isdigit() ]
    missing_nums = sorted(set(range(0, 10)) - set(nums))
    expression_check = runes.split("=")
    rem_zero_list = runes.replace("*", "#").replace("+", "#").replace("-", "#").replace("=", "#").split("#")
    for item in rem_zero_list:
        if item.startswith("?") or item.startswith("??"):
            if item is "?":
                continue
            if item is "??":
                continue
            else:
                missing_nums = [ x for x in missing_nums if x != 0 ]
    for x in missing_nums:
        if int(eval(expression_check[0].replace("?", str(x)))) == int(expression_check[1].replace("?", str(x))):
            final = x
            break
    return final