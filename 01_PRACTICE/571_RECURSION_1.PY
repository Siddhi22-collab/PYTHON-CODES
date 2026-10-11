def foo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 3
    return n+foo(n-1)+foo(n-2)
foo(6)