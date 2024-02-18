# INTERNAL WORKING OF PYTHON

# script/program -> byte code (hidden) -> python virtual machine(VM)
# STEP 1 : code is compiled into byte code that is low-level and platform independent (as long as there is a interpreter on system, it can run on any OS- mac or windows machine)
# byte code runs faster than scripts
# the .pyc file is compiled python (also called frozen binaries, that produces .exe files too)

# python creates a system folder to keep up with changes in source files: __pycache__ (underscores refer to internally useful files for python)
# in hello_world.cpython-311.pyc -> .pyc file is visible for imported files (not top level files) to optimize them.

# python virtual machine
#     - software that runs in a loop continuously- be it byte code or python scripts
#     - also called run time engine & python interpreter
# byte code is NOT machine code
#   - byte code refers to python specific interpreter
#   - PVMs: cpython (for default & standard implementation), jython (for Java VM), ironPython (for .NET), stackless, pypy (to specify if you wanna use any other interpreter)

# python manages memory automatically (called garbage collection)
# interpreter takes care of allocating memory for objects & reclaiming when its not in use.

# GLOBAL INTERPRETER LOCK(GIL) in cpython- to ensure that one thread executes bytecode at one time to simplify memory management.



# BUILT-IN DATA TYPES FOR PYTHON 

# In python, data-types are assigned to the numbers & strings in memory instead of the variables holding them.
# Numeric data type:
a , b = 1 , -1 
print (a + b)   
d = -5.000 # float data type
c = 3+0j
print(type(c))  #<class 'complex'> output
# Variable names are case-sensitive.
A , B = 2, -2 
print(A+B)

# String in python : 
# A collection of one or more characters put in single, double or triple quotes.
Name = "Himmi" # Double quotes are the same as single quotes
Name[0] # H Strings are almost treated like arrays but you cannot assign, modify in existing ones as it is immutable
len(Name) # 5 (length of the string)
Name[-1] # i  ( to access the last character in the string)


# MUTABILITY
# When a program is run, data objects ( data/values is stored as object in python) in the program are stored in the computer’s memory for processing.
# While some of these objects can be added, removed, or modified at that memory location (mutable objects), 
# Other data objects can’t be, once they are stored in the memory (immutable objects). 
# The property of whether or not data objects can be added, removed, or modified in the same memory location where they are stored is called mutability.
# Operations on immutable objects create new objects rather than modifying existing ones.
# Mutable : list, dictionary, sets
# Immutable : numeric (int, float), string, tuple (a variable name is given to location of memory) 

# Tuple V/S List
# If you need to change the items of collection- then list is preferred as it is mutable, if items can remain unchanged, tuple is used.
# As lists are mutable they consume more memory and tuple provides better performance in those certain situations.
# both are iterable (to run loops), allow indexing and slicing and support different data-types

Names = ["Akii","Himmi", "Bruce"] #list (ordered collection as mutable)
print(id(Names[2]))     #140585041201648
Names[2] = "Maheet"
print( Names , id(Names[2])) #['Akii', 'Himmi', 'Maheet'] 140585040881648 id same before and after so it is mutable 
# Structure is similar to array 
Names2 = ("Akii", "Himmi" , "Bruce")
print(id(Names(2)))  #'list' object is not callable
# Names2(2) = "Mohit"  #Error: 'tuple' object does not support item assignment
 
Print(Names2 , id(Names2(2)))

# In Python, everything and every data/ value of variable is an object. (instance of a datatype) 
# Why? (to stay committed to python being a OOP lang) beacause if we treat data as object we can use METHODS (function inside classes, used by objects) with them like .sort() , .append() , .extend() )
# A variable is a name given to a memory location where a value is stored. 
# Objects are regions of memory with types and associated operations.
# Examples of objects include numbers, strings, lists, functions, and modules.

# Immutability in Python means that once an object is created, its value cannot be changed.
# Numeric types like integers are immutable, so modifying their value creates a new object.

# Example illustrating immutability with integers:
original_integer = 42  # Creating an integer object with value 42
original_integer = 99  # Modifying the value creates a new integer object with value 99

# The original integer object with value 42 still exists in memory,
# but the variable now references the new object with value 99.
# since python has automated garbage allocation, the objects that are no longer in use get deleted automatically after a while.

# Immutability offers benefits like predictability 
# but may lead to increased memory consumption, as new objects are created for each modification.

# In situations where memory efficiency is a critical concern, and frequent modifications are needed,
# mutable data structures like lists or arrays might be more appropriate.
# However, it's essential to balance these considerations with the design goals and requirements of your specific application. 

numbers = [1,2,3,4,5]
sum = 0    # No memory wastage as value is not overwritten beacause INTERNING if there was a bigger value then it would have wasted memory
for num in numbers :
    sum +=num  
print(sum)

# In Python, integers are immutable objects, meaning their values cannot be changed after creation.
# The operation sum_result += num seems like it modifies the existing integer object, but it actually
# creates a new integer object with the updated value and makes the variable refer to this new object.

