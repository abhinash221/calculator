

# # amt = int(input("what is the principal amount?: "))
# # rate = float(input("what is the rate?: "))
# # rate = rate/100
# # years = float(input("what is the number of years?: "))
# # num_times = float(input("what is the number of times the interest is compounded per year?: "))

# # #breaking down the simple interest formula
# # # b = 1 + (rate/num_times)
# # # c = num_times * years
# # # A = amt * ((b)**c)
# # A = amt*(1+(rate/num_times))**(num_times*years)

# # #A = int(A)

# # print(f"The compound interest of {amt} at {rate}% in {years} years compounded {num_times} times is {A:.2f}")

# # print("Welcome To Compound Interest Calculator")
# # print("---------------------------------------")






# # def cal(a,b):
# #     add = a+b
# #     sub= a-b
# #     mul = a*b
# #     div = a/b
# #     return add, sub , mul,div
# # print(cal(3,4))






# # def com(a,b,c):
# #     if a>b and a>c:
# #         return a 
# #     elif b>c and b>a:
# #         return b
# #     else:
# #      return c

# # a = int(input('a'))
# # b = int(input("b"))
# # c = int(input("c"))
# # print(com(a,b,c))


# # def d(a,b):
# #     sum = a+b
# #     return sum
# # print(d(3,4))



# # def greeter(name):
# #     print('gm')
# #     print('hello'+str(name))
# # print("go")
# # greeter('world')


# # def inner():
# #     x=5
# #     print(x)
# # inner()




# # x = 10
# # def outer():
# #     x=4
# #     def inner():
# #         x = 8
# #         print(x)
# #         inner()
# # outer()


# # def outer ():
# #     x="local"
# #     def inner():
# #         nonlocal x
# #         x ="non local"
# #         print('inner:',x)
# #     inner()
# #     print("outer:",x)
# # outer()


# # result = lambda n1,n2,n3,:n1*n2+n3
# # print("sum of three vaules:", result(10,20 ,30))




# # We double all numbers using map()
# # numbers = (1, 2, 3, 4)
# # result = map(lambda n : n*n , numbers)
# # print(list(result))


# # from functools  import reduce
# # li = [12,3,4,5,5,5,6]
# # sum = reduce((lambda x,y:x+y),li)
# # print(sum)


# # data = {1,2,3,4}
# # # data.add(5)
# # # print(data)
# # data.remove(1)
# # print(data)

# # a = {"lemon","cat","dog"}
# # a.discard("lemon")
# # print(a)

# # data  = {1,2,3,4,5,6,"ram"}
# # if"ram" in data:
# #     print('hey')
# # else:
# #     print('may')



# # d1 = {1,2,3,4,5,6}
# # print(d1)
# # d2 = d1.copy()
# # print(d2)

# # x= {1,2,3,4,5}
# # y = {2,3,4,6,7}
# # x.update(y)
# # print(x)

# my_dict ={}
# my_dict={1:"apple",2:"ball"}
# my_dict ={"name":"john",1:[2,3,4]}
# my_dict = dict({1:"apple",2:"ball"})
# my_dict = dict([1,"apple",(2,"ball")])
# print(my_dict)





a ={"name":"abhinash","age":20}
# del a['age']
print(a)
remove_pop = a.pop('age')
print(remove_pop)
