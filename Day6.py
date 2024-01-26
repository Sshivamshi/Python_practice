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
