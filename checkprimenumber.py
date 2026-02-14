# n = 7
# for i in range(2, n):
#     if n % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")

num_n = int(input("enter a number"))
for i in range(2, num_n):
   if num_n % i == 0:
       print("Not prime")
       break
else:
    print("Prime")   