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


data = input()
l = data.split(",")
t = tuple(l)

print(l)
print(t)
