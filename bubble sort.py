# bubble sort algorithm
def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

li=list(map(int,input().split()))
bubble(li)