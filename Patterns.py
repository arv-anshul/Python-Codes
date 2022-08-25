# Patterns Project

# for i in range(5):
#     for j in range(i+1):
#         print(i+1, end=" ")
#     print()
# for i in range(5, 1, -1):
#     for j in range(i-1):
#         print(i-1, end=" ")
#     print()

# ===================================
# rows = int(input("Enter the number of rows:"))
rows = 6

""" Makes a diamond shape pattern. """
# k = rows-1                   # It is used for number of spaces
# for i in range(rows):
#     for j in range(k):
#         print(end=" ")
#     k = k - 1                      # decrement k value after each iteration
#     for j in range(i + 1):
#         print(j+1, end=" ")        # printing star/numbers
#     print()

# k = 0                              # It is used for number of spaces
# for i in range(0, rows):
#     for j in reversed(range(0, k)):
#         print(end=" ")
#     k = k + 1                      # decrement k value after each iteration
#     for j in range(rows-(i+0)):
#         print(j+1, end=" ")        # printing star/numbers
#     print()


# for i in range(rows):
#     for j in range(i + 1):
#         print(j+1, end=" ")
#     print()
# for i in range(rows-1):
#     for j in range(rows-(i+1)):
#         print(j+1, end=" ")
#     print()


# for i in range(5):
#     for i in range(rows):
#         for j in range(i+1):
#             print("*", end=" ")
#         print()
#     for i in range(rows-1):
#         for j in range(rows-(i+1)):
#             print("*", end=" ")
#         print()


# ------------------------------------------
initial, final = 1, 6
# for i in range(initial, final):
#     for j in range(i):
#         print(j+1, end=" ")
#     print()
# for i in range(final, initial, -1):
#     for j in range(i-2):
#     # for j in range(i-1):
#         print(j+1, end=" ")
#     print()


# ------------------------------------------
""" Makes a diamond shape pattern. """
rows = 6
k = rows-1
pattern = "*"
for i in range(rows):
    for x in range(k):
        print(end=" ")
    k -= 1
    for j in range(i+1):
        print(pattern, end=" ")
    print()
# Reversed sequence
k = 1
for i in reversed(range(rows)):
    for x in range(k):
        print(end=" ")
    k += 1
    for j in range(1, i+1):
        print(pattern, end=" ")
    print()
