# Pre-order traversal
def pre_order(node):
    if node is None: 
        return []
    output = [node.data]
    if node.left is not None:
        output += pre_order(node.left)
    if node.right is not None:
        output += pre_order(node.right)
    return output

# In-order traversal
def in_order(node):
    if node is None: 
        return []
    output = [node.data]
    if node.left is not None:
        output = in_order(node.left) + output
    if node.right is not None: 
        output += in_order(node.right)
    return output

# Post-order traversal
def post_order(node):
    if node is None: 
        return []
    output = [node.data]
    if node.right is not None: 
        output = post_order(node.right) + output
    if node.left is not None:
        output = post_order(node.left) + output
    return output

