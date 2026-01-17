# LeetCode Problem 88: Merge Sorted Array


def merge(nums1, m, nums2, n):
    """
    Merge nums2 into nums1 in-place.
    
    Args:
        nums1: List with m elements followed by n zeros
        m: Number of elements in nums1
        nums2: List with n elements
        n: Number of elements in nums2
    """
    # Three pointers
    p1 = m - 1      # Last element in nums1's initial portion
    p2 = n - 1      # Last element in nums2
    p = m + n - 1   # Last position in nums1
    
    # Merge from the end
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


# Test cases
def test_merge():
    print("Running test cases...\n")
    
    # Test 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3
    print(f"Test 1:")
    print(f"  Before: nums1 = {nums1}, nums2 = {nums2}")
    merge(nums1, m, nums2, n)
    print(f"  After:  nums1 = {nums1}")
    print(f"  Expected: [1, 2, 2, 3, 5, 6]")
    print(f"  Pass: {nums1 == [1, 2, 2, 3, 5, 6]}\n")
    
    # Test 2
    nums1 = [1]
    nums2 = []
    m, n = 1, 0
    print(f"Test 2:")
    print(f"  Before: nums1 = {nums1}, nums2 = {nums2}")
    merge(nums1, m, nums2, n)
    print(f"  After:  nums1 = {nums1}")
    print(f"  Expected: [1]")
    print(f"  Pass: {nums1 == [1]}\n")
    
    # Test 3
    nums1 = [0]
    nums2 = [1]
    m, n = 0, 1
    print(f"Test 3:")
    print(f"  Before: nums1 = {nums1}, nums2 = {nums2}")
    merge(nums1, m, nums2, n)
    print(f"  After:  nums1 = {nums1}")
    print(f"  Expected: [1]")
    print(f"  Pass: {nums1 == [1]}\n")
    
    # Test 4
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    m, n = 3, 3
    print(f"Test 4:")
    print(f"  Before: nums1 = {nums1}, nums2 = {nums2}")
    merge(nums1, m, nums2, n)
    print(f"  After:  nums1 = {nums1}")
    print(f"  Expected: [1, 2, 3, 4, 5, 6]")
    print(f"  Pass: {nums1 == [1, 2, 3, 4, 5, 6]}\n")
    
    # Test 5
    nums1 = [1, 2, 4, 5, 6, 0]
    nums2 = [3]
    m, n = 5, 1
    print(f"Test 5:")
    print(f"  Before: nums1 = {nums1}, nums2 = {nums2}")
    merge(nums1, m, nums2, n)
    print(f"  After:  nums1 = {nums1}")
    print(f"  Expected: [1, 2, 3, 4, 5, 6]")
    print(f"  Pass: {nums1 == [1, 2, 3, 4, 5, 6]}\n")


if __name__ == "__main__":
    test_merge()