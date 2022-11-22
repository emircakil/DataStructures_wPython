class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def pushLast(self, new_data):
        new_node = Node(new_data)
        temp = self.head

        if (temp == None):
            self.head = new_node
        else:
            while (temp.next != None):
                temp = temp.next

            temp.next = new_node

    def pushFirst(self, new_data):
        new_node = Node(new_data)
        temp = self.head

        if temp == Node:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=' -> ')
            temp = temp.next
        print(" ")

    def deleteNode(self, key):
        temp = self.head

        if temp is None:
            if temp.data == key:
                self.head = temp.next
                temp.next = None
        else:
            while temp.data != key:
                prev = temp
                temp = temp.next

            prev.next = temp.next

    def popNode(self, key):
        temp = self.head

        if temp.data == key:
            self.head = temp.next
            temp.next = None

        else:
            while temp.data is not key:
                prev = temp
                temp = temp.next

        prev.next = temp.next
        return temp.data

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        temp = self.head
        counter = 0
        while temp is not None:
            counter = counter + 1
            temp = temp.next

        return counter

    def concatenateTwoList(self, list2):
        temp = self.head

        outputList = LinkedList()
        outputList.head = temp

        while temp.next is not None:
            temp = temp.next

        temp.next = list2.head

        return outputList


    def reverseList(self):

        temp = self.head
        prev = None

        while (temp is not None):
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    def lastNodeMoveFirst(self):

        temp = self.head


        while temp.next != None:
            perv = temp
            temp = temp.next
        perv.next = None
        temp.next = self.head
        self.head = temp



linkedList = LinkedList()
linkedList.pushFirst(10)
linkedList.pushFirst(9)
linkedList.pushLast(11)
linkedList.pushLast(12)
linkedList.pushFirst(5)

linkedList.printList()

linkedList.deleteNode(11)

linkedList.printList()

print(f"Node {linkedList.popNode(10)} has been deleted from Linked list")

linkedList.printList()

print(f"Size of Linked List is: {linkedList.size()}")

linkedList2 = LinkedList()
linkedList2.pushLast(20)
linkedList2.pushLast(21)
linkedList2.pushLast(22)

linkedList2.printList()

linkedList3 = LinkedList()
linkedList3 = linkedList.concatenateTwoList(linkedList2)

linkedList3.printList()

linkedList3.reverseList()

linkedList3.printList()

linkedList3.lastNodeMoveFirst()

linkedList3.printList()