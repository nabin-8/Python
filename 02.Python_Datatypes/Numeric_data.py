
'''
Numeric data Types

int
float
bool
complex
'''

# integer type (int)
a=10
d=10321531556165151321321650
b=-10
print(a)
print(type(a))
print(b)
print(type(b))
print(d)

# check how much it takes
print(d.__sizeof__())
print(a.__sizeof__())


# Floating Point
a=13.25
print(a)
print(type(a))
b=-17.66
c=12.59
print(c)
c=1259E-2
print(c)
c=0.1259E2
print(c)
print(type(c))

# Boolean
x=True
print(x)
print(type(x))
y=False
print(y)
print(type(y))


# Complex Numbers
# real and imaginary number

x=3+5j
print(type(x))
b=complex(12,9)
print(b)

a=1.22+3.55j

print(a.real)
print(a.imag)