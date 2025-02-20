# price1 = int(input("Enter the price of the first laptop: "))
# price2 = int(input("Enter the price of the second laptop: "))
# price3 = int(input("Enter the price of the third laptop: "))
# budget = int(input("Enter your budget: "))


# if budget==price1:
#     print("laptop 1 is in budget")
# elif budget==price2:
#     print("laptop two is in budget")
# elif budget==price3:
#     print("laptop3 is in budget")
# else:
#     print("nothing is in budget")


# price1 = int(input("Enter the price of the first laptop: "))
# price2 = int(input("Enter the price of the second laptop: "))
# price3 = int(input("Enter the price of the third laptop: "))
# budget = int(input("Enter your budget: "))


# multiplication of any table:
# number=int(input("add a number for multiplication table: "))
# for i in range(1,11):
#     print(f"{(number)}*{i}={number*i}")


# for i in range(1,11):
#     if i%4 ==0:
#         continue
#     print(i)

# rows=int(input("number of rows: "))
# for i in range(1,rows+1):
#     print('*'*i)


# PALINDROME
# def is_palindrome(number):
#     original_number=number
#     reversed_number=0
#     while number>0:
#         digit=number%10
#         reversed_number=reversed_number*10 + digit
#         number=number//10
#         if original_number==reversed_number:
#             return "palindrome"
#         else:
#             return "not a palindrome"
# number= int(input("enter the number to check: "))
# print(is_palindrome(number))
          



# def is_palindrome(number):
#     original_number = number
#     reversed_number = 0
#     while number > 0:
#         digit = number % 10
#         reversed_number = reversed_number * 10 + digit
#         number = number // 10

#     if original_number == reversed_number:
#         return "Palindrome"
#     else:
#         return "Not a Palindrome"
# number = int(input("Enter the number to check: "))
# print(is_palindrome(number))


# marks_sum = 0
# marks_count = 0

# while True:
#     mark = input("Enter a mark (or 'n' to stop): ")
#     if mark.lower() == 'n':
#         break
#     try:
#         mark = float(mark)
#         marks_sum += mark
#         marks_count += 1
#     except ValueError:
#         print("Invalid input. Please enter a number or 'n' to stop.")

# if marks_count > 0:
#     average_mark = marks_sum / marks_count
#     print(f"Average mark: {average_mark:.2f}")
# else:
#    ( print("No marks entered.")

# num = int(input("enter a number"))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"The factorial of {num} is {factorial}")`


# price1 = int(input("Enter the price of the first laptop: "))
# price2 = int(input("Enter the price of the second laptop: "))
# price3 = int(input("Enter the price of the third laptop: "))
# budget = int(input("Enter your budget: "))
# if budget>price1:
#     print("laptop 1 is in budget")
# if budget > price2:
#     print("laptop two is also in budget")
# if budget > price3:
#     print("laptop 1 n 2 and 3 all are in budget.")

# sum = 0
# n = int(input())
# for i in range(n+1):
#     sum = sum+ i 
# print(sum)
# n = int(input()) 
# digits = 0
# for i in range(n+1):
#     digits = digits + i
# print(digits)
# n =int(input())
# factorial = 1
# for i in range (1,n+1):
#     factorial = factorial*i
# print(factorial)

# def palindrome(n):
#     n == n[::-1]
# n = str(input())
# reversed = palindrome(n)
# if reversed == True:
#     print(n,"is a palindrome.")
# else:
#     print(f"{n} is not a palindrome.")

# def prime(n):
#     if n<=1:
#         return False
#     for i in range(2,(n-1)):
#         if n % i == 0:
#             return False
#     return True
# a = int(input(" "))
# print(prime(a))

