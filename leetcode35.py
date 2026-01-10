# LeetCode Problem 35: Search Insert Position

def searchInsert(nums, target):
    """
    Find the index of target in a sorted array, or the index where it should be inserted.
    
    Args:
        nums: List of distinct integers in sorted order
        target: The target value to search for
    
    Returns:
        Index of target if found, otherwise index where it should be inserted
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If target not found, left will be at the insertion position
    return left


# Test cases
if __name__ == "__main__":
    # Test case 1: Target found in array
    nums1 = [1, 3, 5, 6]
    target1 = 5
    print(f"Array: {nums1}, Target: {target1}")
    print(f"Output: {searchInsert(nums1, target1)}")  # Expected: 2
    print()
    
    # Test case 2: Target should be inserted in middle
    nums2 = [1, 3, 5, 6]
    target2 = 2
    print(f"Array: {nums2}, Target: {target2}")
    print(f"Output: {searchInsert(nums2, target2)}")  # Expected: 1
    print()
    
    # Test case 3: Target should be inserted at end
    nums3 = [1, 3, 5, 6]
    target3 = 7
    print(f"Array: {nums3}, Target: {target3}")
    print(f"Output: {searchInsert(nums3, target3)}")  # Expected: 4
    print()
    
    # Test case 4: Target should be inserted at beginning
    nums4 = [1, 3, 5, 6]
    target4 = 0
    print(f"Array: {nums4}, Target: {target4}")
    print(f"Output: {searchInsert(nums4, target4)}")  # Expected: 0
    print()
    
    # Test case 5: Single element array
    nums5 = [1]
    target5 = 0
    print(f"Array: {nums5}, Target: {target5}")
    print(f"Output: {searchInsert(nums5, target5)}")  # Expected: 0