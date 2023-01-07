def main(s,n):
    """
    The s string variable is given. return all characters except n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    c=s[-1] 
    x=s[n:-1]
    g=x+c
    return g
print(main('12344',2))