#String foramtting function .format()
print("{}".format(10))
print("{}  {}".format(10,20))
print("{} {} {} {} {}".format(101,202,303,404,505))

string_a = "{}".format(10)
print(string_a , type(string_a))
format_a = "{}  dollors".format(10)
format_b = "Hard study with {} salary".format(4000)
format_c = "{} , {} , {} ".format(3000,4000,5000)
format_d = "{} {} {}".format(1, "String" , True)
print(format_a)
print(format_b)
print(format_c)
print(format_d)

#When the count of format argument greater than brace .
#Index error not occured.
print("{} ,{} ".format(1,2,3,4,5))
#When the count of format argurment less than brace.
#IndexError
#print("{} {} {} {} {}".format(1,2,3,4))

#Other usage of format function.
#explicitly use interger at argument.
#And set string width.
output_a = "{:d}".format(52)
output_b = "{:5d}".format(25)
output_c = "{:10d}".format(32)
print(output_a)
print(output_b)
print(output_c)

#put the '0' into the white space area.
output_a = "{:05d}".format(52)
output_b = "{:05d}".format(-25)
print(output_a)
print(output_b)

# print signedness
print("{:+d}".format(52))
print("{:+d}".format(-52))
# reserved area for signedness
print("{: d}".format(52))
print("{: d}".format(-52))

print("{:+5d}".format(52))
print("{:+5d}".format(-52))
print("{:=+5d}".format(52))
print("{:=+5d}".format(-52))
print("{:+05d}".format(52))
print("{:+05d}".format(-52))

'''Floating point print'''
print("{:f}".format(52.273))
print("{:15f}".format(52.273))
print("{:+15f}".format(52.273))
print("{:+015f}".format(52.273))

#Set significant number width
print("{:+15.3f}".format(52.273))
print("{:+15.2f}".format(52.273))
print("{:+15.1f}".format(52.273))

#Delete useless number
number = 52.0
string_number = "{:g}".format(number)
print(number , type(number) , string_number , type(string_number))

#Change upper and lower case.

a = "Hello Python Programming ...!"
print(a.upper())
print(a.lower())

input_a = """
            Hello .   
We will study string data type.
"""

print(input_a)
print(input_a.strip())
