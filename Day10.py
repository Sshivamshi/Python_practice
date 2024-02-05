
n = int(input())
for i in range(1, n):
    print(f"{i}" * i)

# printing pattern through recursion

n = int(input())

def output(n):
    if n == 1:
        print(1)
        return 1
    else:
        ones = (10 ** (n - 1)) + output(n - 1)
        print(ones*ones)
        return ones
output(n)

