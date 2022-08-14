# Interger and floating point data type.
print(273)
print(52.273)
print(type(273))
print(type(52.273))
print(type(0))
print(type(0.))

#Numerical operator.
print("5 + 7 = " , 5 + 7)
print("5 - 7 = " , 5 - 7)
print("5 * 7 = " , 5 * 7)
print("5 / 7 = " , 5 / 7)
#Floor division.(divide operator and eliminate floating remainder.)
print("3 / 2 = " , 3/2 , type(3/2))
print("3 // 2 = " , 3//2 , type(3//2))
#Modulo operator.
print("5 % 2 = ", 5%2 ,type(5%2))
#Power operator.
print("2**1 = " , 2**1)
print("2**2 = " , 2**2)
print("2**3 = " , 2**3)
print("2**4 = " , 2**4)

#Priority between operators.
#This is too confused and have trouble understanding others.
#Please enclose with parenthesis.
print(2+2-2*2/2*2)
print(2-2+2/2*2+2)

print(2+2-(2*2/2*2))
print(2-2+(2/2*2)+2)


#TypeError in python
string = "string_type"
number = 273
# TypeError occured.
#print(string + number)

#String operator priority
print("Nice" + " to meet you" * 2)
print