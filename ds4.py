def commonelemet(a,b):
    seta=set(a)
    setb=set(b)
    if(seta & setb):
      print("common element is:", seta &setb)
    else:
        print("no common element:")





x=int(input("enter the no of elements in first array:"))
A=list()
print ("enter the  elements:")
for i in range(x):
    k=int(input())
    A.append(k)
print(A)

y=int(input("enter the no of elements in second array:"))
B=list()
print ("enter the  elements:")
for i in range(y):
    k=int(input())
    B.append(k)
print(B)
commonelemet(A,B)

