# ## =========== LEVEL 1 ===========
# # l=[]
# # for i in range(2000, 3201):
# #     if (i%7==0) and (i%5!=0):
# #         l.append(str(i))

# # print(','.join(l))


# # def fact(x):
# #     if x == 0:
# #         return 1
# #     return x * fact(x - 1)

# # x = int(input())
# # print(fact(x))


# # con = {}
# # x = int(input())

# # for i in range(1, x+1):
# #     con[i] = i*i

# # print(con)


# # data = input()
# # l = data.split(",")
# # t = tuple(l)

# # print(l)
# # print(t)


# # class _string_(object):
# #     def __init__(self):
# #         self.s = ""

# #     def getString(self):
# #         self.s = input()

# #     def printString(self):
# #         print(self.s.upper())

# # data = _string_()
# # data.getString()
# # data.printString()

# # import math

# # C, H = 50, 30
# # D_l = input()
# # D = D_l.split(",")
# # Q = []
# # for d in D:
# #     Q.append(str(math.sqrt((2*C*int(d)) / H)))

# # print(','.join(Q))

# # input_str = input()
# # dimensions = [int(x) for x in input_str.split(",")]
# # ans = [[0 for col in range(dimensions[1])] for row in range(dimensions[0])]
# # for row in range(dimensions[0]):
# #     for col in range(dimensions[1]):    
# #         ans[row][col] = row * col

# # print(ans) 

# # data = input()
# # data_l = data.split(",")
# # data_l.sort()
# # print(",".join(data_l))

# # data = input()
# # data = data.upper()
# # print(data)

# # s = input()
# # words = [word for word in s.split(" ")]
# # print(" ".join(sorted(list(set(words)))))

# value = []
# items=[x for x in input().split(',')]
# for p in items:
#     intp = int(p, 2)
#     if not intp%5:
#         value.append(p)

# print(','.join(value))

# values = []
# for i in range(1000, 3001):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         values.append(s)
# print(",".join(values))

# s = input()
# d={"DIGITS":0, "LETTERS":0}
# for c in s:
#     if c.isdigit():
#         d["DIGITS"]+=1
#     elif c.isalpha():
#         d["LETTERS"]+=1
#     else:
#         pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])

# s = input()
# d={"UPPER CASE":0, "LOWER CASE":0}
# for c in s:
#     if c.isupper():
#         d["UPPER CASE"]+=1
#     elif c.islower():
#         d["LOWER CASE"]+=1
#     else:
#         pass
# print("UPPER CASE", d["UPPER CASE"])
# print("LOWER CASE", d["LOWER CASE"])

# a = input()
# n1 = int( "%s" % a )
# n2 = int( "%s%s" % (a,a) )
# n3 = int( "%s%s%s" % (a,a,a) )
# n4 = int( "%s%s%s%s" % (a,a,a,a) )
# print(n1+n2+n3+n4)

# values = input()
# odds = [x for x in values.split(',') if int(x) % 2 != 0]
# print(','.join(odds))

# record = input()
# record = record.split(" ")

# rules = []
# values = []

# for item in record:
#     if item.isalpha(): rules.append(item)
#     elif item.isdigit(): values.append(item)
#     else: pass 

# ans = 0
# for i in range(len(rules)):
#     if rules[i] == 'D': ans += int(values[i])
#     else: ans -= int(values[i])

# print(ans)

# import re

# passwords = input()
# passwords_l = passwords.split(",")

# def check_valid(password):
#     if len(password) < 6 or len(password) > 12: 
#         return False
#     elif not re.search("[a-z]", password): 
#         return False
#     elif not re.search("[0-9]",password): 
#         return False
#     elif not re.search("[A-Z]",password): 
#         return False
#     elif not re.search("[$#@]",password): 
#         return False
#     elif re.search("\s",password): 
#         return False
#     else:
#         return True

# ans = []
# for password in passwords_l:
#     if check_valid(password): 
#         ans.append(password)
# print(",".join(ans))
        
# l = []
# while True:
#     s = input()
#     if not s:
#         break
#     l.append(tuple(s.split(",")))

# print(sorted(l, key=itemgetter(0,1,2)))

# def putNumbers(n):
#     i = 0
#     while i<n:
#         j=i
#         i=i+1
#         if j%7==0:
#             yield j

# for i in putNumbers(100):
#     print(i)