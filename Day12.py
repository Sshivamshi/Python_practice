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