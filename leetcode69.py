# LeetCode Problem 69: Sqrt(x)


def mySqrt(x: int) -> int:
    """
    Calculate the square root of x rounded down to the nearest integer.
    Uses binary search without any built-in exponent functions.
    
    Time Complexity: O(log x)
    Space Complexity: O(1)
    """
    if x == 0:
        return 0
    
    # Binary search between 1 and x
    left, right = 1, x
    result = 0
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if mid is the square root
        # Use mid <= x // mid to avoid overflow instead of mid * mid <= x
        if mid <= x // mid:
            result = mid  # mid could be the answer, store it
            left = mid + 1  # Try to find a larger value
        else:
            right = mid - 1  # mid is too large
    
    return result


# Test cases
test_cases = [
    (0, 0),
    (1, 1),
    (4, 2),
    (8, 2),
    (16, 4),
    (25, 5),
    (26, 5),
    (100, 10),
    (2147395599, 46339)  # Large number test
]

print("Testing mySqrt function:")
print("-" * 50)
for num, expected in test_cases:
    result = mySqrt(num)
    status = "✓" if result == expected else "✗"
    print(f"{status} mySqrt({num}) = {result} (expected: {expected})")
    
    # Verify the result
    if result * result <= num < (result + 1) * (result + 1):
        print(f"  Verification: {result}² = {result * result} <= {num} < {(result + 1) * (result + 1)}")
    print() 