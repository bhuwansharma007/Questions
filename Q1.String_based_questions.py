# Write a program to take an input string and exchange the first and last word and reverse the middle word. 
# Input: Hello World GFG Welcomes You 
# Output:You semocleW GFG dlroW Hello

str1 = input("Enter String") 

header = str1.split(" ")[0]
footer = str1.split(" ")[-1]
answer = str1[::-1]
answer = answer.replace(header[::-1],header)
answer = answer.replace(footer[::-1],footer)

print(answer)