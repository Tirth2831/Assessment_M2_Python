'''
Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.
'''

s = "The movie is not that poor!"

not_index = s.find('not')
poor_index = s.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:
  
    s = s[:not_index] + 'good' + s[poor_index + len('poor'):]

print(s)
