t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    a.sort()
    size = len(a)
    print(a,size)


# CODECHEF SOLUTION OF FINDING SUM OF TWO DISTINCT INTEGER

    t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    a.sort()
    size = len(a)
    
    if a[size-1] != a[size-2]:
        print(a[size-1] + a[size-2])
    else:
        for num in reversed(a):
            if a[size-1] != num:
                print(a[size-1] + num)
                break