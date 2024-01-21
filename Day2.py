t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    a.sort()
    size = len(a)
    print(a,size)


# https://www.codechef.com/practice/course/arrays-python/PPYAR01/problems/LARGESECOND

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

# https://www.codechef.com/practice/course/arrays-python/PPYAR01/problems/CS2023_STK

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    
    count = 0 #initilization of count outide loop
    streak = 0
    for nums in a:
        if nums == 0:
            count = 0 #assigning count = 0 if a num is 0 , count can be called current or temporary streak here 
            continue #to skip iteration for this value of num after setting current count to 0
        elif nums > 0 :
                count += 1
        streak = max(streak,count)   #update streak if current count > streak
        
    count1 =  0 
    streak1 = 0
    for nums1 in b:
        if nums1 == 0:
            count1 = 0  #count reset
            continue #to skip iteration for this value of num
        elif nums1 > 0 :
            # count1++wrong
            count1 += 1  # Use += for incrementing count
        streak1 = max(streak1,count1)  
        
    if streak > streak1 :
        print("Om")
    elif streak < streak1:
        print("Addy")
    else:
        print("Draw")