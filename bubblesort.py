def bubblesort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
         if num[j]>num[j+1]:#swapping 
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp



num=[2,7,9,3,6]
bubblesort(num)
print(num)