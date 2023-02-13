class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function to implement hte pre-order traversal using iteration
def pre_order_traversal_iterative(root):
    tree_stack = []
    result = []
    current = root
    while current is not None or tree_stack:
        while current is not None:
            tree_stack.append(current)
            current = current.left
        current = tree_stack.pop()
        result.append(current.data)
        current = current.right

    return result



# function to implement the preorder traversal using recursion
def pre_order_traversal_recursive(current):
    if current is not None:
        pre_order_traversal_recursive(current.left)
        print(current.data, end=" ")
        pre_order_traversal_recursive(current.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    pre_order_traversal_recursive(root)
    print()
    result = pre_order_traversal_iterative(root)
    print(result)

if __name__ == "__main__":
    main()

