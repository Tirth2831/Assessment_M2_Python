'''
Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
'''
string1 = "hello"
string2 = "world"

if len(string1) < 2 or len(string2) < 2:
    result = "Both strings must have at least two characters."
else:
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]
    
    result = new_string1 + " " + new_string2

print(result)
    
