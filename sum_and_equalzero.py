'''
Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.
'''
n1=int(input("Enter Number 1 : "))
n2=int(input("Enter Number 2 : "))
n3=int(input("Enter Number 3 : "))

sum=n1+n2+n3
if n1==n2:
    print(" 0 ")
elif n2==n3:
    print(" 0 ")
elif n1==n3:
    print(" 0 ")
else :
    print(sum)
