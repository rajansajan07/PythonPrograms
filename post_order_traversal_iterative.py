class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def postorder_traversal(root):
    if not root:
        return []
    stack, result = [(root, False)], []
    while stack:
        node, visited = stack.pop()
        if visited:
            result.append(node.value)
        else:
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))
    return result
