# Basic code for Binary search in an array
def binarySearch(arr, b, e, tar):

    while b <= e:
        mid = b + (e- b) // 2
          
        if arr[mid] == tar:
            return mid
        
        elif arr[mid] < tar:
            b= mid + 1
        
        else:
            e = mid - 1
    
    return -1
 

list_1=list(map(int,input("Enter list elements: ").split()))
tar=int(input("Enter the target elemnts: "))
print( binarySearch(list_1, 0, len(list_1)-1, tar))

#Code for Binary Search (Order Agnostic)
def BinSearch(arr,tar,s,e):
    s=0
    e=len(arr)-1
    while(s<=e):
        mid=s+(e-s)//2
        if(tar==arr[mid]):
            return mid

        if(arr[s]<arr[e]):
            if(tar>arr[mid]):
                s=mid+1
            else:
                e=mid-1
            
        else:
            if(tar>arr[mid]):
                e=mid-1
            else:
                s=mid+1
    return -1

arr=list(map(int,input("Enter the array elements: ").split()))
tar=int(input("Enter the target: "))
print(BinSearch(arr,tar,0,len(arr)-1))

 
