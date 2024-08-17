## =========== LEVEL 1 ===========
# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))

# print(','.join(l))


# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)

# x = int(input())
# print(fact(x))


# con = {}
# x = int(input())

# for i in range(1, x+1):
#     con[i] = i*i

# print(con)


# data = input()
# l = data.split(",")
# t = tuple(l)

# print(l)
# print(t)


# class _string_(object):
#     def __init__(self):
#         self.s = ""

#     def getString(self):
#         self.s = input()

#     def printString(self):
#         print(self.s.upper())

# data = _string_()
# data.getString()
# data.printString()

# import math

# C, H = 50, 30
# D_l = input()
# D = D_l.split(",")
# Q = []
# for d in D:
#     Q.append(str(math.sqrt((2*C*int(d)) / H)))

# print(','.join(Q))

# input_str = input()
# dimensions = [int(x) for x in input_str.split(",")]
# ans = [[0 for col in range(dimensions[1])] for row in range(dimensions[0])]
# for row in range(dimensions[0]):
#     for col in range(dimensions[1]):    
#         ans[row][col] = row * col

# print(ans) 

# data = input()
# data_l = data.split(",")
# data_l.sort()
# print(",".join(data_l))

# data = input()
# data = data.upper()
# print(data)

s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
