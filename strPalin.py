# s="abcdba"
# rev=""
# for i in range(len(s)-1,-1,-1):
#     rev+=s[i]
# if(rev==s):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#with Function

def pal(s):
    i,j=0,len(s)-1
    while(i<=j):
        if(s[i]==s[j]):
            i=i+1
            j=j-1
        else:
            return -1
    return 1
s="aba"
rev=pal(s)
if(rev==1):
    print("Palin")
else:
    print("Not Palin")