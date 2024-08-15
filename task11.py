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


'''
Write a program that validate name and age as entered by the user to determine whether the person can cast vote or not. To handle the age, 
create InvalidAge exception and for name, create InvalidName exception. The name will be invalid when the string will be empty or name has only one word.
'''
class InvalidAge(Exception):
   def __init__(self,message):
       print(message)


class InvalidName(Exception):
    def __init__(self,message):
        print(message)

        

def castVote(name,age):
    if age < 18:
        raise InvalidAge("Age is Invalid to cast Vote")
    if ((' ' not in name)  or (len(name) == 0)):
        raise InvalidName("Name is Invalid")
    else:
        print("able to cast vote")

try:
    castVote("akshay",19)
except InvalidAge as e:
    pass

except InvalidName as e:
    pass