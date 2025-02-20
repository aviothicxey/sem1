# age=23
# old=False
# a=None
# print(type(old))
# print(type(a))
# a=2
# b=5
# sum= a+b 
# print(sum) 
# a=5
# b=2

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)  
#range(start,stop,step)
# list components- max, min, length
# outer for loop
# for i in range(1,11):
#     for j in range(1,11):
#           print(i*j,end=" ")
#           print('')
# i=1
# while(i<=5):
#     j=5
#     while(j>i-1):
#         print(j, end='     ')
#         j=j-1
#     i=i+1
#     print()
# for i in range (1,6):
#     for j in range(i):
#         print(i,end='  ')
#     print()
# colors = ['red','green','blue']
# for x in colors:
#     print(x)
# start-optional
# stop - required
# step-optional
# for i in range(2,20,2):
#     print(i)
# num=int(input("enter the number: "))
# if(num==0):
#     fact=1
# fact=1
# for i in range(1,num+i):
#     fact=fact*i
#     print("factorial of",num,"is",fact)
# pass statement:
# for letter in 'python':
#     if letter =="h":
#         break
#         print("this is a pass block")
#     print("current letter:",letter)
# for letter in 'Python':
#    if letter == 'h':
#       continue
#       print ('This is pass block')
#    print ('Current Letter :', letter)
# The multiple loops are used to print the patterns where the first outer loop is used to print the 
# number of rows, and the inner loop is used to print the number of columns.
# n = int(input("Enter the number of rows: "))
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("* ", end="")
#     print()
# rows = int(input("Enter the number of rows:"))   
# k = 2* rows-2       
# for i in range(0, rows):    
#     for j in range(0, k):    
#         print(end=" ")    
#     k = k - 2           
#     for j in range(0, i + 1):    
#         print("* ", end="")   
#     print('')
# rows = int(input("Enter the number of rows: "))
# k = rows - 2
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print()
# k = 2 * rows - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print()
# def function name([comma seperated list of parameters]):
# statements...
# statements...
# user defined funtion csn be:
# 1)function with no argumentsand no return value.this type of funtion is known as void funtion
# function with parameters but no return values
# parameters are given in parenthesis seprrerated by comma
# values are passed for the parameter at the time of function calling
# def square(num):
#     return num**2
# print(square(5))
# print(square(225))
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))
# a="hello"
# b="world"
# print(a + b)
# tuples_list=[(1,3),(2,1),(4,5),(3,2)]
# sorted_list =sorted(tuples_list, key=lambda x:x[1])
# print("sorted list:",sorted_list)
# import random
# random_number=random.randint(1,100)
# print(random_number)
# def guess_number(guess):
#     if guess < random_number:
#         return "number was too low:"
#     elif guess > random_number:
#         return "number was too high:"
#     else:
#         return "correct! the guessed number is equal with random number:"+str(random_number)
        
# guess = int(input("enter your guess:"))        
# print(guess_number(guess))
# Function to modify a list
# def modify_list(my_list):
#     print("List inside function before modification:", my_list)
#     my_list.append(100)  # Modify the list by adding an element
#     print("List inside function after modification:", my_list)

# # Original list
# original_list = [1, 2, 3]

# # Call the function and pass the list
# print("Original list before function call:", original_list)
# modify_list(original_list)
# print("Original list after function call:", original_list)
# x=5
# y=6.5
# z=3.00
# print(type(x))
# print(type(y))
# print(type(z))
# for x in "aparna":
#     print(x)
# abc="The way to get started is to quit talking and begin doing."
# if "free" in "abc":
#     print('yes ! "free" is in the test')
# else:
#     print('no ! wrong word...')    
# a="hello world"
# print(a.upper())
# a="hello world"
# print(a.lower())
# a = "Hello, World!"
# print(a.replace("e","f"))
# a=input("ENTER A NUMBER A:")
# b=input("ENTER A NUMBER B:")
# if a>b:
#     print(a>b)
# else:
#     print(b>a)    
# def val(x):
#     x=15
#     print(x,'and id: ',id(x))
# x=10
# val(x)
# print(x,'ans id: ',id(x))
# def val(ist):
#     ist.append(4)
#     print(ist,'and id: ',id(ist))
# ist={1,2,3}
# print(ist,'ans id, ',id(ist))
# val(ist)
# def factorial(x):
#     if x == 1:
#          return 1
#     else:
#         return(x* factorial(x-1))
# num=3
# print("factorial of")
# x=lambda a,b:a+10*b
# print("result",x(5,6))
# import random
# def guess_the_number():
#     random_number = random.randint(1,100)
#     attempts = 0

#     print("welcome to the guess the number game from 1 to 100")
#     while True:
#         user_guess=int(input("enter your guess: "))
#         attempts += 1
#         if user_guess<random_number:
#             print("too low try again")
#         elif user_guess>random_number:
#             print("too high try again")
#         else:
#             print(f"congrats you have guessed the number in (attempts)attempts,")
#             break
# guess_the_number()
# a=int(input("type a number1 "))
# b=int(input("type a number1 "))
# if a>b :
#     print("a is greater than b")
# else:
#     print("a is smaller than b")

