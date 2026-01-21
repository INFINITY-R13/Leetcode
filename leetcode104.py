# LeetCode Problem 104: Maximum Depth of Binary Tree


from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    """
    Find the maximum depth of a binary tree.
    
    Approach: Recursive DFS
    - Base case: If node is None, depth is 0
    - Recursive case: Depth is 1 + max(left subtree depth, right subtree depth)
    
    Time Complexity: O(n) - visit each node once
    Space Complexity: O(h) - recursion stack, where h is height (worst case O(n) for skewed tree)
    """
    if root is None:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# Alternative iterative approach using BFS (level-order traversal)
from collections import deque

def maxDepthBFS(root: Optional[TreeNode]) -> int:
    """
    Find maximum depth using iterative BFS approach.
    
    Time Complexity: O(n)
    Space Complexity: O(w) - where w is maximum width of tree
    """
    if root is None:
        return 0
    
    queue = deque([(root, 1)])  # (node, depth)
    max_d = 0
    
    while queue:
        node, depth = queue.popleft()
        max_d = max(max_d, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_d


# Test cases
if __name__ == "__main__":
    # Example 1: [3,9,20,null,null,15,7]
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    
    print(f"Example 1 - Recursive: {maxDepth(root1)}")  # Output: 3
    print(f"Example 1 - BFS: {maxDepthBFS(root1)}")      # Output: 3
    
    # Example 2: [2, null, 3]
    #       2
    #        \
    #         3
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    
    print(f"Example 2 - Recursive: {maxDepth(root2)}")  # Output: 2
    print(f"Example 2 - BFS: {maxDepthBFS(root2)}")      # Output: 2
    
    # Example 3: Empty tree
    print(f"Example 3 - Recursive: {maxDepth(None)}")   # Output: 0
    print(f"Example 3 - BFS: {maxDepthBFS(None)}")       # Output: 0