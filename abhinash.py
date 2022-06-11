
# for i in range(4):
#     user_name = input('enter the username : ')
#     pass_word = input('enter the password: ')
#     if user_name == 'nepal123' and pass_word == 'mount everest':
#         print('congratulation ')
#         break
#     else:
#         print(" try again ☹️" )



# def sum(numbers):


# total = 1
# for x in numbers:
#     total *= x
# return total
# print(sum(8, 2, 3, 0, 7))


# def sum(numbers):
#     total = 1
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))



# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# n3 = int(input("Enter Third number: "))
# def f():
#     if(n1 >= n2) and (n1 >= n3):
#       l = n1
#     elif(n2 >= n1) and (n2 >= n3):
#         l = n2
#     else:
#         l = n3
#     print("Largest number among  the three is", l)


# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)
	

# def demo(name, age):
#     print(name, age)
# demo("Ben", 25)




# n1=int(input("Enter first number: "));
# n2=int(input("Enter second number: "));
# n3=int(input("Enter Third number: "));
# def f():
#     if(n1>=n2) and (n1>=n3):
#         l=n1
#     elif(n2>=n1) and (n2>=n3):
#          l=n2
#     else:
#          l=n3
#     print("Largest number among  the three is",l)
# f()



# list1 = [1,2,3,4,5,6]
# for num in list1:
# 	if num % 2 == 0:
# 		print(num, end=" ")


# #ODD NUM
# list1 = [1,2,3,4,5,6]
# for num in list1:
# 	if num % 2 != 0:
# 	   print(num, end = " ")


# # prime or not

# num = 11
# if num > 1:
# 	for i in range(2, int(num/2)+1):
# 		if (num % i) == 0:
# 			print(num, "is not a prime number")
# 			break
# 	else:
# 		print(num, "is a prime number")
# else:
# 	print(num, "is not a prime number")
      



# def reverse(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse(s[1:]) + s[0]
  
# s = "Geeksforgeeks"
  
# print ("The original string  is : ",end="")
# print (s)
  
# print ("The reversed string(using recursion) is : ",end="")
# print (reverse(s))




# def func(employee, salary=8000):
#     print('employee: ', employee )
#     print('Salary: ', salary)

# func('dipes', 3000)
# func('subash')




# a = [4, 6, 8, 24, 12, 2]
# max(a)

# a = [4, 6, 8, 24, 12, 2]
# min(a)

# def detail(roll):
#     x=[1,2,3,4,5,6,7]
#     if roll in x:
#         print(f"roll number is{roll}is present")
#     else:
#         print(f"roll number{roll}is absent")
# roll=int(input("enter roll no."))
# detail(roll)
    

# str1 = input("Please Enter Your Own String : ")
# vowels = 0
# consonants = 0
# str1.lower()
# for i in str1:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1
# print("Total Number of Vowels in this String = ", vowels)
# print("Total Number of Consonants in this String = ", consonants)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# n=int(input("Input a number to compute the factiorial : "))
# print(factorial(n))

# 21 no ayena 

# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))