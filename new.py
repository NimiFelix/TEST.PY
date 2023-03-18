##operators in python
"""
1. arithmetic operators
2. assignment operators
3. comparison operators
4. logical
5. identity   (is, is not)
6. membership  (in, not in)
7. bitwise
"""


fruits = ["apple", "banana"]
if "apple" in fruits:
    print("yes, apple is a fruit")

x = "upper"
print(x.upper())

a = "Hello, World!"
print(a.split(","))

a = str(input("Name"))
b = int(input("age"))
txt = "My name is {}, and i'm {}"
print(txt.format(a, b))

y = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {}\nfor {} dollars"
print(myorder.format(y, itemno, price))

txt = "We are the so called \"vikings\" from the north"
print(txt)

txt = "i want to sleep"
print(txt.center(4))

