#Linear Search in 1D array without functions

list_1=list(map(int,input("Enter the array elements: ").split()))
tar=int(input("Target?= "))
for i in range(len(list_1)):
    if(list_1[i]==tar):
        print("Index of target=",i)

#Linear Search in 1D array with functions

def linSearch(arr,tar):
    for i in range(len(arr)):
        if (arr[i]==tar):
            print("Index of target=",i)
list_2=list(map(int,input("Enter the array elements: ").split()))
tar=int(input("Enter the target element: "))
linSearch(list_2,tar)







        