def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    d=s[-4:-1]
    h=s[-1]
    e=d+h
    return e
print(main('123456789absdf'))