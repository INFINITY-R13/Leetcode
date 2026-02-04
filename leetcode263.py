# LeetCode Problem 263: Ugly Number


def isUgly(n: int) -> bool:
    # Ugly numbers must be positive
    if n <= 0:
        return False
    
    # Divide by 2, 3, and 5 as many times as possible
    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor
    
    # If we're left with 1, all prime factors were 2, 3, or 5
    return n == 1


# Test cases
def test_isUgly():
    test_cases = [
        (6, True),      # 6 = 2 × 3
        (1, True),      # 1 has no prime factors
        (14, False),    # 14 = 2 × 7 (has prime factor 7)
        (8, True),      # 8 = 2^3
        (10, True),     # 10 = 2 × 5
        (12, True),     # 12 = 2^2 × 3
        (15, True),     # 15 = 3 × 5
        (7, False),     # 7 is prime (not 2, 3, or 5)
        (0, False),     # Not positive
        (-6, False),    # Negative numbers are not ugly
        (30, True),     # 30 = 2 × 3 × 5
        (100, True),    # 100 = 2^2 × 5^2
        (11, False),    # 11 is prime
        (25, True),     # 25 = 5^2
        (2, True),      # 2 is ugly
        (3, True),      # 3 is ugly
        (5, True),      # 5 is ugly
    ]
    
    print("Testing isUgly function:\n")
    for num, expected in test_cases:
        result = isUgly(num)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} | isUgly({num:4}) = {result:5} | Expected: {expected:5}")
    
    print("\n" + "="*50)
    print("All tests completed!")


# Run tests
if __name__ == "__main__":
    test_isUgly()