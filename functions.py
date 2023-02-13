# Write code to implement binary search tree
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            focus_node = self.root
            while True:
                parent = focus_node

                if data < focus_node.data:
                    focus_node = focus_node.left
                    if focus_node is None:
                        parent.left = new_node
                        return
                else:
                    focus_node = focus_node.right
                    if focus_node is None:
                        parent.right = new_node
                        return

    def pre_order_traversal(self, current):
        if current is not None:
            print(current.data, end=" ")
            self.pre_order_traversal(current.left)
            self.pre_order_traversal(current.right)


def main():
    btree = BinaryTree()
    btree.insert(50)
    btree.insert(25)
    btree.insert(75)
    btree.insert(12)
    btree.insert(37)
    btree.insert(30)
    btree.insert(43)

    btree.pre_order_traversal(btree.root)


if __name__ == "__main__":
    main()




