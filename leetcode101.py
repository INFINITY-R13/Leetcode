# LeetCode 101: Symmetric Tree


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Solution 1: Recursive Approach
def isSymmetric_recursive(root):
    """
    Check if a binary tree is symmetric around its center.
    
    Time: O(n) - visit each node once
    Space: O(h) - recursion stack where h is height
    """
    def isMirror(left, right):
        # Both null - symmetric
        if not left and not right:
            return True
        
        # One null, one not - not symmetric
        if not left or not right:
            return False
        
        # Check: same value AND left's left mirrors right's right 
        # AND left's right mirrors right's left
        return (left.val == right.val and
                isMirror(left.left, right.right) and
                isMirror(left.right, right.left))
    
    if not root:
        return True
    
    return isMirror(root.left, root.right)


# Solution 2: Iterative Approach (Using Queue)
def isSymmetric_iterative(root):
    """
    Iterative approach using BFS with a queue.
    
    Time: O(n)
    Space: O(w) where w is max width of tree
    """
    if not root:
        return True
    
    queue = deque([(root.left, root.right)])
    
    while queue:
        left, right = queue.popleft()
        
        # Both null - continue
        if not left and not right:
            continue
        
        # One null or values differ - not symmetric
        if not left or not right or left.val != right.val:
            return False
        
        # Add children in mirror order
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    
    return True


# Test Cases
def run_tests():
    print("Testing Symmetric Binary Tree Solutions\n")
    print("=" * 50)
    
    # Test 1: Symmetric tree
    #       1
    #      / \
    #     2   2
    #    / \ / \
    #   3  4 4  3
    print("\nTest 1: Symmetric tree")
    print("       1")
    print("      / \\")
    print("     2   2")
    print("    / \\ / \\")
    print("   3  4 4  3")
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))
    print(f"Recursive: {isSymmetric_recursive(root1)}")  # Expected: True
    print(f"Iterative: {isSymmetric_iterative(root1)}")  # Expected: True
    
    # Test 2: Not symmetric
    #       1
    #      / \
    #     2   2
    #      \   \
    #       3   3
    print("\nTest 2: Not symmetric tree")
    print("       1")
    print("      / \\")
    print("     2   2")
    print("      \\   \\")
    print("       3   3")
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))
    print(f"Recursive: {isSymmetric_recursive(root2)}")  # Expected: False
    print(f"Iterative: {isSymmetric_iterative(root2)}")  # Expected: False
    
    # Test 3: Single node (symmetric)
    print("\nTest 3: Single node")
    print("       1")
    root3 = TreeNode(1)
    print(f"Recursive: {isSymmetric_recursive(root3)}")  # Expected: True
    print(f"Iterative: {isSymmetric_iterative(root3)}")  # Expected: True
    
    # Test 4: Empty tree (symmetric)
    print("\nTest 4: Empty tree")
    root4 = None
    print(f"Recursive: {isSymmetric_recursive(root4)}")  # Expected: True
    print(f"Iterative: {isSymmetric_iterative(root4)}")  # Expected: True
    
    # Test 5: Symmetric with deeper tree
    #         1
    #       /   \
    #      2     2
    #     / \   / \
    #    3   4 4   3
    #   /         \
    #  5           5
    print("\nTest 5: Deeper symmetric tree")
    print("         1")
    print("       /   \\")
    print("      2     2")
    print("     / \\   / \\")
    print("    3   4 4   3")
    print("   /           \\")
    print("  5             5")
    root5 = TreeNode(1)
    root5.left = TreeNode(2, TreeNode(3, TreeNode(5)), TreeNode(4))
    root5.right = TreeNode(2, TreeNode(4), TreeNode(3, None, TreeNode(5)))
    print(f"Recursive: {isSymmetric_recursive(root5)}")  # Expected: True
    print(f"Iterative: {isSymmetric_iterative(root5)}")  # Expected: True
    
    # Test 6: Not symmetric (different values)
    #       1
    #      / \
    #     2   3
    print("\nTest 6: Different values")
    print("       1")
    print("      / \\")
    print("     2   3")
    root6 = TreeNode(1, TreeNode(2), TreeNode(3))
    print(f"Recursive: {isSymmetric_recursive(root6)}")  # Expected: False
    print(f"Iterative: {isSymmetric_iterative(root6)}")  # Expected: False
    
    print("\n" + "=" * 50)
    print("All tests completed!")


if __name__ == "__main__":
    run_tests()