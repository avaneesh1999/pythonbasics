def klargest(arr,k):

    arr.sort(reverse=True)
    print("reversed array is::",arr)
    for i in range(k):
        print(arr[i],end=" ")


arr=[22,33,55]
k=2

klargest(arr,k)








