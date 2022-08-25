# Doubt *
# if __name__ == '__main__':
# #     names_grades = []
#     names_grades = [[input(),float(input())] for i in range(int(input()))]
# #     names_grades = [['alka',43.4],['alja',33.3],['dkls',43.4],['rkdj',40.4],]
#     names_grades.sort()
#     second_min = names_grades[(names_grades.index(min(names_grades)))+1]
#     a,b = second_min
#     for i,j in names_grades:
#         if j==b:
#             print(i)

# Practice 1
# def func1(n1,*anshul) :
#      print(n1,"\n")
#      for i in cw:
#           print(i)
# cw = ["maths","science","Computer"]
# xz = "I am Anshul"
# func1(xz,*cw,"Axe")


# Practice 2
# nx = int(input("Enter your 1st number = "))
# def recursion(n):
#      if n<0 :
#           print ("oops")
#      elif n==0 :
#           return 0
#      elif n==1 :
#           return 1
#      else :
#           return (recursion(n-1)+recursion(n-2))
# print(recursion(nx))


# Practice 3
# how = int(input("How many no. you have for input : "))
# lst = []
# for i in range(how):
#      user = int(input("Enter no. : "))
#      lst.append(user)
# print(lst)
# even = 0
# odd = 0
# def func1(a):
#      for i in lst:
#           if i%2==0:
#                global even
#                even+=1
#           else:
#                global odd
#                odd+=1
#      return even,odd
# even,odd = func1(lst)
# print(f"Even : {even} and Odd : {odd}")


# Practice 4
# wish = int(input("How many no. you have for enter : "))
# lst = []
# for i in range(wish):
#     wish2 = int(input("Enter you number: "))
#     lst.append(wish2)
# odd, even = 0, 0

# def count():
#     for i in lst:
#         if i % 2 == 0:
#             global even
#             even += 1
#         else:
#             global odd
#             odd += 1
#     return even, odd
# count()
# print(f"Even:{even} and Odd:{odd}")

# Practice 4 - Revised
import os
re_lst = [23, 12, 22, 33, 0, 55]

# Practice 5


def fibb(x):
    lst = [0, 1]
    a = 0
    b = 1
    for i in range(2, x):
        c = a+b
        a, b = b, c
        lst.append(c)
    return lst

# st = fibb(10)
# lst2 = []
# for i in st:
#      if i<len(st):
#           lst2.append(i)
# print(lst2)

# Practice 5A


def fib(n):
    lst = [0, 1]
    a = 0
    b = 1
    for i in range(2, n):
        c = a+b
        lst.append(c)
        a = b
        b = c
    return lst

# main = fib(10)
# lstt=[]
# for i in main:
#      if i < len(main):
#           lstt.append(i)
# print(lstt[-1])

# Practice 6 - map, filter, reduce
# numbers = [2,4,23,45,65,4,44,67,87]
# print('\nThe numbers are',numbers)

# odds = list(filter(lambda a:a%2!=0, numbers))
# print('\nAfter filter the odd numbers',odds)

# doubles_of_numbers = list(map(lambda a:a*2, numbers))
# print('\nDoubles of the numbers are',doubles_of_numbers)

# import reduce
# others = list(reduce(lambda a,b: a+b, numbers))

# Practice 7

# def cube(a=2):
#      # if n==0 or n=='':
#      #      print(2*2*2)
#      # else:
#      #      print(a*a*a)
#      print(a*a*a)
# # n = int(input('Enter your number: '))
# cube(5)

# Practice 8 HackerRank
# def check(a,b):
#      x,y=len(a),len(b)
#      if x==y:
#           print(True)
#      else :
#           print(False)
# check('Anshul','Akansha')


# practice 8A
# def is_leap(year):
#     leap = False
#     if year%400==0 or (year%4==0 and year%100!=0) :
#         return not leap
#     else:
#         return leap

# year = int(input('Enter year:'))
# print(is_leap(year))

# practice 8B  #list comprehension
# x = int(input('x:'))
# y = int(input('y:'))
# z = int(input('z:'))
# n = int(input('n:'))
# l = []
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if (i+j+k != n):
#                 l.append([i, j, k])
# print(l)

#     # l=[[i,j,k] for i,j,k in range(x+1,y+1,z+1) if (i+j+k!=n)]
#     l=[(i,j,k) for i in range(x+1) for j in range(y+1)
#     for k in range(z+1) if (i+j+k!=n)]
#     print(l)

# practice 8c
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     l=list(arr)
#     l.sort()
#     a=set(l)
#     b=list(a)
#     print(b[-2])
#     print(b)


# practice 8d  #nested list..
# if __name__ == '__main__':
#     names_grades = []
#     scores = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         names_grades.append([name,score])
#         scores.append(score)
#     # names_grades = [['alka',43.4],['alja',33.3],['dkls',43.4],['rkdj',40.4],]
#     # scores = [43.4,33.3,43.4,401.4]
#     a = set(scores)
#     f_min = min(a)
#     # print(f_min,'ansh')
#     a.remove(f_min)
#     s_min = min(a)
#     # print('sjddjd',s_min)
#     names_grades.sort()
#     for i,j in names_grades:
#         if j==s_min:
#             print(i)

# practice 9 #fibonacci term wit recursion
# fib_cache ={}
# def fib(n):
#      if n in fib_cache:
#           return fib_cache[n]
#      #Compute the nth term
#      if n == 1:
#           v = 1
#      elif n == 2:
#           v=1
#      elif n>2:
#           v = fib(n-1)+fib(n-2)
#      # cache the value and retun it
#      fib_cache[n]= v
#      return v
# # for n in range(1,111):
# print(fib(9))

# practice 10 # find second minimum no.
# lst = [1,3,34,-1,-5,2,4]
# set(lst)
# lst.sort()
# lst.remove(min(lst))
# second_minimum = min(lst)
# print(second_minimum)

# practice 11  #swap case
# def swap_case(s):
#      a = ''
#      for i in s:
#         if i.isupper():
#           x=i.lower()
#         else:
#           x=i.upper()
#         a+=''.join(x)
#      return a
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

# practice 11a == doubt -> why this show false for input (q2A)
# s=input('-->')
# print(True) if s.isalnum() else print(False)
# print(True) if s.isalpha() else print(False)
# print(True) if s.isdigit() else print(False)
# print(True) if s.islower() else print(False)
# print(True) if s.isupper() else print(False)


# os.chdir("Python")
# currDir = os.getcwd()
# work = os.listdir(currDir)

# for file in work:
#     if "#me" in file:
#         new_name = file.replace(" #me", '').replace(" #loop", "")
#         the = open(file)
#         print(the.name)
#         the.close()

columbs, rows = 27, 5

# columbs = rows**2-rows
for i in range(rows):
    cen = i*2+1
    print(str('.|.'*cen).center(columbs, '-'))
print('WELCOME'.center(columbs, '-'))
for i in range(rows-1, -1, -1):
    cen = i*2+1
    print(str('.|.'*cen).center(columbs, '-'))
print()

mid = rows//2+1
print(mid)
for i in range(mid):
    cen = i*2+1
    print(str('.|.'*cen).center(columbs, '-'))
print('WELCOME'.center(columbs, '-'))
for i in reversed(range(mid)):
    cen = i*2+1
    print(str('.|.'*cen).center(columbs, '-'))