# mylist=[1,2,3,4,5,6]
# print(mylist[:4])
# print(mylist[2:])
# print(mylist[2:4])
# print(mylist[:])
# mylist=[1,2,3,4,5,6]
# print(mylist)
# mylist.reverse()
# print(mylist)


# mylist=["apple,banana,guava"]
# print(mylist)
# mylist.reverse()
# print(mylist)

# mylist=[1,2,3,4,5,6,5,6,4]
# print(mylist)
# mylist.sort()
# print(mylist)


# mylist=["apple,banana,guava"]
# print(mylist)
# mylist.sort()
# print(mylist)


# mylist=["a,b,c,d,e,f"]
# print(mylist)
# mylist.sort()
# print(mylist)

# mylist=[1,2,3,5,4,7,6]
# print(mylist)
# print(mylist.count(3))

# numbers = [1,2,3,4,5]
# doubled_numbers = [number * 2 for number in numbers]
# print (doubled_numbers)

# numbers = [1,2,3,4,5]
# squares = [number ** 2 for number in numbers]
# print (squares)


# even_numbers= [num for num in range(1,10)if num %2 == 0]
# print(even_numbers)

# function to double the value od numbers:
# def double(n):
#     return n *2
# numbers = [5,6,7,8]
# result = map(double,numbers)
# print(list(result))

# function to square the value of numbers:
# def square(n):
#     return n**2
# numbers=[3,4,5,6,7]
# result = map(square,numbers)
# print(list(result))


# def multiply_numbers(given_numbers):
#     return given_numbers * 3
# given_numbers= map (multiply_numbers,[1,3,5,2,6,10])
# print("multipling list elements with 3: ")
# for elements in given_numbers:
#     print(elements , end=" , ")

# strings = ["1","2","3","4","5"]
# numbers = list(map(int,strings))
# print(numbers)


# strings = ["1","2","3","4","5"]
# numbers = list(map(float,strings))
# print(numbers)


# numbers=[23,45,67,12,89,38,55]
# numbers_greater_than_50= list(filter(lambda x : x> 50 , numbers))
# print("Numbers grester than 50: " , numbers_greater_than_50)


# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for row in matrix:
#     print(row)


# matrix = []
# for i in range (2):
#     row = []
#     for j in range(2):
#         value = int(input(f"enter the value for element [{i},{j}]: "))
#         row.append(value)
#     matrix.append(row)
#     print("the 2d list(matrix)is : ")
#     for row in matrix:
#         print(row)

# def find_max(list1):
#      return max(max(row)for row in list1)
# def find_min(list1):
#     return min(min(row)for row in list1)
# list1= [
#      [1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]
# ]
# maximun_number=find_max(list1)
# print("the maximum number in 2D list is: ",maximun_number)
# minimum_number=find_min(list1)
# print("the minimum number in 2D list is: ",minimum_number)


# def find_max(list1):
#     return max(max(row) for row in list1)
# def find_min(list1):
#     return min(min(row) for row in list1)
# # Example usage
# list1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# maximum_number = find_max(list1)
# print("The maximum number in the 2D list is:", maximum_number)
# minimum_number = find_min(list1)
# print("The maximum number in the 2D list is:", minimum_number)

# jagged_list = [
#     [10, 20, 30],
#     [40, 50],
#     [60, 70, 80, 90]
# ]

# # Accessing specific elements
# print("Element at row 0, col 2:", jagged_list[0][2])  # Output: 30
# print("Element at row 1, col 1:", jagged_list[1][1])  # Output: 50
# print("Element at row 2, col 3:", jagged_list[2][3])  # Output: 90

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6],
#     [7, 8, 9],
#     [10, 11, 12, 13]
# ]
# total_sum = 0
# # Calculate the sum of all elements
# for row in matrix:
#     total_sum += sum(row)
# print("Total sum of all elements:", total_sum)


# import random
# n=random.sample(range(50,100),5)
# print(n)


# my_string = 'Hello, Students!'
# print("String 1:",my_string)
# my_string = "He is 'Rohit'"
# print("String 2:",my_string)
# my_string = '''Hello,
#                World!'''
# print("String 3:",my_string)

# my_string = "Hello, World!"
# print(my_string[0])
# print(my_string[7])
# print(my_string[-2])

# str = "Hello"
# str1 = "world"
# print(str*3)
# print(str+str1)
# print(str[4])
# print(str[2:4])
# print('w' in str)
# print('wo' not in str1)
  
# my_string = "Hello, World!"
# list1 = list(my_string)
# list1[2] = 'p'
# my_string2 = ''.join(list1)
# print(my_string2)

# a=0
# b=1
# for i in range(0,11,1):
#     c=a+b
#     a=b
#     b=c
#     print(c)
  
# def function():  
#     series = [0, 1]
#     for i in range(0, 10): 
#         a = series[-1] + series[-2]  
#         series.append(a)  
#     return series 
# print(function())

# x = tuple(["Rohit", 35, 1.75, "Mumbai"])
# print(x)
# y = tuple("Python")
# print(y)
# z = tuple({12,15,18,25,50})
# print(z)

