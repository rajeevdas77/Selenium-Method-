# s1="rajeev python automation"
# duplicate_char = []
# for character in s1:
#       if s1.count(character) > 1:
#          if character not in duplicate_char:
#             duplicate_char.append(character)
# print(*duplicate_char)

# s2= "rajeev das kumar"
# duplicate_char=[]
# for character in s2:
#     if s2.count(character)>1:
#         if character not in duplicate_char:
#             duplicate_char.append(character)
# print(duplicate_char)  
 
#Extend
# l1=['apple','banana','chrey']
# l2=[1,2,5,8,5]
# l2.extend(l1)
# print(l2) 

# a=["kumar","das"]
# b=["rajee"]
# b.extend(a)
# print(b)

# a=" kumar das"
# b="rajeev"
# c= b+a
# print(c)

# a=" kumar das"
# b="rajeev"
# c=''.join([b,a])
# print(c)

#Insert
# l1=[1,5,8,9,6,2]
# l1.insert(2,52)   
# print(l1)

# fruits = ['rajeev', 'kumar', 'das']

# fruits.reverse()

# print(fruits)

# s={
#     "Name":"Rajeev",
#     "Id": "Raj123",
#     "age": 26
#     }
# s.update({"hight": 5.5})
# print(s)

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.index(5)

# print(x)

#how to reverse a string in python without changing the position of words?
# str5 = 'peter piper picked a peck of pickled peppers.'
# b = str5.split()
# rev_str5 = ""
# for i in b:
#     rev_str5 = rev_str5 + ' ' + i[::-1]
# print(rev_str5.lstrip()) # Removes the one space in the starting.

#another method
# s= "welcome to india"   
# print(' '.join(w[::-1] for w in s.split()))

#similer word
# a=['rajeev','rajeev','kumar','das']
# b=a.count('rajeev')
# print(b)

# a= "i love python coding"
# b= "coding in python is easy"
# for i in a:
#     if i in b:
#         print(i)

# a= "rajeev automation tester"
# a=' '.join(reversed(a))
# print(a)
