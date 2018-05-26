def printall(*args):
    print(args)

def sumall(*args):
    return sum(args)


if __name__ == '__main__':
    printall(1, 2.0, '3')
    print(sumall(1,2,3,4,5))