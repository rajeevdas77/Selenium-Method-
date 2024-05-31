# list1 = [1,2,3,4,5]
# list2=[8,6,4,2]
# list3 = [1,3,5,7]

# list4= list1+list2+list3
# print(list4)

# list_5=[1, 2, 3, 4, 5, 8, 6, 4, 2, 1, 3, 5, 7]
# print ("The list is: " + str(list_5)) 
# list_5 = list(set(list_5)) 
# print ("The list duplicates: " + str(list_5))
#Output= he list after removing duplicates: [1, 2, 3, 4, 5, 6, 7, 8]

# list6=[1, 3, 4, 2, 7, 6, 5, 8]
# list6.sort()
# print(list6)

# num=int(input("Enter a number : "))
# factorial=1
# if num <0:
#     print("factorial number does not exit negative number")

# elif num ==0:
#     print("factorial number 0 is 1 ")
# else :
#     print("the factorial number")

# num= int (input("Enter a number"))
# if num>0:
#     print("positive number")
# elif num ==0:
#     print("Zero")
# else:
#     print("negative number")

# num =int(input("enter a number"))
# if num >0:
#     print("positive numbe")
# elif num ==0 : 
#     print("Zero")
# else :
#     print("negative")

# num = int (input ("Enter a number :"))
# if(num%2)==0:
#     print(format(num),"even number")
# else:
#     print(format(num),"odd number")


# num = int (input ("Enter a number"))
# if (num %2)==0:
#     print(format(num),"even number")
# else:
#     print(format(num),"odd number")

# lower = 900
# upper= 1000
# print("Prime number between",lower,"and",upper,"are:")
# for num in range(lower, upper + 1 ):
#     if num >1:
#         for i in range (2,num):
#             if (num%i) ==0:
#                  break
#             else :
#                 print (num)


# lower = 1
# upper = 100

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


# class A:
#     def show(sefl):
#         print("welcome")


# class phone :
#     def make_call (self):
#         print("I am making a call")
#     def play_game(sefl):
#         print("I am playing a game ")

#     def ludu_game(self):
#         print("rajeev plya a game")

#     def action_game(self):
#         print("good game")        

        
# p1=phone()
# p1.make_call()
# p1.play_game()
# p1.ludu_game()
# p1.action_game()

#overloding
# def product(a,b):
#     p=a*b
#     print(p)

# def product(a,b,c):
#     p=a*b*c
#     print(p)   

# product(2,2,2)     

#overrinding
# class A:#parent class
#     def Disp(self):
#         print("This is parent calss")
# class B(A):#child         
#     def Disp(self):
#         # super().Disp()
#         print("This is child class")
# obj=B()
# obj.Disp()

# class A: #parent class
#     def Disp(Self):
#         print("this is parent class")
# class B(A):#child class 
#     def Disp(self):
#         super().Disp() #call of parent calss
#         print("This is child class")

# obj=B()
# obj.Disp() 

#encupsulation

# class A:
#     _a=10
#     __b=20
#     def show(self):
#         print("a=",self._a)
#         print("b=", self.__b)
# obj=A()
# obj.show()  # inside class
# # #outside class run 
# print("outside of class",obj._a)
# print("outside of class",obj.__b)



# def Add():
#     a= int(input("Enter a first number"))
#     b= int (input("Enter a second number"))
#     sum=a+b;
#     print("addition of two number:",sum)

# print(len("rajeev"))
# print(len(["rajeev","das"]))

#decorator
# def div(a,b):# change the code
#     if a<b:
#         a,b=b,a
#     print(a/b)
# div(2,4)

# def div1(a,b):# without change the code useing decotorator
#         print(a/b)

# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func (a,b)
#     return inner

# div1=smart_div(div1)
# div1(2,4)
    
#useing lambda function
# str1 = "Rajeev Kumar Das"
# lower= lambda string:string.lower()#
# print(lower(str1)) # have a any number of argumaent but only one expression

# a = lambda x:x*2
# print(a(5))

# b= lambda x,y,z:(x+y+z)/2
# print(b(3,5,10))

# class GeekforGeeks:
 
#     # default constructor
#     def __init__(self):
#         self.geek = "GeekforGeeks"
 
#     # a method for printing data members
#     def print_Geek(self):
#         print(self.geek)
 
# # creating object of the class
# obj = GeekforGeeks()
 
# calling the instance method using the object obj
# obj.print_Geek()

# class A:
#     def __init__(self):
#         self.act="Rajeev Kmar Das"l

#     def print_act(self):
#         print(self.act)
# obj=A()
# obj.print_act()


