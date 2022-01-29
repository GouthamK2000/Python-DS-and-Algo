def linSe2D(arr,tar,r,c):
    for i in range(r):
        for j in range(c):
            if(arr[i][j]==tar):
                return i,j
    return -1,-1
    
r=int(input("No of Rows: "))
c=int(input("Enter the colummns: "))
t=int(input("enter the target: "))
arr=[]
for i in range(r):
    temp=[]
    for j in range(c):
        temp.append(int(input()))
    arr.append(temp)
print(linSe2D(arr,t,r,c))

#Without functions
r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
tar=int(input("Enter the no. of columns: "))
arr=[]
for i in range(r):
    temp=[]
    for j in  range(c):
        temp.append(int(input()))
    arr.append(temp)

for i in range(r):
    for j in range(c):
        if(arr[i][j]==tar):
            print(i,j)


