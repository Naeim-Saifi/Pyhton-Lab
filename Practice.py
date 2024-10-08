#Fibonacci Series
# 0 1 1 2 3 5 8....
# n=7
# prev=0
# next=1
# print("0", "1",end=' ')
# for i in range(1,n):
#     fib=prev+next
#     print(fib,end=' ')
#     prev=next
#     next=fib


#Armstrong Number
# import math
# n=1539
# cpy=n
# chck=n
# count=0
# arm=0
# while(n!=0):
#     count+=1
#     n=n//10
# print(count)
# while(cpy!=0):
#     a=cpy%10
#     cpy=cpy//10
#     arm+=math.pow(a,count)

# arm=int(arm)
# if(arm==chck):
#     print("Armstrong Number")
# else:
#     print("Not")

#Recursion
#Factorial
# def fact(n):
#     if(n<=1):
#         return 1
#     else:
#         return n*fact(n-1)
    
# print(fact(4))

#Fibonnaci Series
# def fibonacci(n):
   
#     if n == 1 :
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = 10  
# for i in range(1, n + 1):
#     print(fibonacci(i), end=" ")

#Tower Hanoi 
# def TowerofHanoi(n,A,B,C):
#     if(n==1):
#         print("Disk Transfer",n,"From",A,"to",C)
#         return
#     else:
#         TowerofHanoi(n-1,A,C,B)
#         print("Disk Transfer",n,"From",A,"to",C)
#         TowerofHanoi(n-1,B,A,C)
# TowerofHanoi(3,"S","H","D")
n = 2.0283374
print(f"{n:.2f}")
