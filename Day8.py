# PALINDROME CHECK 

s = "MoM"
list1 = list(s)
sr =""
for ele in s :
    sr += ele

if s == sr:
    print("palindrome")
 
# FACTORIAL USING FOR LOOP

def factorial(N):
    fact = 1
    for i in range(1,N+1):
        fact *= i
    
    print(fact)
    
factorial(4)


# FACTORIAL USING FOR LOOP and counting Digits in factorial 

def factorial(N):
    fact = 1
    for i in range(1,N+1):    #as required range is 1 to N  [ range(5) means 0-4
        fact *= i
    
    print(fact)
    s = str(fact)      # converting int to string(so that it becomes iterable , can be later turned to list and find length / no. of element)
    list1 = list(s)
    print(len(s))       #print number of digits in the factorial 
    
factorial(4)