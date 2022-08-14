#Variable declaration with assign value
# variable = ${be assigned value}
pi = 3.14159265
print(pi)
print(pi + 2 , type(pi + 2))
print(pi - 2 , type(pi - 2))
print(pi / 2 , type(pi / 2))
print(pi % 2 , type(pi % 2))
print(pi * pi , type(pi * pi))
#String with floating variable cannot be executed.
#print(pi + "Hello")

#Calculate circumference and area of circle.
r = 10
print("Pi = " , pi)
print("radius = " ,r)
print("Circumference of circle = ", 2 * pi * r)
print("Area of circle = " , pi * r * r)

#Assigne operators.
number = 100
print("number = " ,number)
number += 10
print("after  += 10" , number)
number +=20
print("after  += 20" , number)
number +=30
print("after  += 30" , number)

string = "Hello"
print("Hello = " , string)
string += "!"
print("after +=! " , string)
string += "!"
print("after +=! " , string)

#User input.
input_value = "273"#input("Input  >>  ")
input_int = int(input_value)
input_value2 = "52"#input("Input2  >>  ")
input_int2 = int(input_value2)
print("input_value + input_value2 = " , input_value + input_value2)
print("intpu_int + input_int2 = " , input_int + input_int2)

#Interger and floating point casting.
output_a = int("52")
output_b = float("52.273")
print(type(output_a) , output_a)
print(type(output_b) , output_b)

input_a = 273.#float(input("First operand >>> "))
input_b = 52.#float(input("Second operand >>> "))

print("Addition result = "          , input_a + input_b)
print("Substraction result = "      , input_a - input_b)
print("Multiplication result = "    , input_a * input_b)
print("Division result = "          , input_a / input_b)

#ValueError 
#When try to cast us-convertable value to int or float.
#int("hello")
#float("hello")

#"Floating point string to int"
#int("52.273")

#To String function.
output_a = str(52)
output_b = str(52.273)
print(type(output_a) , output_a)
print(type(output_b) , output_b)