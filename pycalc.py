import sys

def main(args):
    x = int(args[0])
    y = int(args[2])
    opp = args[1]
    print(x,opp,y)
    if opp == "+":
        print(x+y)
    elif opp == "-":
        print(x-y)
    elif opp == "/":
        print(x/y)
    else:
        a=0
        for _ in range(y):
            a=x+a
            print(a)


main([2,"*",4])

