#single line string
a = "It's me Zobaer Ahmed"
b = "My YouTube channel name is: Mr. ZoZo Programmer"
print(a)
print(b)

#Multiline strings. For this we need three quotes """
c= """Hi It's me Zobaer.
I am pursuing CSE from
American International Univeristy-Bangladesh"""
print(c)

#Basically strings are represented by an array.
Array = "Hello World!"
print(Array[0])
print(Array[6])

#Looping through a strings
for x in "Zobaer":
    print(x)

#Find a lenght of string. using len keyword
FindLenght = "S. S. Zobaer Ahmed"
print(len(FindLenght))

#Find a word from a santences using keyword in
txt = "Python is a slow language compare to C/C++, C#, Java or any other language"
print("C++" in txt)

#we can create this code professional using if else condition
if "C++" in txt:
    print("Yes, C++ is present")
else:
    print("No, C++ is not present here")

#Check if not find this word into the string using "not in" keyword
if "Javascript" not in txt:
    print("Yes, Javascript is not present")
else:
    print("No, Javascript is present")

#Slice
Text = "Zobaer Ahmed"
print(Text[7:])
print(Text[:6])
print(Text[-5:9])

#Upper Case
Name = "Zobaer Ahmed"
print(Name.upper())

#Lower Case
email = "AhmedSSZobaer@GMAIL.COM"
print(email.lower())

#Remove WhiteSpaces
Greetings = " Hello everyone "
print(Greetings.strip())

#Replace strings
name = "Jobaer Ahmed"
print(name.replace("J", "Z"))

#Split Strings
print(name.split())

#Concatenate Strings
str1 = "Hello"
str2 = "Zobaer"
fullStr = str1+" "+str2
print(fullStr)

#F-Strings
#It's like interpolation of C# where we used '$'. but in python we use 'f'
age = 20
print(f"I am {age} years old")

def capitalize():
    Abs = "ggez"
    return Abs
