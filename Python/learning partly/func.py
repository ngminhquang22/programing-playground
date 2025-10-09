#def a function
#default arguments
#keywords
#arbitrary

def add(*args):
    total = 0;
    for arg in args:
        total += arg
    return total

print(add(8,22,3,6,8,9))