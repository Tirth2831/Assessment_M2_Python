'''
Write a Python program that will return true if the two given integer
values are equal or their sum or difference is 5.
'''
n1=int(input("Enter a Number 1 : "))
n2=int(input("Enter a Number 2 : "))
if n1==n2:
    print("True")
elif n1+n2 == 5:
    print("True")
elif abs(n1-n2)==5:
    print("True")
else :
    print("False")

