# Write code to implement queue in python

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Emtpy queue")
            return
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if len(self.queue) == 0:
            print("Emtpy queue")
            return
        for i in range(0, len(self.queue)):
            print(self.queue[i], end=" ")


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.display()


if __name__ == "__main__":
    main()

