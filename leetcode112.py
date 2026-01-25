# LeetCode Problem 112: Path Sum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: empty tree
        if not root:
            return False
        
        # Check if we're at a leaf node
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check left and right subtrees
        # Subtract current node's value from targetSum
        remaining = targetSum - root.val
        
        return (self.hasPathSum(root.left, remaining) or 
                self.hasPathSum(root.right, remaining))


# Alternative iterative solution using stack
class SolutionIterative:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        
        # Stack stores (node, current_sum)
        stack = [(root, root.val)]
        
        while stack:
            node, curr_sum = stack.pop()
            
            # Check if leaf node with matching sum
            if not node.left and not node.right and curr_sum == targetSum:
                return True
            
            # Add children to stack with updated sum
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))
            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
        
        return False


# Example usage and test cases
def test_path_sum():
    # Example 1: Tree [5,4,8,11,null,13,4,7,2,null,null,null,1]
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    
    sol = Solution()
    print(f"hasPathSum(root, 22): {sol.hasPathSum(root, 22)}")  # True (5->4->11->2)
    print(f"hasPathSum(root, 26): {sol.hasPathSum(root, 26)}")  # True (5->8->13)
    print(f"hasPathSum(root, 10): {sol.hasPathSum(root, 10)}")  # False
    
    # Example 2: Empty tree
    print(f"hasPathSum(None, 0): {sol.hasPathSum(None, 0)}")  # False
    
    # Example 3: Single node
    single = TreeNode(1)
    print(f"hasPathSum(TreeNode(1), 1): {sol.hasPathSum(single, 1)}")  # True

if __name__ == "__main__":
    test_path_sum()