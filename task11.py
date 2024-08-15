'''
Write a python function which infinitely prints natural numbers in a single line.
Raise the StopIteration exception after displaying first 20 numnbers to exit from the program.

'''

def printNumbers():
    i=0
    while True:
        if i == 20:
            raise StopIteration("Program is now stopped")
        print(i,end='')
        i += 1
try:
    printNumbers()
except StopIteration as e:
    print(e)