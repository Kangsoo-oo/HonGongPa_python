# Data type
print(type("Hello"))
print(type(273))

#String with single quotation mark.
print('single quotation - Hello')
#String with double quotation mark.
print("double quotation - Hello")

#When wanna put the single quotation mark into the string
#Enclose string as double quotation mark.
print("She said 'hello'")
#When wanna put the double quotation mark into the string
#Enclose string as single quotation mark.
print('He said "No"')
#Can handle this confusion with escape character.
# \" , \' is not handled as string start or end.
print('She said \'Hello\' and he said \"No\" ')

# \n is the newline.
print('She was beautiful.\nHe was hansome.')
# \t is the tab.
print("Hello\tHello")

print('--------------------------')
print("Age\tName\tLoc")
print("32\tcharles\tseoul")
print("33\tJason\tincheon")
print("34\tWatt\twonju")
print('--------------------------')

print("\\ \\ \\ \\")

# Print function can multiple line supported with '''
print('''
She was beautiful 
and tired becuase of work.
He was hansome
They are so tired.
and Wanna go home
''')

#String additional operator(+)
print("Hello" + "world")
print("Hello world" + "!")
#print("Error + operator to int" + 1)

#String multiply operator(*)
print("Hello" * 3)
print(3 * "Hello")

# Indexing
print("Search \'hello\' forward start with 0")
print("Hello"[0])
print("Hello"[1])
print("Hello"[2])
print("Hello"[3])
print("Hello"[4])
print("Search \'hello\' backward start with -1")
print("Hello"[-5])
print("Hello"[-4])
print("Hello"[-3])
print("Hello"[-2])
print("Hello"[-1])

#Slicing [start : end] ,$end is not licluded $end index value.
#When omit the start or end, be substitued by 0 and  count of string at each
print("Hello"[1:4])
print("Hello"[0:2])
print("Hello"[1:3])
print("Hello"[2:4])
print("Hello"[1:])
print("Hello"[:3])

# Count length of string.
print(len("Hello"))