# Python optimizes the process for small integers (typically -5 to 256) using "interning."
# Interning: refers to the optimization technique of storing only one copy of each unique immutable object to save memory and improve performance.
# Small integers are interned, meaning there is a single object for each distinct small integer value,
# and all variables referring to that value point to the same object in memory.

# Interning helps reduce memory usage and makes integer operations more efficient, as it avoids
# unnecessary creation of new objects for frequently used small integer values.

# Therefore, when using += with small integers, Python may reuse the existing interned object,
# making it appear as if the integer is being modified in place and contributing to efficient memory usage.



a, b = 10,-10
print(a+b)
print(a-b)
print(a*b)
print(a/b)  #division (leaves quotient)
print(a%b) #modulus (leaves remainder)
c , d = -21 , 10
print(c%d) #-21%10 is 9 because the closest multiple of 10 towards negative infinity is -30 and -30+9 is -21. 
# Remainder is always positive 
print(c/d) # negative quotient : -2.1

# int(print(c/d))  # but the print() function returns None.
# The expression print(c/d) will print the result of the division of c by d,
# but the print() function returns None.
# you're trying to convert None to an integer and will result in a TypeError.

# printing a loop in python for i=0 to i<testcases ; i++

test = int(input()) #input() always return string hence type conversion
for i in range(test): #range(n) sets range from 0 to n-1
    print("hello")


print(int(c/d)) # -2 Type converted to int
e , f = 4 , 1/2   
print(e**f)  
# modulus operator :
# e, f = 4 , 1/2   shortway of calculating square root 
# (a)^1/2 mean sqaure root 
# (a)^-1 means reciprocal 
# (a)^-1/2 means square root of reciprocal 

powers = [1/2,-1/2,2,-2]
output =[]
for nums in powers :
    #output[nums]    nums is values inside power not index
    output.append(4**nums)
print(output) #[2.0, 0.5, 16, 0.0625]  


# MAP FUNCTION map() IN PYTHON: similar to map() in JS , used to iterate a function over all values in a list 
# map() is a built-in function that applies a given function to all items in an input list (or any other iterable) and returns an iterable (usually a list) of the results.
numbers = [1,2,3,4,5]
def square(nums):
    return nums*nums
output =[]
# output.append((map( square,numbrs))  
output.append(list(map( square,numbrs))) 
print(output[0]) #[1, 4, 9, 16, 25] as list() was made to store all map objects and that list got appended to output list
# append is generally good when working with for loops 
# The append() method is often used in conjunction with loops, especially for loops, when you want to build up a list by adding elements iteratively. When you are looping through a sequence or performing some operation multiple times, you can use append() to add elements to the end of a list during each iteration.

# concatenation using MAP()
greet = "hey"
names = ["Himmi", "Akii", "Bruce"]
messages =[]
# def message(greet, word): #the function that uses map can take only one argument and return one value 
def message(word):
        return greet + " "+ word
# messages = messages.append(list(map(message , names)))
# messages = messages.append(list(map(message, names))): This line is assigning the result of the append method to the variable messages. However, the append method in Python returns None because it modifies the list in-place and doesn't produce a new list. Therefore, after this line, messages will be set to None.

messages.append(list(map(message , names))) 
messages.extend(map(message , names))
# extend function is similar to : messages = messages + list(map(message , names))
print(messages)   #[['hey Himmi', 'hey Akii', 'hey Bruce'], 'hey Himmi', 'hey Akii', 'hey Bruce'] 
# messages[0] = ['hey Himmi', 'hey Akii', 'hey Bruce'] beacuse list() creates a new empty list and stores all values returned by map 

numbers = [1,2,3,4,5]
def square(nums):
    return nums*nums
output =[]
# output.append((map( square,numbrs)) 
# using the map function, but you are not converting the result to a list after applying the square function. The map function returns a map object, and you need to convert it to a list
# Map Object:

# Lazily evaluates the values.
# Consumes less memory as it generates values on demand.
# Does not support random access (you can't access elements by index).
# Once iterated, it's over, it cannot be reused (you need to create a new map object).

# List:

# Stores all values in memory.
# Supports random access (you can access elements by index).
# Can be iterated over multiple times.
output.append(list(map( square,numbers)))  
output.extend(map(square, numbers)) 
print(output) #[[1, 4, 9, 16, 25], 1, 4, 9, 16, 25]  
numbers = [1,2,3,4,5]
def square(nums):
    return nums*nums
output =[]
# output.append((map( square,numbers))  
for i in range(5):
    output.append((map( square,numbers)))
print(output)
#[<map object at 0x7ffbd7ecb970>, <map object at 0x7ffbd7d7cd60>, <map object at 0x7ffbd7d7ccd0>, <map object at 0x7ffbd7d7cc40>, <map object at 0x7ffbd7d7cbb0>]

