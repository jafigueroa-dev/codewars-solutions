def pig_it(text):
    t_list = text.split()
    result = ""
    for word in t_list:
        if word.isalnum() is True:
            result = result + word[1:] + word[0] + "ay" + " "
        else:
            result = result + word
    return result.rstrip()
        