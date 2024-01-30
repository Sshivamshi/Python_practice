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



# https://www.codechef.com/practice/course/strings-python/PPYST01/problems/BLOBBYVOLLEY 

t = int(input())

def swaps(server, receiver):
    temp = server
    server = receiver
    receiver = temp
    return server, receiver

while t > 0:
    n = int(input())
    s = input()
    win = list(s)
    server = "Ali"
    receiver = "Bob"
    alice_score = 0
    bob_score = 0
    
    for i in range(n):
        if win[i] == 'A':
            if server == 'Ali':
                alice_score += 1
            elif server == 'Bob':
                server, receiver = swaps(server, receiver)
        
        elif win[i] == 'B':
            if server == 'Bob':
                bob_score += 1
            elif server == 'Ali':
                server, receiver = swaps(server, receiver)
    
    print(alice_score, bob_score)
    t -= 1
