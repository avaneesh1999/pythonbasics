def fminele(heap,n):
    minele=heap[0]
    for i in range(1,n):
        minele=min(minele,heap[i])
    return minele
n=10
heap = [20, 18, 10, 12, 8,
            9, 3, 5, 6, 8]
print(fminele(heap,n))
