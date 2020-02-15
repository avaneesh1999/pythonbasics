import heapq
li=[2,8,9,4,3]
lii=[3,5,9,4,1]
heapq.heapify(li)
print(list(li))
heapq.heappush(li,4)
print(list(li))
heapq.heappop(li)#pops out the smallest element
print(list(li))
heapq.heappushpop(li,3)
print(list(li))
print(heapq.nlargest(2,li))
print(heapq.nsmallest(3,li))
