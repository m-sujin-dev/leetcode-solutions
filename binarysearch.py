
def binarysearch(s,target):
    low,high=0,len(s)-1
    while low<=high:
        mid=(low+high)//2
        if s[mid]==target:
            return mid
        elif s[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1




s=[1,2,3,4,5,6]
target=int(input())
result = binarysearch(s, target)
print(result)
