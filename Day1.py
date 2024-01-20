
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
Names = ["Akii","Himmi", "Bruce"] #list (orderered collection as mutable)
print(id(Names[2]))     #140585041201648
Names[2] = "Maheet"
print( Names , id(Names[2])) #['Akii', 'Himmi', 'Maheet'] 140585040881648 id same before and after hence mutablity 
#Structure also similar to array 
Names2 = ("Akii", "Himmi" , "Bruce")
print(id(Names(2)))
Names2(2) = "Mohit"  #Error: tuple' object does not support item assignment
 
Print(Names2 , id(Names2(2)))
