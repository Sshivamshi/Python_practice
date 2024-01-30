# https://www.codechef.com/practice/course/strings-python/PPYST01/problems/TWOSTR


t = int(input())

while t > 0:
    x = input()
    y = input()
    listx = list(x)
    listy = list(y)
    c = 0
    for char1,char2 in zip(listx,listy):        # using Zip function
        if char1 == char2 or char1 == '?' or char2 == '?':
            c += 1
        else:
            break
    
    if c == len(listx):
        print("Yes")
    else:
        print("No")
    t -= 1



