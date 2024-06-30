'''
Write a Python program to count the number of characters (character
frequency) in a string
'''
s= input("Enter a String : ")
frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

