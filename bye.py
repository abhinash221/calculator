# # # # from sys import float_repr_style


# # # y=100
# # # z=0o215
# # # u=0x12d
# # # float_1=100.5
# # # float_2=1.5e2
# # # a=5+3.14
# # # print(y,z,u)
# # # print(float_1,float_2)
# # # print(a,a.imag,a.real)
# # # x=(1==True)
# # # y=(2==True)
# # # z=(3==True)
# # # a=True+10
# # # b=False+10
# # # print("x is",x)
# # # print ("studytonight")
# # # print("is awesome")
# # # a = '20'
# # # b = '30'
# # # c = a+b
# # # print(c)

# # #print("Hello{0}, you are a {a}, becAUSE YOUR balance is {B}.".format(" Abhinash", a= "god ", B = '1Billion trillion hajar crore '))


# # # name = "pAShon"
# # # print(name)
# # # print(name.casefold())

# # # n = "python is a programming language"
# # # print(n)
# # # print(n.title())

# # # a = "python"
# # # b = [10,20,30]
# # # c = (10,20,30,40)
# # # d = {10,20,30,40,50}
# # # e = {101:'sunil',102:'raj',103:'suman'}
# # # f = [[10,20],[30,40],[60,70]]
# # # print(len(a))
# # # print(len(b))

# # # gender = input("Enter your gender")
# # # gender = gender.lower()
# # # if gender == "male":
# # #     print("You are male")
# # # elif gender =="female":
# # #     print ('you are beautiful ')
# # # else:
# # #     print('you are  cute ')



# # # gender = input("Enter character: ")
# # # gender = gender.lower()
# # # if gender == "a"or"e"or"i"or"o"or"u":
# # #     print("You vowel")
# # # else:
# # #     print('you are  consonant ')



# # a  = input ('enter a day')
# # a=int(a)
# # if a == 1:
# #     print('JANUARAY')
# # elif a == 2:
# #  print ('FEB')
# # elif a == 3:
# #     print('MARCH')
# # elif a == 4:
# #  print ('APRIL')
# # elif a == 5:
# #     print('MAY')
# # elif a == 6:
# #  print ('JUNE')
# # else:
# #      print( 'shut up')

# # a = input('enter a num')
# # a = int(a)
# # if a%2== 0:
# #      print("even")
# # else:
# #      print('odd')


# a = input('enter a num')
# a = int(a)
# if a>0:
#     print('positve')
# else:
#     print('negative')

# import pdb
# bike1  = "yahama"
# bike1_price = 25000

# bike2 = "honda"
# bike2_price = 40000
# pdb.set_trace()
# name = input("enter your name")
# choose = int(input('press 1 fir yamaha and 2 for honda'))
# print(f'hello(name)')

# if choose== 1:
#     print(f'{bike1}will cost you {bike_price}')
# elif choose== 2:
#     print(f'{bike2 +2000} will cost you {bike2_price}')
# else:
#     print('press only 1 or 2 ')

# for i in range(78):
#      print("Abhinash tripathi is a legend")


# a = 'gari'
# for i in range(2):
#      print(a)


# a='abhinash'
# for i in a: 
#     print(i)

# for i in range (0,51):
#     print(i)




# a = 'python'
# for i in range(6) :
#     print(i,"=",a[i])
# else:
# print("Hello Python")



# num = 2
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)

# num = 2
# for i in range(10,1,-1):
#    print(num, 'x', i, '=', num*i)

# st = "Programming"
# for i in st:
#     print(i)
# else:
#     print("Else part")    

# a = "hari"
# b = ""
# for i in a:
#     b = i+ b
# print(b)

# for i in range(3):
#     user_name = input('enter the id: ')
#     pass_word = input('enter the password: ')
#     if user_name == 'car' and pass_word == 'bus':
#         print('welcome')
#         break
#     else:
#         print('get lost ')


# a = ["hari ", "shayam" , "chor"]
# for i in reversed(a):
#    print(i)



# a = [1,2,3]
# b= []
# for i in reversed(a):
#     b.append(i)
# print(b)

# a = [1,2,3,4]
# b = 1
# for i in a:
#     b = b*i
# print(b)


# a = int(input("enter the num"))
# for i in range (2,a):
#     if a%2 == 0:
#         print('composite')
#         break
# else:
#     print('prime')


# for i in range(2):

#     for j in range(3):
#         print('inner loop',j)
#         print('outer loop',i)

# a="*"
# for i in range(5):
#     for j in range(5):
#         print(a,end="")
#     print()


# a="*"
# for i in range(6):
#     for j in range(i):
#         print(a,end="")
#     print()


# print()
# a="*"
# for i in range(6):
#     for j in range(6-i):
#         print(a,end="")
#     print()