


"""
c = int(input("Enter value (mins): "))
x = int(input('Enter value (secs): '))
f = (c / 60) + (x / 360)
k = f"{f} hrs"
print(k)
"""

"""
a = int(input("Enter value(a): "))
b = int(input("Enter value(b): "))
c = int(input("Enter value(c): "))
k = (-b + sqrt(b** - (4*a*c))) / (2 * a)
q = (-b - sqrt(b** - (4*a*c))) / (2 * a)
print(k)
print(q)
"""

def add(x,y):
    z = x + y
    return print(z)

a = int(input("First value"))
b =  int(input("second value"))
add(a,b)

#Convertors
def deg(c):
    f = (9/5)*c +32
    return print(f)

c = int(input("write the temperature in celsius"))
deg(c)

def hrs(m, s):
    h = (m / 60) + (s / 3600)
    return print(h)

m = int(input("write in min: "))
s = int(input("write in sec: "))
hrs(m , s)

##modifying a function
def div(a,b):
    if (b == 0):
        return print("maths error")
    else:
        k = a / b
        return print(k)

a = int(input("input first no: "))
b = int(input("input second no: "))
div(a,b)

x = 400
print(isinstance(x, str))
