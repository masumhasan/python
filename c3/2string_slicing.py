hello = "Whatsup"
# name = input("Enter Name: ")
# c = name+hello
# print(c)
print(hello[0])
x = 3
d = "345634"
print(d[x])
# hello[3]= "r" ====> Does not work
print(hello[0:4])
# ([:4 same as] use 1:4 to choose starting index) slicing the string from index 1to3   0<1---3<4
print(hello[3:])
print(hello[-1])  # print the last index with -1


# SKIP CHAR
abc = "abcdefghijklmnopqrstuvvxyz"
print(abc[0:-1:2])  # print every second char
