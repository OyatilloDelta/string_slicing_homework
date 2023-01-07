def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    x=s[-n:-1]
    d=s[-1]
    l=x+d
    return l
print(main('alpha1234',2))
