stack=[]
def push():
    elem=int(input("Enter the element: "))
    stack.append(elem)
    print(stack)

def pop():
    if(len(stack)==0):
        print("Stack is empty")
    else:
        elem=stack.pop()
        print("Removed element is: ",elem)
        print(stack)

while True:
    user=int(input("Press 1.for push,2.pop, 3.quit "))
    if user==1:
        push()
    elif user==2:
        pop()
    elif user==3:
        break
    else:
        print("Enter the correct statement")



