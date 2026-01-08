# LeetCode Problem 27: Remove Element


def removeElement(nums, val):
    """
    Remove all occurrences of val in-place and return the new length.
    
    Args:
        nums: List[int] - input array
        val: int - value to remove
    
    Returns:
        int - number of elements not equal to val
    """
    k = 0  # pointer for next position to place non-val element
    
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    
    return k


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = removeElement(nums1, val1)
    print(f"Test 1: k = {k1}, nums = {nums1[:k1]}")
    # Expected: k = 2, nums = [2, 2]
    
    # Test case 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = removeElement(nums2, val2)
    print(f"Test 2: k = {k2}, nums = {nums2[:k2]}")
    # Expected: k = 5, nums = [0, 1, 3, 0, 4]
    
    # Test case 3 - all elements are val
    nums3 = [1, 1, 1, 1]
    val3 = 1
    k3 = removeElement(nums3, val3)
    print(f"Test 3: k = {k3}, nums = {nums3[:k3]}")
    # Expected: k = 0, nums = []
    
    # Test case 4 - no elements are val
    nums4 = [1, 2, 3, 4]
    val4 = 5
    k4 = removeElement(nums4, val4)
    print(f"Test 4: k = {k4}, nums = {nums4[:k4]}")
    # Expected: k = 4, nums = [1, 2, 3, 4]