# %%
# Recursive Python program for Breadth and Depth First traversal (BFT and DFT)
# of a Binary Tree.

# A node structure
class Node:

    # A utility function to create a new node (constructor)
    def __init__(currentNode, key):

        currentNode.left = None
        currentNode.right = None
        currentNode.data = key


# Breadth First Travesal functions:

# Function to  print level order for Breadth First traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i,)


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end="\n")
    elif level > 1:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)


# Function to calculate the height of the tree (number of nodes
# forming the longest path from the root down to the furthest
# node)

def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1


# Depth First Functions:

# Preorder traversal of DFT
# (Read the Node, recurse through left subtree followed by right)
def printPreorder(root):

    if root:

        # First print the data of node
        print(root.data),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)


# Postorder traversal of DFT
# Recursivly traverse left subtree and then right, finally reading the current node)
def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.data),

# Inorder traversal of DFT
# (path down leftmost leaf then back to root then path down rightmost leaf)


def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.data),

        # now recur on right child
        printInorder(root.right)


# Driver program to test above functions
root = Node(9)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Printing results to terminal/interactive window
print("Preorder traversal of binary tree is -")
printPreorder(root)

print("\nPostorder traversal of binary tree is -")
printPostorder(root)

print("\nInorder traversal of binary tree is -")
printInorder(root)

print("\nBreadth First order traversal of binary tree is -")
printLevelOrder(root)


# %%

# %%
