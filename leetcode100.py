# LeetCode Problem 100: Same Tree


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Check if two binary trees are the same.
    
    Two trees are the same if:
    1. Both nodes are None (base case)
    2. Both nodes have the same value and their left and right subtrees are the same
    
    Time Complexity: O(min(m, n)) where m and n are the number of nodes
    Space Complexity: O(min(h1, h2)) for recursion stack, where h1 and h2 are heights
    """
    # Base case: both nodes are None
    if not p and not q:
        return True
    
    # If one is None and the other is not, they're different
    if not p or not q:
        return False
    
    # If values don't match, trees are different
    if p.val != q.val:
        return False
    
    # Recursively check left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Identical trees
    #       1           1
    #      / \         / \
    #     2   3       2   3
    p1 = TreeNode(1)
    p1.left = TreeNode(2)
    p1.right = TreeNode(3)
    
    q1 = TreeNode(1)
    q1.left = TreeNode(2)
    q1.right = TreeNode(3)
    
    print(f"Test 1 - Same trees: {isSameTree(p1, q1)}")  # True
    
    # Test case 2: Different structure
    #       1           1
    #      /             \
    #     2               2
    p2 = TreeNode(1)
    p2.left = TreeNode(2)
    
    q2 = TreeNode(1)
    q2.right = TreeNode(2)
    
    print(f"Test 2 - Different structure: {isSameTree(p2, q2)}")  # False
    
    # Test case 3: Different values
    #       1           1
    #      / \         / \
    #     2   1       2   3
    p3 = TreeNode(1)
    p3.left = TreeNode(2)
    p3.right = TreeNode(1)
    
    q3 = TreeNode(1)
    q3.left = TreeNode(2)
    q3.right = TreeNode(3)
    
    print(f"Test 3 - Different values: {isSameTree(p3, q3)}")  # False
    
    # Test case 4: Both empty
    print(f"Test 4 - Both empty: {isSameTree(None, None)}")  # True