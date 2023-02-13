# Program to implement the doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head
        print("N <- ", end=" ")
        while current.next is not None:
            print(current.data, " <--> ", end=" ")
            current = current.next
        print(current.data, " -> N")

    # method to reverse a doubly linked list
    def reverse__list(self):
        current = self.head
        prev_ptr = None

        while current is not None:
            next_ptr = current.next
            current.next = prev_ptr
            current.prev = next_ptr
            prev_ptr = current
            current = next_ptr
        self.head = prev_ptr


def main():
    d_list = DoublyList()
    d_list.add_first(1)
    d_list.add_first(2)
    d_list.add_first(3)

    d_list.display()
    d_list.reverse__list()
    d_list.display()


if __name__ == "__main__":
    main()
