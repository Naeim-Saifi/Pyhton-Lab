# arr=[2,5,8,12,14,3,4,1]
# k=3
# max
# sum=0
# for i in range(0,k):
#     sum+=arr[i]
# max=sum
# for i in range(0,len(arr)-k):
#     res=sum-arr[i]+arr[i+k]
#     sum=res
#     if(res>max):
#         max=res
# print("Maximum in array: ", max)
arr=[1,3,-1,-3,5,3,6,7]
res = []
k=3
l1 = []
for i in range(0, k):
    l1.append(arr[i])
res.append(max(l1))
for i in range(0, len(arr) - k):
    
    l1.pop(0)
    l1.append(arr[i + k])
    res.append(max(l1))
print(res)