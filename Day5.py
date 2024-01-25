my_message = "himmi"
message = """ This
              is a multiline string  """ 
print(my_message , message)              
print(my_message)  
print(message)  
''' 
OUTPUT: 
himmi  This      (Output on same line)
              is a multiline string 

himmi        
 This              (Second line of output)
              is a multiline string  
'''


'''
This is a multi-line comment.
It spans multiple lines.
'''

"""
Another way to create a multi-line comment.
Use triple double quotes .
"""


message = "Bruce is goodg"
print(len(message)) #13 (includes space )
print(message[0:5])  #Bruce   (prints range of characters from a string )

# STRING METHODS 

print(message.lower())   # bruce is goodg
#Takes string input and return lowercase of that string 

print(message.upper())  # BRUCE IS GOODG
#Takes string input and return uppercase of that string 

print(message.count("o")) # 2  

#takes char,string and returns number of times it appeared
print(message.count("good")) # 1

#takes string and returns index of first letter of word/string
print(message.find("good")) # 9 

#Takes a char/Alphabet and returns the index of FIRST OCCURENCE"
print(message.find("g")) # 9 

message = message.replace( 'good', 'bad' ) # Bruce is badg  
print(message)