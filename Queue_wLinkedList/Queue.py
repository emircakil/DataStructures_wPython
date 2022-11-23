class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):

        new_node = Node(value)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        temporary = self.front

        if self.front is None:
            print("Please add element for queue before dequeued it!")
            return

        self.front = self.front.next

        return temporary

    def getFront(self):
        return self.front

    def getRear(self):
        return self.rear

    def getSize(self):
        temporary = self.front
        counter = 0
        while temporary != None:
            counter = counter + 1
            temporary = temporary.next

        return counter
    def printQueue(self):
        temporary = self.front

        while temporary != None:
            print(temporary.value, end=' -> ')
            temporary = temporary.next
        print()
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    queue.printQueue()

    queue.dequeue()
    queue.dequeue()

    queue.printQueue()

    print(f"Front of queue is {queue.getFront().value}")
    print(f"Rear of queue is {queue.getRear().value}")
    print(f"Size of queue is {queue.getSize()}")


