#LeetCode Problem 108: Convert Sorted Array to Binary Search Tree


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    Convert a sorted array to a height-balanced BST.
    
    A height-balanced BST is defined as a binary tree in which the left and right
    subtrees of every node differ in height by no more than 1.
    
    Args:
        nums: List of integers sorted in ascending order
    
    Returns:
        TreeNode: Root of the height-balanced BST
    """
    def buildBST(left, right):
        # Base case: empty subarray
        if left > right:
            return None
        
        # Choose the middle element as root to ensure balance
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        
        # Recursively build left and right subtrees
        node.left = buildBST(left, mid - 1)
        node.right = buildBST(mid + 1, right)
        
        return node
    
    return buildBST(0, len(nums) - 1)


# Helper function to visualize the tree (in-order traversal)
def inorderTraversal(root):
    """Returns in-order traversal of BST (should be sorted)"""
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)


# Helper function to check tree height
def getHeight(root):
    """Returns the height of the tree"""
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))


# Test cases
if __name__ == "__main__":
    # Test 1: Basic example
    nums1 = [-10, -3, 0, 5, 9]
    root1 = sortedArrayToBST(nums1)
    print(f"Input: {nums1}")
    print(f"In-order traversal: {inorderTraversal(root1)}")
    print(f"Tree height: {getHeight(root1)}\n")
    
    # Test 2: Single element
    nums2 = [0]
    root2 = sortedArrayToBST(nums2)
    print(f"Input: {nums2}")
    print(f"In-order traversal: {inorderTraversal(root2)}")
    print(f"Tree height: {getHeight(root2)}\n")
    
    # Test 3: Larger array
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    root3 = sortedArrayToBST(nums3)
    print(f"Input: {nums3}")
    print(f"In-order traversal: {inorderTraversal(root3)}")
    print(f"Tree height: {getHeight(root3)}\n")
    
    # Test 4: Even number of elements
    nums4 = [1, 2, 3, 4]
    root4 = sortedArrayToBST(nums4)
    print(f"Input: {nums4}")
    print(f"In-order traversal: {inorderTraversal(root4)}")
    print(f"Tree height: {getHeight(root4)}")