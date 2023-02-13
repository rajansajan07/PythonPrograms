# Program to reverse a node in python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    current = head
    if head is None:
        print("Emtpy list")
        return
    while current is not None:
        print(current.data, " -> ", end=" ")
        current = current.next
    print("N")


# function to reverse a node
def reverse_list(head):
    prev_ptr = None
    current = head
    while current is not None:
        next_ptr = current.next
        current.next = prev_ptr
        prev_ptr = current
        current = next_ptr
    head = prev_ptr
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print_list(head)
    head = reverse_list(head)
    print_list(head)





if __name__ == "__main__":
    main()
