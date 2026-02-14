# a, b = 0, 1
# for i in range(7):
#     print(a, end=" ")
#     a, b = b, a + b

num_n = int(input("enter a number"))
a, b = 0, 1
for i in range(num_n):
    print(a, end=" ")
    a, b = b, a + b