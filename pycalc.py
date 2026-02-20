import sys

def main(args):
    x = int(args[0])
    y = int(args[2])
    opp = args[1]
    if opp == "+":
        print(x+y)
    elif opp == "-":
        print(x-y)
    elif opp == "/":
        print(x/y)
    else:
        print(x*y)
    print(x,opp,y)


main([1,"+",2])

