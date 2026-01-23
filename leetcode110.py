# LeetCode Problem 110: Balanced Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    """
    Determine if a binary tree is height-balanced.
    
    A tree is balanced if for every node, the height difference
    between left and right subtrees is at most 1.
    
    Time: O(n), Space: O(h) where h is height
    """
    def check_height(node):
        # Base case: empty tree has height 0 and is balanced
        if not node:
            return 0
        
        # Check left subtree
        left_height = check_height(node.left)
        if left_height == -1:  # Left subtree is unbalanced
            return -1
        
        # Check right subtree
        right_height = check_height(node.right)
        if right_height == -1:  # Right subtree is unbalanced
            return -1
        
        # Check if current node is balanced
        if abs(left_height - right_height) > 1:
            return -1
        
        # Return height of current subtree
        return max(left_height, right_height) + 1
    
    return check_height(root) != -1


# Example usage and test cases
if __name__ == "__main__":
    # Example 1: Balanced tree
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(f"Tree 1 balanced: {isBalanced(root1)}")  # True
    
    # Example 2: Unbalanced tree
    #       1
    #      / \
    #     2   2
    #    / \
    #   3   3
    #  / \
    # 4   4
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(3)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(4)
    print(f"Tree 2 balanced: {isBalanced(root2)}")  # False
    
    # Example 3: Empty tree
    print(f"Empty tree balanced: {isBalanced(None)}")  # True
    
    # Example 4: Single node
    root3 = TreeNode(1)
    print(f"Single node balanced: {isBalanced(root3)}")  # True