# Write code to implement dequeue in python

class Dequeue:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def pop_front(self):
        if len(self.items) == 0:
            print("Empty dequeue")
            return
        return self.items.pop(0)

    def pop_rear(self):
        if len(self.items) == 0:
            print("Emtpy dequeue")
            return
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        if len(self.items) == 0:
            print("Emtpy dequeue")
            return
        for i in range(0, len(self.items)):
            print(self.items[i], end=" ")


def main():
    dequeue = Dequeue()
    dequeue.add_front(3)
    dequeue.add_front(5)

    dequeue.add_rear(4)
    dequeue.display()


if __name__ == "__main__":
    main()

