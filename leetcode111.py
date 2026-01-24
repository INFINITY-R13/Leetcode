# LeetCode 111: Minimum Depth of Binary Tree


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth_BFS(root):
    """
    Find minimum depth using BFS (Level Order Traversal)
    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return 0
    
    queue = deque([(root, 1)])  # (node, depth)
    
    while queue:
        node, depth = queue.popleft()
        
        # If we found a leaf node, return its depth
        if not node.left and not node.right:
            return depth
        
        # Add children to queue
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return 0

def minDepth_DFS(root):
    """
    Find minimum depth using DFS (Recursive)
    Time: O(n), Space: O(h) where h is height
    """
    if not root:
        return 0
    
    # If one subtree is empty, we must go down the other
    if not root.left:
        return 1 + minDepth_DFS(root.right)
    if not root.right:
        return 1 + minDepth_DFS(root.left)
    
    # Both subtrees exist, take minimum
    return 1 + min(minDepth_DFS(root.left), minDepth_DFS(root.right))

# Test cases
if __name__ == "__main__":
    # Example 1: Tree [3,9,20,null,null,15,7]
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
    
    print("Example 1:")
    print(f"BFS: {minDepth_BFS(root1)}")  # Output: 2
    print(f"DFS: {minDepth_DFS(root1)}")  # Output: 2
    
    # Example 2: Tree [2,null,3,null,4,null,5,null,6]
    #     2
    #      \
    #       3
    #        \
    #         4
    #          \
    #           5
    #            \
    #             6
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    
    print("\nExample 2:")
    print(f"BFS: {minDepth_BFS(root2)}")  # Output: 5
    print(f"DFS: {minDepth_DFS(root2)}")  # Output: 5
    
    # Example 3: Single node
    root3 = TreeNode(1)
    print("\nExample 3:")
    print(f"BFS: {minDepth_BFS(root3)}")  # Output: 1
    print(f"DFS: {minDepth_DFS(root3)}")  # Output: 1