#parameterzied constructor
# class student:
#     def __init__ (self,name):
#         # print("this is parametorized constructor")
#         self.name=name
#         # self.age=age
#     def show (self):
#         print("Hello",self.name)
#         # print("27",self.age)
# student=student("RAJEEV DAS")
# # student=student("age=27")
# student.show()

#EX 
# class Add:
#     first=0
#     second=0
#     ans=0

#     def __init__(self,f,s):
#         self.first=f
#         self.second=s
#     def displya(self):
#         print("first number="   +str(self.first))
#         print('secone number='  +str(self.second))
#         print("add two number=" +str(self.ans))
#     def calculate (self):
#         self.ans=self.first - self.second

# obj1=Add(1000,5000)
# obj2=Add(10,500)
# obj1.calculate()
# obj2.calculate()
# obj1.displya()
# obj2.displya()


# lst=[1,2,3,4,5]
# lst.append(6)
# print(lst)
# a=[7,8]
# lst.append(a)
# print(lst)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)
 #Generator
# def sample_generator(number):
# 	for i in range(number):
# 		yield f"Next number is {i}"
# if __name__=="__main__":
#         number=9
		
#         gen_obj=sample_generator(number)
#         print(type(gen_obj))
#         #get value
#         print(next(gen_obj))
#         print(next(gen_obj))
#         print(next(gen_obj))
#iteratore
# class ArrayList:
#    def __init__(self, number_list):
#        self.numbers = number_list
#    def __iter__(self):
#        self.pos = 0
#        return self
#    def __next__(self):
#        if(self.pos < len(self.numbers)):
#            self.pos += 1
#            return self.numbers[self.pos - 1]
#        else:
#            raise StopIteration
# array_obj = ArrayList([1, 2, 3])
# it = iter(array_obj)
# print(next(it)) #output: 2
# print(next(it)) #output: 3
# print(next(it))

# string = "RajeevKumarDAS"
# print(string.swapcase() )

# g.py
# class GeeksClass:
#     def function(self):
#         print ("function()")
# import m
# def monkey_function(self):
#     print ("monkey_function()")
 
# m.GeeksClass.function = monkey_function
# obj = m.GeeksClass()
# obj.function()

#*arg
# def multiply(a, b, *argv):
#    mul = a * b
#    for num in argv:
#        mul *= num
#    return mul
# print(multiply(1, 2, 3, 4, 5)) #output: 120

# def tellArguments(**kwargs):
#    for key, value in kwargs.items():
#        print(key + ": " + value)
# tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")
# #output:
# # arg1: argument 1
# # arg2: argument 2
# # arg3: argument 3

# l=[1,2,5,6,8,9,3]
# s=slice(1,3)
# print(l[s])
#overlodding
# class A:
#     def show(self):
#         print("welcome")
#     def show(self,firstname=''):
#         print("welcome",firstname)
#     def show(self, firstname='' , lastname=''):
#         print("welcome",firstname,lastname)
# obj=A()
# obj.show()

# overrinding

# class father:
#     def transporte (self):
#         print("cycle")
# class son(father):
#     def transporte(self):
#         #9o
#         super().transporte()
#         print("bike")
# obj=son()
# obj.transporte()

#decorator is function that you can use to modifit or
#extand the behavier of other function or methood without changing code
# def div1(a,b):
#     print(a/b)
# def smart_div (func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner
# div1=smart_div(div1) 
# div1(2,4)

# lst=[1,5,8,6,8,9]
# lst1=[5,8,9,1,2,3]
# lst2=[7,8,6,2,1]
# lst3=lst+lst1+lst2
# print(lst3)
# lst4=[1, 5, 8, 6, 8, 9,4,5, 8, 9, 1, 2, 3, 7, 8, 6, 2, 1]
# lst5=set(lst4)
# print(lst5)
# lst6={1, 2, 3, 4, 5, 6, 7, 8, 9}
# lst7=sorted(lst6)
# print(lst7)

# from _pytest.junitxml import merge_family

# def merge(a,b,c):
#     return sorted(set(a+b+c))
# a1=[1,5,8,6,8,9]
# b1=[5,8,9,1,2,3]
# c1=[7,8,6,2,1,5]

# lst3=merge(a1,b1,c1)
# print(lst3)


def merge(A,B,C):
    return sorted(set(A+B+C))
a1={"s","r","e","f","g"}
b2={"r","e","f","g","t"}
c3={"e","r","f","g","t"}
d4= merge(a1,b2,c3)
print(d4)




          
     








        
































