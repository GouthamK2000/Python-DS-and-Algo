class Node:
    def __init__(self,data):
        self.data=data
        self.data=None

class LL:
    def __init__(self):
        self.head=None

    def print_LL(self):
        if self.head is None:
            print("LL is Empty!")
        else:
            n=self.head
            while n!=None:
                print(n.data)
                n=n.ref

L1=LL()
L1.print_LL()