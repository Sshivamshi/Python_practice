# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MASKPOL

# cook your dish here
t = int(input())
for i in range(t):
    N , A = map(int, input().split())
    if (A) >= (N + 1)/2 :
        print(N-A)
    else :
        print(A)
