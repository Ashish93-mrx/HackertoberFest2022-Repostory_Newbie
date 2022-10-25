#this program is use to get the height of the binar tree using recurrsion

#Time and Space Complexity:
#The time complexity of the algorithm is O(n) as we iterate through node of the binary tree calculating the height of the binary tree only once.
#And the space complexity is also O(n) as we are following recursion, where recursive stack can have upto n elements. 
#Where n is the number of nodes in the binary tree.

#define a Class Tree, to intiate the binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def height(root):
 
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0 
    # Recursively call height of each node
    leftAns = height(root.left)
    rightAns = height(root.right)
 
    # Return max(leftHeight, rightHeight) at each iteration
    return max(leftAns, rightAns) + 1
 
# Test the algorithm
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
 
print("Height of the binary tree is: " + str(height(root)))
