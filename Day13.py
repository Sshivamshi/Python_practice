# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MASKPOL

# cook your dish here
t = int(input())
for i in range(t):
    N , A = map(int, input().split())
    if (A) >= (N + 1)/2 :
        print(N-A)
    else :
        print(A)

t = int(input())
for i in range(t):
    N , A = map(int , input().split())
    print(min((A), (N-A)))

# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/HEADBOB


t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if 'Y' in s:
        print('NOT INDIAN')
    elif 'I' in s :
        print('INDIAN')
    else:
        print('NOT SURE')
    
            
        
        
