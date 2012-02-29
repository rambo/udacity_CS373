#Write a function that takes the number of 
#coconuts, n, as an argument and returns the
#number of coconuts after one is given to
#the monkey and one fifth are taken away.


def f(n):
    n = n - 1
    fifth = n/5
    n = n - fifth
    return n

print f(96.)
