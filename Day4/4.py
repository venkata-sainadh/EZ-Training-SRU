class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def insertEnd(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = Node(data)
    def insertFront(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
    def traverse(self):
        if self.head == None:
            print("Empty Linked List")
            return
        temp = self.head
        while temp!=None:
            print(temp.data,end = "->")
            temp = temp.next
        print()
    def insertAtMiddle(self,data,pos):
        if pos<=0:
            print("Invalid Index ")
            return
        if pos==1:
            self.insertFront(data)
            return
        index = 1
        temp = self.head
        while(index!=pos-1 and temp.next!=None):
            index+=1
            temp = temp.next
        if index<pos-1 :
            print("Invalid position")
            return
        newnode = Node(data)
        newnode.next = temp.next
        temp.next = newnode
obj = SingleLinkedList()
obj.insertFront(10)
obj.insertFront(5)
obj.insertEnd(20)
obj.insertEnd(30)
obj.insertFront(3)
obj.traverse()
obj.insertAtMiddle(15,7) 
obj.traverse()