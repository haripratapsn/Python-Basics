# Given a string s of single space-separated words. Capitalize the first letter of all words and count the number of the words in the string. Print the line and the number in separate lines with new line character at the end.

# Examples:

# Input: s = "welcome to the world of geeks"
# Output: 
# Welcome To The World Of Geeks
# 6
# Input: s = "are you enjoying programming"
# Output:
# Are You Enjoying Programming
# 4 



s = input()
capital_words=[]
words=s.split()
count=0
for word in words:
    capital_word=word[0].upper() + word[1:].lower()
    capital_words.append(capital_word)
    count+=1
    
print(" ".join(capital_words))
print(count)

