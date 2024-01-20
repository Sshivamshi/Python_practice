#press alt+Z for word wrap
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
print(id(Names(2)))  #'list' object is not callable
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

numbers = [1,2,3,4,5]
sum = 0    # No memory wastage as value is not overwritten beacause INTERNING if there was a bigger value then it would have wasted memory
for num in numbers :
    sum +=num  
print(sum)
  # In Python, integers are immutable objects, meaning their values cannot be changed after creation.
# The operation sum_result += num seems like it modifies the existing integer object, but it actually
# creates a new integer object with the updated value and makes the variable refer to this new object.

# Python optimizes the process for small integers (typically -5 to 256) using "interning."
# Small integers are interned, meaning there is a single object for each distinct small integer value,
# and all variables referring to that value point to the same object in memory.

# Interning helps reduce memory usage and makes integer operations more efficient, as it avoids
# unnecessary creation of new objects for frequently used small integer values.

# Therefore, when using += with small integers, Python may reuse the existing interned object,
# making it appear as if the integer is being modified in place and contributing to efficient memory usage.



a ,b = 10,-10
print(a+b)
print(a-b)
print(a*b)
print(a/b)  #division (leaves quotient)
print(a%b) #modulus (leaves remainder)
c , d = -21 , 10
print(c%d) #-21%10 is 9 because the closest multiple of 10 towards negative infinity is -30 and -30+9 is -21. 
# Remainder is always positive 
print(c/d) # negative quotient : -2.1

#int(print(c/d))  # but the print() function returns None.
# The expression print(c/d) will print the result of the division of c by d,
# but the print() function returns None.
# you're trying to convert None to an integer and will result in a TypeError.

#printing a loop in python for i=0 to i<testcases ; i++
#int(print(c/d))  # but the print() function returns None.
test = int(input()) #input() always return string hence type conversion
for i in range(test): #range(n) sets range from 0 to n-1
    print("hello")


print(int(c/d)) # -2 Type converted to int
e , f = 4 , 1/2   
print(e**f)  #modulus operator :
# e , f = 4 , 1/2   shortway of calculating square root 
# (a)^1/2 mean sqaure root 
#(a)^-1 means reciprocal 
#(a)^-1/2 means square root of reciprocal 

powers = [1/2,-1/2,2,-2]
output =[]
for nums in powers :
    #output[nums]    nums is values inside power not index
    output.append(4**nums)
print(output) #[2.0, 0.5, 16, 0.0625]  


#map() : similar to map() in JS , used to iterate a function over all values in a list 
#map() is a built-in function that applies a given function to all items in an input list (or any other iterable) and returns an iterable (usually a list) of the results.
numbrs = [1,2,3,4,5]
def square(nums):
    return nums*nums
output =[]
# output.append((map( square,numbrs))  using the map function, but you are not converting the result to a list after applying the square function. The map function returns a map object, and you need to convert it to a list
output.append(list(map( square,numbrs)))
print(output)


#concatenate using MAP()
greet = "hey"
names = ["Himmi", "Akii", "Bruce"]
messages =[]
#def message(greet , word): #the function that uses map can take only one argument and return one value 
def message(word):
        return greet + " "+ word
#messages = messages.append(list(map(message , names)))
#messages = messages.append(list(map(message, names))): This line is assigning the result of the append method to the variable messages. However, the append method in Python returns None because it modifies the list in-place and doesn't produce a new list. Therefore, after this line, messages will be set to None.

messages.append(list(map(message , names))) 
messages.extend(map(message , names))
#extend function is similar to : messages = messages + list(map(message , names))
print(messages)   #[['hey Himmi', 'hey Akii', 'hey Bruce'], 'hey Himmi', 'hey Akii', 'hey Bruce'] 
#messages[0] = ['hey Himmi', 'hey Akii', 'hey Bruce'] beacuse list() creates a new empty list and stores all values returned by map 

numbrs = [1,2,3,4,5]
def square(nums):
    return nums*nums
output =[]
# output.append((map( square,numbrs))  using the map function, but you are not converting the result to a list after applying the square function. The map function returns a map object, and you need to convert it to a list
output.append(list(map( square,numbrs)))  
output.extend(map(square, numbrs)) 
print(output) #[[1, 4, 9, 16, 25], 1, 4, 9, 16, 25]   