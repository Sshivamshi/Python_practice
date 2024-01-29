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