# import os
# os.getcwd()
# os.chdir('C:\\Users\\lenovo\\Desktop\\file_handling')
# f= open('hello.txt','w')
# f.write("I am a CSE Branch student")
# f.write("\n my university name is Chitkara")
# f.write("\n  my name is aparna")
# print('data successfully')
# print("\n data has complete successfully")
# f.close()

# with open("hello.txt") as f:
#     with open("aparna.txt","w") as f1:
#         for line in f:
#             f1.write(line)
#             f.write

# fname = input("enter file  name: ")
# num_lines = 0
# with open(fname,"r")as f:
#     for line in f:
#         num_lines += 1
#         print("number of lines : ")
#         print(num_lines)

# fname = input("enter file name: ")
# k = 0
# with open(fname , "r") as f :
#     for line in f:
#         words = line.split()
#         for i in words:
#             for letter in i:
#                 if (letter.isspace):
#                     k = k + 1
# print("occurence of blank spaces: ")
# print(k)

# fname= input("enter file name: ")
# word= input("enter word to be searched: ")
# k = 0 
# with open(fname , "r") as f:
#     for line in f:
#         word = line.split()
#         for i in word:
#             if (i == word):
#                 k=k+1
# print("occurence of blank spaces: ")
# print(k)

# import math

# print("the value of pi is ", math.pi)

# import math as m
# print("the value of pi is:", m.pi)

# from math import*
# print("the value of pi is ", pi)
# print("sqrt of 5" , sqrt)

import aparna
a = aparna.person["age"]
print(a)

