# from audioop import reverse
from itertools import count
from re import X, sub
from shlex import join
import string
from tkinter import Y


# l=[1,2,3,6,5]
# l.append(2)
# print(l)

# a= "rajeevdas"[::-2]
# print(a)



# l = ["a", "b", "a", "c", "c"]
# print(reverse(l))
# def reverse(list):
#     new_list=list[::-1]
#     return new_list
# list = ["a", "b", "a", "c", "c"]
# print (reverse(list))


# def reverse(list):
#     n_list=list[::-1]
#     return n_list
# list=[1,2,5,8,989,88,8]
# print (reverse(list))






# # mylist = list(dict.fromkeys(mylist))

# mylist.pop(2)
# print(mylist)

# a= "kishorrajeev"[::-1]
# print(a)

#Reverse
# a= "kumardas"
# a= "".join(reversed(a))
# print(a)

#Python: Swap two variables
# a=10
# b=20
# print("a = ", a)
# print("b = ", b)
# t=a
# a=b
# b=t
# print("a =", a)
# print("b =", b)

#another method

# num1=input("enter a num1 number:-")
# num2= input("enter a num2 number:-")
# print("",num1)
# print("",num2)
# temp=num1
# num1=num2
# num2=temp
# print("",num1)
# print ("",num2)


# x = 34
# y = 56
# print("Initial Value of x =", x)
# print("Initial Value of y =", y)
# temp = x
# x = y
# y = temp
# print("\nAfter swaping value of x =", x)
# print("After swaping value of y =", y)


#Given a string, the task is to reverse the order of the words in the given string.

# s = 'i like this program very much '
# a= s.split(" ")
# string=[]
# for b in a:
#     string.insert(0,b)
# print(" ".join(string)) 
#another method (best)   
# a= "rajeev kumar das"
# b=a.split()[::-1]
# print(" ".join(b))

# print(a)
#Another mathod use
# a= "rajeev kumar das"
# a="".join(reversed(a))
# print(a)

# python if condition
'''
a= int (input("Enter a value:-"))
if a%2==0:
    print(a,"even number")  
else:
    print(a,"odd number") 
'''

#use a IF, eilf,else
# a=int(input("Enter a number:-"))
# if a>=80:
#     print("1st Division")
# elif a>=50:
#     print("2nd Division")  
# elif a>35:
#     print("3rd Division")
# else:
#     print("Fail")          


#For loop with Range
# for a in range(5):
#     print(a)
# for b in range (1,11):
    # print(b)    

#While Loop
# i=1
# while i <=10:
#     print("rajeev")
#     i=i+1
# i=1
# while i <5:
#     print("das")
#     i=i+1

# How to check number is prime or not?

# num=17
'''
num=int(input("Enter a Number:-"))
count=0
if num>1:
    for i in range(2,num-1):
        if (num%i)==0:
            count=count+1
    if count==0:
        print("number is prime ")
    else:
        print("number is not prime")  
'''
'''
#How to find the factorial of a number?
factorial=1
# num=5
num = int(input("Enter a number:-"))
if num<0:
    print("Factorial does not exist for negative number")
elif num==0:
    print("Factorial 0 is 1")
else:
    for i in range (1,num+1):
        factorial=factorial * i
    print("Factorial of ", num, "is ",factorial) 
'''

# How to print the Fibonacci series?

# n1=0
# n2=1
# print(n1)
# print(n2)
# for i in range(1,100):
#     sum=n1+n2
#     print(sum)
#     n1=n2
#     n2=sum

#How to find sum of element in an array?
# array=[1,2,3,4,5]
# print (sum(array))

#How to find maximum and minimum element in array?
#Maximum
# a= [1,8,5,6,5,44589]
# max=a[0]
# n=len(a)
# for i in range(1,n):
#     if a[i]>max:
#         max=a[i]
# print ("maximum element ",max)    

#Minimum
'''
b= [1,5,8,9,4]
min=b[0]
n=len(b)
for i in range(1,n):
    if b[i]<min:
        min=b[i]
print ("minimum element",min)        
'''

b= [1,5,6,8,9]


