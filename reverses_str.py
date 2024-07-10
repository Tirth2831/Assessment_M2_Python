'''
Write a Python function to reverses a string if its length is a multiple of 4.
'''
def reverse(s):
    if len(s) % 4 == 0:
        return s[::-1]
    return s

input_string = "name"
result = reverse(input_string)
print(result)

input_string = "to"
result = reverse(input_string)
print(result)

