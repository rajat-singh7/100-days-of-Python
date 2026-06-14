#Write a Python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language.

#Coding:
#If the word contains atleast 3 characters, remove the first letter and append it at the end 
# Now append three random characters at the starting and the end..
#else:
#Simply reverse the string

#Decoding:
#If the word contains less than 3 characters, remove it
#else:
#remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
#Your program should ask whether you want to code or decode
import random
import string

word = input("Choose a Word:")

choice = input("What you want to do Code or decode? write c/d ").lower()
if choice == "c":
    coded_word = word[1:]+ word[0] #ajat + R
    random_letters = ''.join(random.choices(string.ascii_letters,k = 3))
    final_code =  random_letters + coded_word + random_letters
    print("Coded Word" ,final_code)
elif choice == "d":
    coded_word = input("Paste the coded word:") 
    without_random = coded_word[3:-3]
    decoded_word = without_random[-1] + without_random[:-1]
    print("Decoded Word",decoded_word)
else:
    print("Please choose only c or d:")
    

