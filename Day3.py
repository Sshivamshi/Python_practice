# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ATM2

t = int(input())  # taking input string and converting to int

for i in range(t):
    # peeps, total = map(int, input().split())  # corrected map() syntax
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
