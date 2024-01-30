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


# https://www.codechef.com/practice/course/strings-python/PPYST01/problems/DNASTORAGE


t = int(input())

while t > 0:
    n = int(input())
    s = input()
    binary = list(s)
    st = ""
    
    for i in range(len(binary)):
        if i % 2 == 0:
            continue
        
        elif i % 2 == 1:
            if binary[i] == '0' and binary[i-1] == '0':
                st += 'A'
            elif binary[i] == '0' and binary[i-1] == '1':
                st += 'C'
            elif binary[i] == '1' and binary[i-1] == '0':
                st += 'T'
            elif binary[i] == '1' and binary[i-1] == '1':
                st += 'G'
    
    print(st)
    t -= 1



# https://www.codechef.com/practice/course/strings-python/PPYST01/problems/TWOSTR


# approach : all non '?' positions should be equal