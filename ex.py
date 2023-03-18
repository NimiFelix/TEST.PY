"""
a = str(input("Name: "))
b = int(input("age: "))
txt = "My name is {}, and i'm {}"
print(txt.format(a, b))


def comp(a , b):
    if b > a:
      txt = "{} is greater than {}"
      return print(txt.format(b,a))

    else:
        txt = "{} is greater than {}"
        return print(txt.format(a, b))

a = input("Enter first value: ")
b = input("enter second value: ")
comp(a,b)
"""

## to check for more info on a function dir()

def chngme(mylist):
    mylist = [10, 20, 30]
    mylist[0] = input()