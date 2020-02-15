T = int(input())
for i in range(T):
    N, D = map(int, input().strip().split(" "))
    arr = list()
    for i in range(N):
        arr = list(map(int, input().split(" ")))

    for i in range(0, D):
        first = arr[0]
        for j in range(0, len(arr) - 1):
            arr[j] = arr[j + 1]
            arr[len(arr) - 1] = first
            print()


