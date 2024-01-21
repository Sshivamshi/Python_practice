t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    a.sort()
    size = len(a)
    print(a,size)


# https://www.codechef.com/practice/course/arrays-python/PPYAR01/problems/LARGESECOND

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    a.sort()
    size = len(a)
    
    if a[size-1] != a[size-2]:
        print(a[size-1] + a[size-2])
    else:
        for num in reversed(a):
            if a[size-1] != num:
                print(a[size-1] + num)
                break

# https://www.codechef.com/practice/course/arrays-python/PPYAR01/problems/CS2023_STK

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    
    count = 0 #initilization of count outide loop
    streak = 0
    for nums in a:
        if nums == 0:
            count = 0 #assigning count = 0 if a num is 0 , count can be called current or temporary streak here 
            continue #to skip iteration for this value of num after setting current count to 0
        elif nums > 0 :
                count += 1
        streak = max(streak,count)   #update streak if current count > streak
        
    count1 =  0 
    streak1 = 0
    for nums1 in b:
        if nums1 == 0:
            count1 = 0  #count reset
            continue #to skip iteration for this value of num
        elif nums1 > 0 :
            # count1++wrong
            count1 += 1  # Use += for incrementing count
        streak1 = max(streak1,count1)  
        
    if streak > streak1 :
        print("Om")
    elif streak < streak1:
        print("Addy")
    else:
        print("Draw")


# INT() , lIST() , STRING() TYPE CONVERSION  IN DETAIL


t = input("enter a number ")  #input function takes string argument to print and returns string too 
print(t)  #wil print string too if entered , so to sanitize input or type convert to int
n = int(input("enter a no."))
print(n)
#t = input("enter a number ")
# print(int(t))   to type convert output

#enter a number 
# hello
# hello
# enter a no.
# a
# ValueError: invalid literal for int() with base 10: 'a'

#Now, if you run the program and enter non-integer values like "hello" or "a," you will get a ValueError because these values cannot be converted to integers. The error message you provided (ValueError: invalid literal for int() with base 10: 'a') indicates that the program is trying to convert the string 'a' to an integer, which is not possible.


# int()
# Use Case: Converts a value to an integer.
# Argument Type: Any numeric type (int, float, etc.), or a string containing a valid integer.
# Return Type: Integer.

num_str = "42"
num_int = int(num_str)  # Output: 42

# float()
# Use Case: Converts a value to a floating-point number.
# Argument Type: Any numeric type, or a string containing a valid floating-point number.
# Return Type: Float.

num_int = 42
num_float = float(num_int)  # Output: 42.0

# str()
# Use Case: Converts a value to a string.
# Argument Type: Any type.
# Return Type: String.

num_int = 42
num_str = str(num_int)  # Output: '42'

# list()
# Use Case: Converts an iterable (e.g., tuple, string, or another list) to a list.
# Argument Type: Iterable.
# Return Type: List.

my_tuple = (1, 2, 3)
my_list = list(my_tuple)  # Output: [1, 2, 3]

# tuple()
# Use Case: Converts an iterable (e.g., list, string, or another tuple) to a tuple.
# Argument Type: Iterable.
# Return Type: Tuple.

my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Output: (1, 2, 3)

# set()
# Use Case: Converts an iterable (e.g., list, string, or another set) to a set.
# Argument Type: Iterable.
# Return Type: Set.

my_list = [1, 2, 3, 2]
my_set = set(my_list)  # Output: {1, 2, 3}

# bool()
# Use Case: Converts a value to a boolean.
# Argument Type: Any type.
# Return Type: Boolean.

num = 42
is_true = bool(num)  # Output: True

# dict()
# Use Case: Converts an iterable of key-value pairs (e.g., a list of tuples) to a dictionary.
# Argument Type: Iterable.
# Return Type: Dictionary.

key_value_pairs = [('a', 1), ('b', 2)]
my_dict = dict(key_value_pairs)  # Output: {'a': 1, 'b': 2}

# ord() and chr()
# Use Case (ord()): Converts a character to its Unicode code(ASCII) point.
# Use Case (chr()): Converts a Unicode code(ASCII) point to a character.
# Argument Type (ord()): Character (string of length 1).
# Argument Type (chr()): Integer.
# Return Type (ord()): Integer.
# Return Type (chr()): Character.

char = 'A'
unicode_code_point = ord(char)  # Output: 65

code_point = 65
character = chr(code_point)  # Output: 'A'


# input().split(): split() is a METHOD used if we want input on single line ,
#  it separates/splits the input string (input() returns inputed string to split() method)  to int,float or string separated by space separated by , better than using input() 5 times with for loop 

# Function:

# A function in Python is a block of code that performs a specific task and can be called by its name.
# Functions can take input parameters (arguments), perform operations, and return a result.
# Functions can be defined using the def keyword, and they are not tied to any specific object or class.

def add_numbers(a, b):
     # This function takes two parameters, adds them, and returns the result
    return a + b
# Calling the function with arguments 3 and 5
result = add_numbers(3, 5)
# Output: 8
print(result)

# Method:

# A method in Python is a function that is associated with an object and is called on that object.
# Methods are called on objects, and they operate on the data within the object. They donot take arguments
# Methods are accessed using the dot notation: object.method().
# Many methods are built-in for various data types (e.g., strings, lists, dictionaries),
# and custom classes can define their own methods.

# Creating a string object
my_string = "Hello, World!"
# Using the upper() method on the string object
uppercased_string = my_string.upper()
# Output: "HELLO, WORLD!"
print(uppercased_string)


