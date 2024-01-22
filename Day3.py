# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ATM2

t = int(input())  # taking input string and converting to int

for i in range(t):
    # peeps, total = map(int(), input().split())  # corrected map() syntax
    peeps, total = map(int, input().split())  # corrected map() syntax
    a = list(map(int, input().split()))
    output = []

    for nums in a:
        if total == 0 or total < nums:
            output.append(0)
        elif total >= nums:  # corrected condition
            total -= nums
            output.append(1)

    # Use str() to convert the list of integers to a string
    print("".join(map(str, output)))




# https://www.codechef.com/practice/course/arrays-go/PGOAR01/problems/KITCHENCOST


t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    output = 0
    # Your code goes here
    for i in range(n):
            if a[i] >= x:
                output += b[i]
                
    print(output)
    t -= 1


# https://www.codechef.com/practice/course/arrays-go/PGOAR01/problems/RUNCOMPARE

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    
    for i in range(n):
        if 2*a[i] >= b[i] and 2*b[i] >= a[i]:
            count += 1
    print(count)
    t -= 1

