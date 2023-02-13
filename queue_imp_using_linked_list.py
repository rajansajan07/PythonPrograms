# Write code to implement queue using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.front is None and self.rear is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Emtpy queue")
            return
        temp = self.front
        self.front = self.front.next
        return temp.data

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end=" ")
            current = current.next


def main():
    queue = MyQueue()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.dequeue()

    queue.display()


if __name__ == "__main__":
    main()





