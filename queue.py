queue=[]
def enque():
    elem=int(input("Enter the element: "))
    queue.append(elem) #or  queue.insert(0,element) can be used
    
def deque():
    queue.pop(0)

def show():
    print(queue)

while(True):
    user=int(input("press 1.enque 2.deque 3.show 4.quit"))
    if user==1:
        enque()
    elif user==2:
        deque()
    elif user==3:
        show()
    else:
        print("Enter the right element")

