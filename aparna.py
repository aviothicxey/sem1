# person={
#     "name":"john",
#     "age":"36",
#     "country":"norway"
# }


# def myfunction(x,y,z):
#     myfunction= max(x,y,z)
#     return myfunction
# x= float(input("enter the value of x: "))
# y= float(input("enter the value of y: "))
# z = float(input("enter the value of z: "))

# greatest_number= myfunction(x,y,z)
# print("greatest number is: ", greatest_number)



# def sum_even(num):
#     return sum(num for num in numbers if num%2==0)
# numbers=[]
# numbers.append(int(input()))
# print(sum_even(numbers))


# def palindrome(a):
#     return a == a[::-1]
# a = str(input())
# reversed= palindrome(a)
# if reversed==True:
#     print("yes")
# else:
#     print("no")

# def palindrome(a):
#     return a == a[::-1]
# print(palindrome("madam"))

# def count_vowels(a):
#     vowels = ["A","E","I","O","U","a","e","i","o","u"]
#     return sum(1 for char in a if char in vowels)

# a = str(input())
# char = count_vowels(a)
# print(char)


# def count_vowels(a):
#     vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
#     return sum(1 for char in a if char in vowels)
# a = input(" ")
# char = count_vowels(a)
# print(f"Number of vowels: {char}")

# def fibonacci(n):
#     fib_sequence = [0,1]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence
# n=10
# print(fibonacci(n))

# def fibbonacci(n):
#     fib = [0,1]
#     while len(fib)< n :
#         fib.append(fib[-1] + fib[-2])
#     return fib
# n = 10
# print(fibbonacci(n))

# def prime_num(num):
#     if num<= 1:
#         return False
#     for i in range(2,int(num%2)+1):
#         if num% i == 0 :
#             return False
#     return True
# a= int(input(""))
# print(prime_num(a))

# def prime_num(num):
#     if num<= 1:
#         return False
#     for i in range(2,(num-1)):
#         if num% i == 0 :
#             return False
#     return True
# a= int(input(""))
# print(prime_num(a))

# def factorial(n):
#     if n == 0 or n ==1 :
#         return 1 
#     return n * factorial(n-1)
# a = int(input(" "))
# print(factorial(a))

# def myfunction(numbers):
#     if len(numbers)<3:
#         return "this list must contain at least three numbers."
#     largest = max(numbers[0],numbers[1],numbers[2])
#     return largest
# numbers = []
# n = int(input())
# numbers.append(n)
# print(myfunction(numbers))
# def myfunction(numbers):
#     if len(numbers) < 3:
#         return "This list must contain at least three numbers."
#     largest = max(numbers[0], numbers[1], numbers[2])
#     return largest

# # Initialize an empty list
# numbers = []

# # Append three numbers to the list
# for i in range(3):
#     n = int(input(f"Enter number {i+1}: "))  # Ask the user to input three numbers
#     numbers.append(n)

# # Call the function and print the result
# print(myfunction(numbers))

# n= int(input())
# if n % 4==0:
#     print("its a leap year")
# else:
#     print("this is not a leap year")

# n = int(input("Enter a number: "))
# if n > 0 :
#     print("+ve number")
# elif n < 0 :
#     print("n is -ve number.")
# else:
#     print("n is zero")

# list1 = ["A","E","I","O","U","a","e","i","o","u"]
# char = str(input("enter an alphabet: "))

# if char in list1:
#     print(f"{char} is a vowel")
# else:
#     print(f"{char} is a consonant")

# n = int(input("enter a number: "))
# if n % 2 == 0:
#     print("even")
# else:
#     print("odd")

# n = int(input("Enter the number of lines: "))
# for i in range(1,n+1):
#     print('*'*i)

# def prime_num(n):
#     if n<= 1:
#         return False
#     for i in range(2,(n-1)):
#         if n % i == 0 :
#             return False
#     return True
# a= int(input(""))
# print(prime_num(a))

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# list1 =sorted(numbers)
# print(list1)
# print(numbers)

# n = int(input("number: "))
# if n % 3 == 0 and n % 5 == 0:
#     print(f"{n} is divisible by 3 and 5.")
# else:
#     print(f"{n} is not divisible by 3 and 5.")

# def smallest(a,b,c,d):
#     return min(a,b,c,d)
# a = int(input("number1: "))
# b = int(input("number2: "))
# c = int(input("number3: "))
# d = int(input("number4: "))
# print(f"the smallest number = {smallest(a,b,c,d)}")

# x = int(input("side 1: "))
# y = int(input("side 2: "))
# z = int(input("side 3: "))

# if x == y == z :
#     print("triangle is eqlateral")
# elif x == y or y == z or z == x:
#     print("isoceles")
# else:
#     print("scalene")

# age = int(input("age: "))
# if age >= 18:
#     print(f"{age} is legal age for voting")
# else:
#     print("not eligible")

# Using a for loop to print the first 10 natural numbers

# for i in range(1,11):
#     print(i , end=" ")


# n = 0
# for i in range(2,101,2):
#     n = n + i 
# print(f"the sum of all even numbers from 1 to 100 : {n}")

# num = int(input("factorial of "))
# factorial = 1
# for i in range(1 , num+1):
#     factorial = factorial*i
# print(f"the factorial of{num} is : {factorial}")

# num = int(input(" "))
# for i in range(1,11):
#     print(num*i)

