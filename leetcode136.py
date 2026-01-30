# LeetCode Problem 136: Single Number


def singleNumber(nums):
    """
    Find the element that appears once while all others appear twice.
    Uses XOR operation: a ^ a = 0, a ^ 0 = a
    """
    result = 0
    for num in nums:
        result ^= num
    return result


# Test cases
def test_singleNumber():
    # Test case 1
    nums1 = [2, 2, 1]
    print(f"Input: {nums1}")
    print(f"Output: {singleNumber(nums1)}")
    print(f"Expected: 1\n")
    
    # Test case 2
    nums2 = [4, 1, 2, 1, 2]
    print(f"Input: {nums2}")
    print(f"Output: {singleNumber(nums2)}")
    print(f"Expected: 4\n")
    
    # Test case 3
    nums3 = [1]
    print(f"Input: {nums3}")
    print(f"Output: {singleNumber(nums3)}")
    print(f"Expected: 1\n")
    
    # Test case 4
    nums4 = [7, 3, 5, 3, 7]
    print(f"Input: {nums4}")
    print(f"Output: {singleNumber(nums4)}")
    print(f"Expected: 5\n")
    
    # Test case 5 - negative numbers
    nums5 = [-1, -1, -2]
    print(f"Input: {nums5}")
    print(f"Output: {singleNumber(nums5)}")
    print(f"Expected: -2\n")


# Run tests
if __name__ == "__main__":
    test_singleNumber()