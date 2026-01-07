# LeetCode Problem 26: Remove Duplicates from Sorted Array


def removeDuplicates(nums):
    """
    Remove duplicates from a sorted array in-place.
    
    Args:
        nums: A list of integers sorted in non-decreasing order
    
    Returns:
        The number of unique elements (k)
    """
    # Edge case: empty array (though constraints say length >= 1)
    if not nums:
        return 0
    
    # The first element is always unique, so our write position starts at index 1
    # This represents where we'll place the next unique element we find
    write_pos = 1
    
    # Scan through the array starting from index 1
    # We compare each element with the one before it
    for read_pos in range(1, len(nums)):
        # If current element is different from the previous one,
        # it's a new unique value (remember: array is sorted!)
        if nums[read_pos] != nums[read_pos - 1]:
            # Place this unique element at our write position
            nums[write_pos] = nums[read_pos]
            # Move write position forward for the next unique element
            write_pos += 1
    
    # write_pos now equals the count of unique elements
    # (since we started at 1 and incremented for each new unique value)
    return write_pos


# Test with Example 1
nums1 = [1, 1, 2]
k1 = removeDuplicates(nums1)
print(f"Example 1: k = {k1}, nums = {nums1[:k1]}")
# Expected: k = 2, nums = [1, 2]

# Test with Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k2 = removeDuplicates(nums2)
print(f"Example 2: k = {k2}, nums = {nums2[:k2]}")
# Expected: k = 5, nums = [0, 1, 2, 3, 4]

# Additional test cases
nums3 = [1, 1, 1, 1, 1]
k3 = removeDuplicates(nums3)
print(f"All duplicates: k = {k3}, nums = {nums3[:k3]}")
# Expected: k = 1, nums = [1]

nums4 = [1, 2, 3, 4, 5]
k4 = removeDuplicates(nums4)
print(f"No duplicates: k = {k4}, nums = {nums4[:k4]}")
# Expected: k = 5, nums = [1, 2, 3, 4, 5]