# my_tuple = ("Apple",)
# print(type(my_tuple))
# #NOT a tuple
# my_tuple = ("Apple")
# print(type(my_tuple))

# my_tuple=('P','r','o','g','r','a','m','m','i','n','g')
# print(my_tuple[1:6])
# print(my_tuple[5:])
# print(my_tuple[:4])
# print(my_tuple[::-2])

# my_tuple = (10, 20, 35, 40, 50)
# print(my_tuple)
# x = list(my_tuple)
# x[2] = 30
# my_tuple = tuple(x)
# print(my_tuple)

# my_tuple = (10, 20, 35, 40, 50)
# print(my_tuple)
# x = list(my_tuple)
# x.append(60)
# my_tuple = tuple(x)
# print(my_tuple)

# my_tuple = (10, 20, 30, 40)
# x = (50, 60, 70, 80)
# my_tuple = my_tuple + x
# print(my_tuple)
# my_tuple1= x + my_tuple
# print(my_tuple1)

# my_tuple = (10, 20, 30, 35, 40, 50)
# x = list(my_tuple)
# x.remove(35)
# my_tuple = tuple(x)
# print(my_tuple)

# my_tuple = (10, 20, 30, 40, 50)
# for x in my_tuple:
#   print(x)
# #By index number;
# for i in range(len(my_tuple)):
#     print(my_tuple[i])

# my_tuple = (1, 3, 7, 5, 7, 5, 4, 6, 8, 5)
# x = my_tuple.count(5)
# print(x)
# my_tuple = (1, 3, 7, 5, 7, 5, 4, 6, 8, 5)
# x = my_tuple.index(5)
# print(x)

# price= int(input("enter the price: "))
# function=f"the price is {price} dollars"
# print(function)

# price= int(input("enter the price: "))
# function=f"the price is {price:.3f} dollars"
# print(function)

# price= int(input("enter the price: "))

# tax= int(input("enter the tax: "))
# function=f"the price is {price+(price*tax)} dollars"
# print(function)

# price= int(input("enter the price: "))
# function=f"the price is {'expensive'if price> 50 else 'cheap'} "
# print(function)

# fruit=str(input("Name a Fruit: "))
# txt=f"i love {fruit.upper()}"
# print(txt)

# def myfunction(x):
#     return x*0.3048

# hey=f"the plane is flying at a {myfunction(500)} meter altitude"
# print(hey)

# price = 590000000
# txt = f"The price is {price:,} dollars"
# print(txt)

# format()
# price=int(input("enter the price: "))
# txt="the price is {} dollars"
# print(txt.format(price))

# quatity = int(input("quantity of items: "))
# items = int(input("price of each item: "))
# total_price =quatity*items
# myorder="i want{} pieces of item {} for {:.2f}dollars."
# print(myorder.format(quatity,items,total_price))

# age = 36
# name = "John"
# txt = "His name is {}. {} is {} years old."
# print(txt.format(name,name,age))

# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = str(input("car name: ")), model = str(input("model number: "))))


# extend example:
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# tropical.extend(thislist)
# print(tropical)

# thislist = ["apple", "banana", "cherry"]
# i=0
# while i < len(thislist):
#     print(thislist[i])
#     i = i + 1

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[]
# for x in fruits:
#     if"n"in x:
#         newlist.append(x)
#         print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist=[x if x!="banana"else "orange"for x in fruits]
# print(newlist)


# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse=True)
# print(thislist)

# def myfunction(n):
#     return abs(n-50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key =myfunction)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#     list1.append(x)
#     print(list1)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# thistuple = ("apple", "banana", "cherry")
# print(len(thistuple))


# thistuple=("apple",)
# print(type(thistuple))

# thistuple = ("apple", "banana", "cherry")
# if "apple"in thistuple:
#     print("yes,'apple' is in the fruit tuple")

# thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# y[1] ="kiwi"
# thistuple=tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# y.append("kiwi")
# thistuple=tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y=list(thistuple)
# y.insert(1,"kiwi")
# thistuple=tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y=(100, 50, 65, 82, 23)
# thistuple = thistuple + y
# print(thistuple)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# print(green)
# print(tropic)
# print(red)

# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
#   print(thistuple[i])

# thistuple = ("apple", "banana", "cherry")
# i = 0
# while i < len(thistuple):
#   print(thistuple[i])
#   i = i + 1

# a= int(input("enter the value of a : "))
# b=int(input("enter the value of b : "))
# if b > a:
#     print("b is greater than a")
# elif a > b :
#     print("a is greater than b")
# else:
#     print("a is equal to b and b is equal to a")

# i=1
# while i <6:
#     print(i)
#     if i == 3:
#         break
#     i= i + 1

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# def myfunction(x,y,z):
#     myfunction= max(x,y,z)
#     return myfunction

# x=float(input("Enter the number 1:"))
# y=float(input("Enter the number 2:"))
# z=float(input("Enter the number 3:"))

# greatest = myfunction(x,y,z)
# print("greatest number is:", greatest)


