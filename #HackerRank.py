# rows,columbs = map(int,input().split())
# rows, columbs = 6, 27
# middle = rows//2+1
# for i in range(1,middle):
#     #calculate number of .|. required and multiply with .|.
#     cen = (i*2-1)*".|."
#     print(cen.center(27,"-"))
# print("WELCOME".center(27,"-"))
# for i in reversed(range(1,middle)):
#     cen = (i*2-1)*".|."
#     print(cen.center(27,'-'))



# def print_rangoli(size):
#     import string
#     alpha = string.ascii_lowercase
#     L = []
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print('\n'.join(L[:0:-1]+L))

# if __name__ == '__main__':
#     # n = int(input())
#     n = 5
#     print_rangoli(5)

# ------------------------------------------------------------------
# ------------------------------------------------------------------

# import string
# alpha = string.ascii_lowercase
# n = 5
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     # L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     L.append((s[::-1]+s[1:]))
#     # L.append(s)
#     print(L)

# from itertools import combinations
# a,b = input().split()
# b = int(b)
# a,b = "HACK",2
# a = ''.join(sorted(a))
# new_b = b   # b=2
# b=1
# for z in range(new_b):
#     X = (list(combinations(a,b)))
#     if b<=new_b:
#         # X =  (list(combinations(a,b)))
#         X.sort()
#         for i in X:
#             for j in i:
#                 print(j,end="")
#             print()
#         b+=1
#     else:
#         break

# from collections import defaultdict
# d = defaultdict(list)
# list1 = []
# m,n = map(int,input().split())
# for i in range(m):
#     a = input()
#     d[a].append(i+1)
# for i in range(n):
#     b = input()
#     list1 = list1 + [b]
# for i in list1:
#     if i in d:
#         print(' '.join(map(str,d[i])))
#     else:
#         print("-1")

# ----> INPUT :
# 5 2
# a
# a
# b
# a
# b
# a
# b
