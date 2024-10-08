# def fibonacci(n):
#     if n <= 0:
#         return "Input should be a positive integer."
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n_terms = 10  
# print("Fibonacci series:")
# for i in range(1, n_terms + 1):
#     print(fibonacci(i), end=" ")
n=5
f1=0,f2=1
print("0", "1")
sum=0
for i in range(1,n+1):
    sum=f1+f2
    f1=f2
    f2=i
    print(sum)