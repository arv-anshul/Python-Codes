def reccur(n):
    """ Return the factorial of given number """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n*reccur(n-1)


let = reccur(5)
print(let)
