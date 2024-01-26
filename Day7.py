# recursion : when a function calls itself  
 
# program to find factorial

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
    
print(fact(5)) 


# Program to find natural number sum upto n natural number

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
        
print(sum(5))    # 


# Program to find power using recursion

def power(N,R):
        if R == 1:
            return N
        else:
            return N*power(N , R-1)

print(power(2,3)) #  8