# for i in range (1,51):
#     if i % 7 ==0:
#         print(i)


# list = []
# for i in range(1,11):
#     i = i*i
#     list. append(i)
# print(list)

# num1 = int(input(" "))
# num2 = int(input(" "))
# for i in range (num1,num2+1):
#     if i % 2 != 0 :
#         print(i)

# n = int(input(" "))
# for i in range (1,n+1):
#     print(i)


# n = int(input(" "))
# sum = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         # print(i,end = " ")
#         sum = sum + i 
# print(sum)

# n = int(input(" "))
# factorial = 1
# for i in range (1,n+1):
#     factorial = factorial* i
# print(factorial)

# name = ['Rishav','Nehal','Pratham']
# print(name[2])


# def myfunction(x):
#     x = x+1
#     return x
# a = 5
# b = myfunction(a)
# print(a,b)

# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
 
#     i += 1
# text = "Hello,World"
# result = [text[i]for i in range(len(text)) if i % 2 == 0 and text[i].isalpha()]
# print("".join(result))


# ist = [10,11,12]
# l = []
# for i in ist:
#     l.insert(0,i)
# print(l)

# number = 1234
# formated = f"{number:08}"
# print(formated)


# def test(i, j):
#     if i == 0:
#         return j
#     else:
#         return test(i - 1, i + j)
# # print(test(4, 7))
# i = 1
# while True:
#     if i % 2 == 0:
#         break
#     print(i)
#     i += 2


# a = [10, 23, 56, [78]]
# b = list(a)
# a[3][0] = 95
# a[1] = 34
# print(b)


# b=[2,3,4,5]
# a=list(filter(lambda x:x%2,b))
# print(a)

# a = 4.5
# b = 2
# print (a//b) 

# a = True
# b = False
# c = False
  
# if not a or b: 
#     print (1)
# elif not a or not b and c: 
#     print (2)
# elif not a or b or not b and a: 
#     print (3)
# else: 
#     print (4)


# def f(): x=4
# x=1
# f()
# print(x)

# def reverse_list(lst):
#     return lst [::-1]
# lst = [1,2,3,4,5]
# print(reverse_list(lst))

# n = int(input())
# factorial = 1
# for i in range(1,n+1):
#     factorial = factorial*i
# print(factorial)


# n = int(input())
# x = (n-32)*5/9
# print(x)

# n = int(input())
# armstrong = 0
# y = str(n)
# a = len(y)

# for i in y:
#     i = int(i)
#     i = i**a
#     armstrong= armstrong+int(i)

# print(armstrong)
    
# n = int(input())
# armstrong = 0
# y = str(n)
# a = len(y)
# for i in y:
#     m = int(i)
#     g = m**a
#     armstrong = armstrong+ int(g)
# print(armstrong)


# def prime_num(num):
#     if num<= 1:
#         return False
#     for i in range(2,(num-1)):
#         if num% i == 0 :
#             return False
#     return True
# a= int(input(""))
# print(prime_num(a))

# def prime(n):
#     if n<=1:
#         return False
#     for i in range(2,(n-1)):
#         if n % i == 0:
#             return False
#     return True
# a = int(input())
# print(prime(a))

# n = int(input())
# y = str(n)
# reverse = int(y[::-1])
# print(reverse)

# # Get the two input strings
# str1 = input("Enter the first string: ").lower()  # Remove spaces and convert to lowercase
# str2 = input("Enter the second string: ").lower()  # Remove spaces and convert to lowercase

# # print(str1)
# # print(str2)
# # Check if both strings have the same characters
# if sorted(str1) == sorted(str2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

# tuple = (1, 2, 2, 3, 4, 4, 5)
# set = set(tuple)
# list = list(set)
# print(list)

# s = "Hello, World!"
# start = 0
# end = 5
# substring = s[start:end]
# print(substring)

# num = 5  # Example number
# for i in range(1, 11):
#     print(f"{num} + {i} = {num + i}")

# n = int(input())
# y = int(str(n)[::-1])
# if n==y:
#     print(True)
# else:
#     print(False)

# n = int(input())
# for i in range(1,11):
#     print(n*i)

# n = int(input())
# prime = []
# for i in range(1,n-1):
#     if n % i == 0:
#         x = False
#     else:
#         x = True
# if x :
#     prime.append(n)

# print(prime)

# lst = [10, 23, 56, 34, 89]  # Example list
# largest = lst[0]
# for num in lst:
#     if num > largest:
#         largest = num

# print(largest)

# sample = str(input())
# ind = int(input())
# lst = []
# for i in sample.split():
#     lst.append(i[ind])
# result = ''.join(lst)
# print(str(result))

# donors = int(input())
# total = 0
# for i in range(donors):
#     donation = int(input())
#     total = total + donation
# print(total)

# num_donors = int(input("Enter the number of donors: "))
# total_amount = 0
# for _ in range(num_donors):
#     donation = int(input("Enter the donation amount: "))
#     total_amount += donation
# print("Total amount collected:", total_amount)

# for i in range (1,11):
#     if i % 4 == 0:
#         continue
#     print(i)

# n = int(input())
# for i in range(1,n+1):
#     print(i*'*')

n = int(input())
y = int(str(n)[::-1])
if (n)== (y):
    print(True)
else:
    print(False)


# var1 = 1
# var2 = 2
# var3 = "3"

# print(var1 + var2 + var3)
