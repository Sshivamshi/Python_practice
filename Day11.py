# Method: capitalize()
# Definition: Returns a copy of the string with its first character capitalized and the rest lowercased.
# Syntax: string.capitalize()
# Argument Type: None
# Return Type: str

# Method: upper()
# Definition: Returns a copy of the string with all alphabetic characters converted to uppercase.
# Syntax: string.upper()
# Argument Type: None
# Return Type: str

# Method: lower()
# Definition: Returns a copy of the string with all alphabetic characters converted to lowercase.
# Syntax: string.lower()
# Argument Type: None
# Return Type: str

# Method: title()
# Definition: Returns a copy of the string with the first character of each word capitalized and the rest lowercased.
# Syntax: string.title()
# Argument Type: None
# Return Type: str

# Method: swapcase()
# Definition: Returns a copy of the string with uppercase characters converted to lowercase and vice versa.
# Syntax: string.swapcase()
# Argument Type: None
# Return Type: str

# Method: strip([chars])
# Definition: Returns a copy of the string with leading and trailing characters specified in the argument removed.
# Syntax: string.strip([chars])
# Argument Type: str (optional)
# Return Type: str

# Method: replace(old, new[, count])
# Definition: Returns a copy of the string with occurrences of the specified 'old' substring replaced by the 'new' substring.
# Syntax: string.replace(old, new[, count])
# Argument Type: str, str, int (optional)
# Return Type: str

# Method: find(sub[, start[, end]])
# Definition: Returns the lowest index in the string where the substring 'sub' is found. Returns -1 if not found.
# Syntax: string.find(sub[, start[, end]])
# Argument Type: str, int (optional), int (optional)
# Return Type: int

# Method: count(sub[, start[, end]])
# Definition: Returns the number of occurrences of the substring 'sub' in the string.
# Syntax: string.count(sub[, start[, end]])
# Argument Type: str, int (optional), int (optional)
# Return Type: int

# Method: split([sep[, maxsplit]])
# Definition: Returns a list of substrings separated by the specified 'sep' (default is whitespace).
# Syntax: string.split([sep[, maxsplit]])
# Argument Type: str (optional), int (optional)
# Return Type: list of str

# Method: join(iterable)
# Definition: Concatenates the elements of an iterable (e.g., a list) with the string as a separator.
# Syntax: string.join(iterable)
# Argument Type: iterable
# Return Type: str


message = '"hello"'
print(message)     # OUTPUT : "hello"   :use of single quote to print ""

# string slicing operation 
print(message[0])   
print(message[-1])
# syntax : message[from index : upto position]
print(message[1:6]) 
print(message[1:2])

# string methods : .methods()

#.upper() : Returns the uppercased version of string 
print(message.upper())

#.find('substring') /   : Takes substring as argument and returns the index of the first occurrence of the searched substring and -1 if searched substring isn't found
string = 'word Find the word from here'
print(string.find('word'))
print(string.find('word2'))
print(string.find('word' ,1)) 
print(string.find('word' ,1 , 15)) 

# string.replace(old, new, count)  : Returns a copy of the string where occurrences of a substring are replaced with another substring. 
string2 = 'word Find the word from here'
string2.replace('word' , 'word2')
print(string2)  # Returns same string (string2) :  as .replace() method returns a copy of modified string IT DOESN'T modify the original string
# print(string.replace('WORD' , 'replaced'))   # .replace()'s  arguments are case sensitive
print(string.replace('word' , 'replaced'))
print(string.replace('word' , 'replaced' , 1)) # count (optional): The maximum number of occurrences to replace. If not specified, all occurrences will be replaced.


# python fstring ( replacement of .format method)
lists = ['Himmi' , 'Akii' , 'Bruce' , 'Mohit' ]
for i in range(len(lists)):
    print(f"Hello {lists[i]} , u good ?")
'''
OUTPUT:
Hello Himmi , u good ?
Hello Akii , u good ?
Hello Bruce , u good ?
Hello Mohit , u good ?
'''