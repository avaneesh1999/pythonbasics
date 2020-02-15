def search(list,n):
    i=0
    while i<len(list):
        if list[i] == n:
           return True
        i=i+1


    return false


list=[1,2,3,45,6]
n=6

if search(list,n):
    print("found")
else:
    print("not found")