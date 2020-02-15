#program for reversing an array:
n=int(input("enter the elements in an array:"))
A=list()
print("enter the elements:")
for i in range(int(n)):
    k=int(input())
    A.append(k)

print(A)
for i in range(n-1,-1,-1):
    print(A[i],end=" ")



