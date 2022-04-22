#we want to print who's this.

print("who\'s this?")

"""
This actually happened because of the backslash (‘\’) before any character tells
the interpreter that this combination is an escape sequence in python, 
which removes the backslash from the string and will put the quote inside the string."""

#\n newine
print("Khammam\nTelangana") #new line
print('Interview\tBit') #tab space between the words or characters using “\t”.
print('Interview \bBit') #  remove the space between the words.
print("\x48\x45\x4C\x4C\x4F\x20\x57\x4F\x52\x4C\x44") #Hexa value we can use “\xhh”, where hh is the unique Hexa value of the alphabets. output Hello World
print("\110\105\114\114\117\040\127\117\122\114\104") # octa Value out put Hello world
s = ['Hello','\x50','to','\x44','World']
print(s) #  Remove all escape sequence from a list  ['Hello', 'P', 'to', 'D', 'World']
print(r"Hello\nWorld") # Python escape sequence ignore
#Raw string method We can use the concept of raw string, i.e., adding r or R before the string, which will preserve the escape sequences as literals.
print("C:\Interview Bit\nScaler\aAcademy")
print(r"C:\Users\Dell\OneDrive\Desktop") 
#Python escape sequence remove To remove all the characters from the left and right of an argument string, we will use the string.strip() function.
s = '\r\r\b InterviewBit \r\r\n  '
s.strip
print(s)
#Escape Sequence Interpretation
# A string with a Valid escape sequence
print("Interview\tBit")

# A string with a Invalid escape sequence
print("Scaler\cAcademy")
#Preventing Escape Sequence Interpretation --In first case "\t" was considered as tab space, but in second one "\t" was printed as normal literal
print("Interview \t Bit")
print("Interview \\t Bit")
#We can use the concept of raw string, i.e., adding r or R before the string, which will preserve the escape sequences as literals.
print("C:\Interview Bit\nScaler\aAcademy")
print(r"C:\Users\Dell\OneDrive\Desktop")
