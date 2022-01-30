def binarySearch(arr, b, e, tar):

    while b <= e:
        mid = b + (e- b) // 2
          
        if arr[mid] == tar:
            return mid
        
        elif arr[mid] < tar:
            b= mid + 1
        
        else:
            e = mid - 1
    
    while e>=b:
        mid=b+(e-b)//2
        
        if arr[mid]==tar:
            return mid
        
        elif arr[mid]<tar:
            e=mid-1
        
        else:
            b=mid+1

    return -1
 

list_1=list(map(int,input("Enter list elements: ").split()))
tar=int(input("Enter the target elemnts: "))
print( binarySearch(list_1, 0, len(list_1)-1, tar))
 
