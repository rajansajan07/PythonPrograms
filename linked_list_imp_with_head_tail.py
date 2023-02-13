# Program to count the number of nodes in a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print()


def main():
    g_list = LinkedList()
    g_list.add_last(1)
    g_list.add_last(2)
    g_list.add_last(3)
    g_list.add_last(4)
    g_list.add_first(-1)
    g_list.add_first(-2)

    g_list.print_list()


if __name__ == "__main__":
    main()

