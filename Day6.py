a = -32.75
print(abs(a))   # 32.75            coverts to +ve if a negative number 
print(round(a))  # -33             Round off to int
print(round(a,1))   # -32.8        Round of upto 2 decimal places
# Second argument here, is the place after decimal upto which round off is required
b = -29.846
print(abs(round(b,2)))  # 29.85
print(abs(round(b,1)))   #29.8
print(abs(round(b)))      # 30

# LISTS TUPLES ANS SETS

students = ["Himmi","AKii", "Bruce","Mohit","Rahul", "Vishwa"]
#slicing operation in lists

print(students[0:4]) # ['Himmi', 'AKii', 'Bruce', 'Mohit']                 # from INDEX 0 to POSITION 4
print(students[:5])  #['Himmi', 'AKii', 'Bruce', 'Mohit', 'Rahul'] 
print(students[2:4]) # ['Mohit', 'Rahul']                                 # from INDEX 2 to POSITION 4

# LIST METHODS
# .append() and .insert() are similar somehow , append adds an element at the last and insert adds an element in a certain position

courses = ["ece", "maths","phy","cse"]
courses2 = ["english","science"]
courses.append("INT")
print(courses)   #  ['ece', 'maths', 'phy', 'cse', 'INT']
courses.insert(0 ,"history")
print(courses)   #  ['history', 'ece', 'maths', 'phy', 'cse', 'INT']
courses.insert(1, courses2)
print(courses) #    ['history', ['english', 'science'], 'ece', 'maths', 'phy', 'cse', 'INT']
courses.append(courses2)
print(courses)  #   ['history', ['english', 'science'], 'ece', 'maths', 'phy', 'cse', 'INT', ['english', 'science']]
 
# Note how append() and insert() are inserting the whole list (courses2) instead of elements of the list , inside the list courses


courses = ["ece", "maths","phy","cse"]
courses2 = ["english","science"]   

courses.extend(courses2) # Only takes one argument
print(courses) #['ece', 'maths', 'phy', 'cse', 'english', 'science']

# Extend is good when we have multiple values to insert into a list , or join two lists by extending

courses3 = ("hindi","sanskrit")  #courses 3 is a tuple

courses.append(courses3)  #can append a tuple too 
print(courses)  # ['ece', 'maths', 'phy', 'cse', 'english', 'science', ('hindi', 'sanskrit')] 
courses2.insert(1,courses3)     #can insert a tuple too , at given location 
print(courses2)  # ['english', ('hindi', 'sanskrit'), 'science']

#note : why not print(courses.append(courses2)) ? since .append() and .insert() returns void/none , it's just to operate with existing list. so  none is printed.
print(courses.append(courses2))   # None
print(courses.extend(courses2))   # None

courses2.extend(courses3)   # The extend() method takes all the elements from another iterable (like list /tuple) and adds them to the end of the list. Instead of appending/Inserting the whole tuple itself
print(courses2)  # ['english', ('hindi', 'sanskrit'), 'science', 'hindi', 'sanskrit']

'''
courses.sort() or courses2.sort
print(courses) # Error if we put here because we cannot use sort method as all are not of same datatype , (Tuple is present in both LISTs)

'''
courses = ["ece", "maths","phy","cse"]
courses.sort() 
print(courses)     # ['cse', 'ece', 'maths', 'phy']
courses.reverse()   #using reverse after sort() method , to get descending order sort
print(courses) # ['phy', 'maths', 'ece', 'cse']





def func1():
    print("Before call of func2")
    func2()
    print(" Func 1 was just executed")
    
def func2():
    print("Before call of func3")
    func3()
    print(" Func 3 was just executed")

def func3():
    print(" Final execution / Func3 execution")
    
func1()

''' OUTPUT : (order of execution)

Before call of func2
Before call of func3
 Final execution / Func3 execution
 Func 3 was just executed
 Func 1 was just executed 
 '''




