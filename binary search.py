

def binarysearch(list,n):
    l=0
    u=len(list)-1

    while l<=u:
        mid=l+u//2

        if (list[mid]==n):
            return True
        else:
            if(list[mid]>n):
                u==list[mid]
            else:
                l==list[mid]



list=[1,2,3,4,5,6,7,8]
n=4
if(binarysearch(list,n)):
    print("found")
else:
    print("not found")

