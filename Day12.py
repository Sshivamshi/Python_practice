t = int(input())
while (t>0):
    count = 0
    n = int(input())
    s = input()
    
    if s == '1'*(n):
        print('1')
    elif s == '0'*(n):
        print('0')
    else:
        lists = list(s)
        for num in lists:
            if num == '1':
                count += 1
            else:
                continue  #skip if digit is already 0 
            
        print(count)
    t -=1

 # https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ZEROSTRING

t = int(input())
while (t>0):
    count1 = 0
    count0 = 0
    n = int(input())
    s = input()
    
    if s == '1'*(n):
        print('1')
    elif s == '0'*(n):
        print('0')
    else:
        lists = list(s)
        for num in lists:
            if num == '1':
                count1 += 1
            else:
                count0 += 1  
        if count1 > count0 :
            print(count0 + 1)
        else :
            print(count1)
        
    t -=1

# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/AIRLINE

t = int(input())
while(t>0):
    a , b, c , d , e =  map(int , input().split())
    mini = min( a, b, c)
    maxi = max(a, b, c)
    sums = a + b + c
    if min(a , b , c) > e  :
        print('NO')
    elif ( a + b <= d and c <= e) or (a + c <= d and b <= e ) or (b + c <=d and a <= e ) : 
        print('YES')
    else: 
        print('NO')
    t -= 1 

# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CHEFSTUD

t = int(input())
for i in range(t):
    s = input()
    res = s.count('<>')
    print(res)
    
# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PIZZA_BURGER

t = int(input())
for i in range(t):
    money , y , z = map(int , input().split()) 
    
    if money >= y and money < z:
        print('PIZZA')
    elif money >= y and money >= z:
        print('PIZZA')
    elif money >= z and money <= y  :
        print('BURGER')
    else :
        print('NOTHING')
        

# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/CANDY123?tab=statement


t = int(input())
for i in range(t):
    counter = 1
    lim , bob = map(int , input().split())
    lims = 0 
    bobs = 0 
    while True :
        if lims <= lim:
            lims += counter
            counter += 1
        else :
            print('Bob')
            break
        if bobs <= bob :
            bobs += (counter)
            counter += 1
        else :
            print('Limak')
            break
              
    
