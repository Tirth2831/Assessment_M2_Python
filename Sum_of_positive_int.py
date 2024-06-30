'''
Write a python program to sum of the first n positive integers.
'''
def sum_positive_integers(n):
    if n <= 0:
        return "Please Enter a Positive Integers"
    return n * (n + 1) // 2
print(sum_positive_integers(12))
