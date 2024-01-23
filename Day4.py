# https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/EZSPEAK


t = int(input())
for i in range(t):
    
    n = int(input())
    word = input()
    count = 0 
  # for i in range(n):
    # if word[i] != "A" or word[i] != "a"  && word[i] != "E" or word[i] != "e" .....till "u"and "U"         #Bruteforce method
     
    # OR covert string to upper or lower case using .upper() and .lower() then check for just lowercase , 5 vowels are only needed   but we should not directly manipulate input rather take a dublicate variable
    for char in word:
        if char not in 'aeiou':
            count += 1             # count++ is not a valid expression in Python
            if count >=4 :      # IMP  in nested IF , its checking if count >= 4 everytime , we can use to check the count conditon(IF-ELSE) only when next vowel is encountered. if count < 4 , then count = 0 (reset)
                break         #we are checking the adjacent characters , so breaking out of loop once 4 consonants are acquired
        else:
            count = 0     #note here the count resets once encountered a vowel , it may have had reset count even after 5 consonant is enocountered FOLLOWED BY A VOWEL if not for the above condition
            
    if count >=4 :
        print("NO")
    else:
        print("YES")
    


# 

t = int(input())
for i in range(t):
    
    ddsa, dtoc ,ddm = map(int , input().split())    #since single line input
    sdsa, stoc , sdm = map(int , input().split())   
    dtot = ddsa + dtoc + ddm
    stot = sdsa + stoc + sdm
    
    if stot == dtot:
        if sdsa == ddsa:
            if dtoc == stoc:
                print("TIE")
            elif dtoc > stoc:
                    print("DRAGON")
            else :
                print("SLOTH")
        elif ddsa > sdsa:
            print("DRAGON")
        else :
            print("SLOTH")
    elif dtot > stot :
        print("DRAGON")
    else :
        print("SLOTH")
        