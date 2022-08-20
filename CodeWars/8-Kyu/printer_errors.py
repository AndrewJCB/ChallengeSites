def printer_error(s):
    # your code
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))
