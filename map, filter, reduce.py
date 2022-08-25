from functools import reduce
import numpy as np
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("========== <><><><> ==========")
# map
# method_1 = list(map(lambda x: x*x, li))
# print(method_1)

# map_2
# method_1a = list(map([lambda x:x*x, lambda x:x*x*x], li))
# print(method_1a)

# map_3
# square = lambda x: x*x
# cube = lambda x: x*x*x
# func = [square, cube]
# result = []
# for i in li:
#     val = list(map(lambda x: x(i), func))
#     result.append(val)
# print(result)

# filter
# method_2 = list(filter(lambda x: x >= 5, li))
# print(method_2)

# reduce
# method_3 = reduce(lambda x, y: x+y, li)
# print(method_3)
