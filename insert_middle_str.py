'''
Write a Python function to insert a string in the middle of a string.
'''
main_string = "HelloWorld"
insert_string = "123"

middle_index = len(main_string) // 2

result = main_string[:middle_index] + insert_string + main_string[middle_index:]

print(result)
