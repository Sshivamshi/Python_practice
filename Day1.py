
# BUILT-IN DATA TYPES FOR PYTHON

a , b = 1 , -1  #numeric data type
print (a + b)   

d = -5.000 #float data type
#double quotes are the same as single quotes:
c = 3+0j
print(type(c))  #<class 'complex'> output

# Variable names are case-sensitive.
A , B = 2, -2 
print(A+B)
#String in python : 
#A collection of one or more characters put in single, double or triple quotes.
Name = "Himmi"

#Tuple vs list
# When a program is run, data objects in the program are stored in the computer’s memory for processing.
#  While some of these objects can be modified at that memory location, 
# other data objects can’t be modified once they are stored in the memory. 
# The property of whether or not data objects can be modified in the same memory location where they are stored is called mutability.

Names = ["Akii","Himmi", "Bruce"] #list (orderered collection as mutable)
print(id(Names[2]))     #140585041201648
Names[2] = "Maheet"
print( Names , id(Names[2])) #['Akii', 'Himmi', 'Maheet'] 140585040881648 id same before and after hence mutablity 
#Structure also similar to array 
Names2 = ("Akii", "Himmi" , "Bruce")
print(id(Names(2)))
# Names2(2) = "Mohit"  #Error: tuple' object does not support item assignment
 
Print(Names2 , id(Names2(2)))

# Mutable : list , dictionary
# Immutable : numeric , string , tuple  (varible name is given to loaction of memory )

# In Python, everything is an object.(instance of a datatype)
#A variable is a name given to a memory location where a value is stored. 
#  Objects are regions of memory with types and associated operations.
# Examples of objects include numbers, strings, lists, functions, and modules.

# Immutability in Python means that once an object is created, its value cannot be changed.
# Numeric types like integers are immutable, so modifying their value creates a new object.

# Example illustrating immutability with integers:
original_integer = 42  # Creating an integer object with value 42
original_integer = 99  # Modifying the value creates a new integer object with value 99

# The original integer object with value 42 still exists in memory,
# but the variable now references the new object with value 99.

# Immutability offers benefits like predictability 
# but may lead to increased memory consumption,as new objects are created for each modification.

# In situations where memory efficiency is a critical concern, and frequent modifications are needed,
#  mutable data structures like lists or arrays might be more appropriate.
#  However, it's essential to balance these considerations with the design goals and requirements of your specific application. 

