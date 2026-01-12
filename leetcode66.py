## LeetCode Problem 66: Plus One


def plusOne(digits):
    """
    Increment a large integer represented as an array of digits by one.
    
    Args:
        digits: List of integers representing digits from most to least significant
    
    Returns:
        List of integers representing the incremented number
    """
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits


# Test cases
def test_plusOne():
    # Test case 1: Normal increment
    result1 = plusOne([1, 2, 3])
    print(f"Input: [1,2,3] -> Output: {result1}")
    assert result1 == [1, 2, 4], f"Expected [1,2,4], got {result1}"
    
    # Test case 2: Carry over (all 9s)
    result2 = plusOne([9, 9, 9])
    print(f"Input: [9,9,9] -> Output: {result2}")
    assert result2 == [1, 0, 0, 0], f"Expected [1,0,0,0], got {result2}"
    
    # Test case 3: Partial carry over
    result3 = plusOne([1, 9, 9])
    print(f"Input: [1,9,9] -> Output: {result3}")
    assert result3 == [2, 0, 0], f"Expected [2,0,0], got {result3}"
    
    # Test case 4: Single digit
    result4 = plusOne([9])
    print(f"Input: [9] -> Output: {result4}")
    assert result4 == [1, 0], f"Expected [1,0], got {result4}"
    
    # Test case 5: Single digit (no carry)
    result5 = plusOne([5])
    print(f"Input: [5] -> Output: {result5}")
    assert result5 == [6], f"Expected [6], got {result5}"
    
    # Test case 6: Larger number
    result6 = plusOne([4, 3, 2, 1])
    print(f"Input: [4,3,2,1] -> Output: {result6}")
    assert result6 == [4, 3, 2, 2], f"Expected [4,3,2,2], got {result6}"
    
    print("\n✅ All test cases passed!")


if __name__ == "__main__":
    test_plusOne()