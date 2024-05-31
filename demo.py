# How to check if a string can be converted to a number

# val=input ("type in a number :")
# print(val)
# print  (val.isdecimal())
# print (val.isnumeric())

# if val.isdecimal():
#     num = int (val)
#     print(num)

#Add numbers enters by the user ()
# a = input ("1st number:")
# b= input ("2nd number:")
# print(a+b)

#Add number entered by the user (fixed)
# a= input ("1st number")
# b= input ("2nd number")
# print (int (a)+ int (b))

#Converting string to int 
# a="23"
# print(type(a))
# print (a)
# b= int(a)
# print (type(b))
# print(b)

#Converting float to int 
# a=1.2
# print (type(a))
# print (a)
# b=int(1.3)
# print (type(b))
# print (b)
 
# Conditionals:if
# expected_ans="42"
# inp=input ("what is the ans:-")
# if inp == expected_ans:
#     print ("welcome to the India")

#Conditional : if - else
# exp="52"
# inp=input ("what is your number")
# if inp == exp:
#     print ("welcome to bangalore") 
# else:
#     print ("vgit again")   

#Conditional: if - else (other Exm)

# a= input("1st number :-")
# b =input ("2nd number:-")  
# if int (b)==2:
#     print ("cannot divide 2")
# else:
#     print ("accept the number") 
#     print (int (a)/int (b))
# other ex.
# a=input ("1st numaber:-") 
# b = input ("2nd number:-")
# if a==b :
#     print ("the number are equal")
# else:
#     if int(a)<int(b):
#         print(a+'grater than'+b)     
#     else:
#         print(a+ 'smaller than '+b) 

#if ,elif and else

# age = int(input("Enter a number:-")) 
# if age<18:
#     print("under age")
# elif age>35:
#     print ("over age")
# elif    age>25:
#     print("middle age")
# else:
#     print ("age is prafect")



#Use of For Loop
# employees=[
#     [1,"rajeev",50000,0],
#     [2,"raj",80000,0],
#     [3,"raju",30000,0],
#     [4,"ram",40000,0],
#     [5,"rani",70000,0],
# ]
# print ("Befor bonus", employees)
# for emp in employees:
#     bonus = emp [2]*2/10
#     emp[3]=bonus
# print("After bonus", employees)    

#Use of while
# num =0

# while num<=100:
#     print ("", num)
#     num = num +1

#Use brake statement ,continue and pass
# from ast import Continue


# l= list(range(31))
# for i in l :
#     if i>10:
#      break
#     # print (i)
#     if i%2==0:
#        print (i)


# Continue()

# l= list(range(50))

# for i in l:
#    if i >30:
#       print ("i value more than 10")
#       break
   

#    if i%2==0:
    #   print("even")
#       continue
#    print (i)  

#use for nested loop 

# nums = list(range(1,16))
# for num in nums:
#     print("Table of", num)

#     for n in nums:
#         print (num*n,end='  ')
   
#String length (len)
# x= "Rajeev kumar"
# y= len(x)
# print (y)

#String repetition and concatenation
# x= 3 * "rajeev"
# print(list(x))
# for i in x:
#     print(i)

#A character in a string
# x= "rajeev kumar"
# y=x[7]
# print(y)

#String slice
# x= "rajeev kumar"
# y= x[1:7]
# print(y)

#Change a string
# x ="rajeev kumar"
# x=x[:3] + 'u'+ x[8:]
# print(x)
#repeat
# x= "kumar rajeev"
# x= x[:3]+ 'z',"y"+x[6:]
# print(x)
#String copy
# x= "rajeev"
# x= x+"  das"
# print(x)

# Python Programe to seperate character in a given string by using function
#from unittest import result


# def seperate_character(input_string):
#             character=list (input_string)
#             return character
# input_string=input ("Enter a string:- ")
# result= seperate_character(input_string)
# print("seperate character")
# for i in result:
#         print (i)
# Python Programe to seperate character in a given string by using function
# s= "rjeevdas"
# inp=input("Enter a string")
# for i in s:
#     print(i)

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a, b)
# print(x)


#what is position of value(List)
# i=['rajeev','kumar','das']
# a=i.index('das')
# print(a)

#using list Short()
# s=["rajeev","das"]
# s.sort()
# print(s)

#get a string made of the 1st 2 chars from a given string
# s = "HayThere" 
# a = s[:2] 
# print(a) 

#Create a string made of the first and last two characters from a given string
# Using formatted string
# a = "Rajeev kumar das" 
# #Creating formatted string
# b = "{}{}".format(a[0:1], a[-2:]) 
# #Printing the new String
# print("Input string = " + a)
# print("New String = " +b)
#***
# a = "Rajeev kumar Das"
# b= "{}{}".format(a[0:1],a[-2:])
# print(""+b)

# a= list("rajeev")
# print(a[0],a[2])

#using list slicing
# from itertools import count
# a="rajeev kumar das"
# count=0
# for i in a:
#     count=count+1
# b= a[0:1]+a[count-2:count] 
# print(""+b)  

#using string first character have been change

# a ="Rajeev kumar das"
# b=a.replace(a[1],"$")
# print(b) 

# a ="Rajeev kumar das"
# b=a.replace("a","$",1)
# print(b)

#singale string from two given string seperated by a space and swap the first two characters
# a = 'abc'
# b = 'xyz'
# print("Before Swap :",a," ",b)
# a1 = b[:2] + a[2:]
# b1 = a[:2] + b[2:]
# print("After Swap :",a1," ",b1)

# a="kishor"
# b="kumar"
# print(" ",a," ",b)
# a1=a[:2]+b[:2]
# b1=b[:2]+a[:2]
# print("",a1," ",b1)



# adding a character at the end of an input string using the + operator
# a="rajeev"
# a = a + 'ing' 
# print(a)

#find the first appearance of the substring a given string replace the whole
# a = "The lyrics is not that poor"
# b=a.replace("not that poor","good")
# print(b)#The lyrics is good

#find the longest word and it's position in the string.
# str = "RAJEEV welcome in india"
# word_list = str.split()
# longest_word = max(word_list, key = len)
# print("Longest word: ",max(word_list))
# print("Length of the Longest word number: ",len(longest_word))

#remove the nth index character from a nonempty string
# string="abcde"
# n=int(4)
# first = string[:n]   
# last = string[n+1:]  
# print("Modified string:",first+last)

#Chnage a given string to a new string where the first and last character have been exchange
# a="RAJEEV"
# x=list(a)
# y=x[0]
# x[0]=x[-1]
# x[-1]=y
# print("".join(x))

# Python Program to Remove Odd Index Characters in a String
# a ="rajeev kumar das"
# b = ''
# for i in range(len(a)):
#     if(i % 2 == 0):
#         b=b+a[i]
        
# print("Original String :  ", a)
# print("Final String :     ", b)
# #**
# a= "rajeev kumar das"
# b=""
# for i in range(len(a)):
#     if (i%2==0):
#         b=b+a[i]
# print(b)

# #***
# a= "rajeev kumar das"
# b=""
# for i in range(len(a)):
#     if(i%2==0):
#         b=b+a[i]
# print(b)

#find odd and even number from list
# n =[5,8,9,77,25,68,1,58,96,33,74,58,72,66]
# for i in n:
#     if(i%2)==0:
#         print(i," even")

#     else:
#         print(i," odd")

#** for user input
# n =int(input("enter a number"))
# lst=[n]

# for i in lst:
#     if(i%2)==0:
#         print(i,"is even")

#     else:
#         print(i,"is odd") 

lis=["2","8","9","1","6"]
print(lis.sort())
print(lis)