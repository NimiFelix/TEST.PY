


if 5 > 2:
   print("Five is greater than two")
   #this is a comment
   print("Hello world!")

   x = str(3)
   y = int(3)
   z = float(3)
   print(x,y,z)
   print(type(x))
   print(type(z))
   
   Fruits = ["apple", "banana", "cherry"]
   y, x, z = Fruits
   print(x)
   print(y)
   print(z)

x = "Nimi "
y = "is "
z ="awesome! "
print(x + y + z)

x = str(5)
y = "John"
print(x, y)

#Dynamic typing and casting
a = float(5.6) 
print(type(a))

#strings
b = 45
print(type(b))
p = 4, 5, 6
print(type(p))

#methods
x = "Pepsi"
print(x.upper())
print(x.lower())
print(x.capitalize())
print(x.title())
dir("string")
y = "believe"
print(y.replace('e', 'a'))
z = "1,2,3,4"
print(z.replace('1', '0'))

#slicing and indexing
"""
indexing is the number/numbering of characters in a string(btw the quotes)
foward : its starts from zero (positive)
backward: it starts from -1 (neg)
"""
x = "hello world"
print(x[6], x[4], x[-3])

"""
slicing is basically splitting characters in a string
"""
x = "hello world"
print(x[0:5])
print(x[6:11])
print(x[-4:-1])

##string formatting
f = int(input('Enter first value: '))
s = int(input('Enter second value: '))
k = f + s
t = "The addition of {} and {} equals {}".format(f , s , k)
print(t)
## OR
f = 2
s = 3
k = f + s
t = f"The addition of {f} and {s} equals {k}"
print(t)
## OR
x = [2, 3, (2 + 3)]
t = f"The addition of {x[0]} and {x[1]} equals {x[2]}"
print(t)

##List
"""
enclosed in []
major types of list
pop, _del_, append, _len_, remove 
"""

##Tuples
"""
enclosed in ()
They cannot be manipulated like the list
"""
x = ("Joe", "Tami", 3, 4, 5)
print(type(x))
 
##Dictionary
"""
enclosed in{}
its keys has to be enclosed in ""
it can be manipulated like the list 
"""
y = {"name": "Tio", "num":2, "age":19}