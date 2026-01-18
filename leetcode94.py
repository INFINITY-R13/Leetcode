# Leetcode problem 94: Binary Tree Inorder Traversal


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    result = []
    stack = []
    current = root
    
    while current or stack:
        # Reach the leftmost node of the current node
        while current:
            stack.append(current)
            current = current.left
        
        # Current must be None at this point
        current = stack.pop()
        result.append(current.val)
        
        # Now move to the right subtree
        current = current.right
        
    return result


# Helper function to build a tree from a list (level-order)
def buildTree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    # Test 1: Example tree
    #       4
    #      / \
    #     2   6
    #    / \
    #   1   3
    tree1 = buildTree([4, 2, 6, 1, 3])
    print("Test 1:", inorderTraversal(tree1))  # Expected: [1, 2, 3, 4, 6]
    
    # Test 2: Simple example from LeetCode
    #   1
    #    \
    #     2
    #    /
    #   3
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    root2.right.left = TreeNode(3)
    print("Test 2:", inorderTraversal(root2))  # Expected: [1, 3, 2]
    
    # Test 3: Left-skewed tree
    #       3
    #      /
    #     2
    #    /
    #   1
    tree3 = buildTree([3, 2, None, 1])
    print("Test 3:", inorderTraversal(tree3))  # Expected: [1, 2, 3]
    
    # Test 4: Single node
    tree4 = buildTree([1])
    print("Test 4:", inorderTraversal(tree4))  # Expected: [1]
    
    # Test 5: Empty tree
    tree5 = buildTree([])
    print("Test 5:", inorderTraversal(tree5))  # Expected: []
    
    # Test 6: Complete binary tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    tree6 = buildTree([1, 2, 3, 4, 5])
    print("Test 6:", inorderTraversal(tree6))  # Expected: [4, 2, 5, 1, 3]