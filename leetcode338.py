# LeetCode 338: Counting Bits


def countBits(n):
    """
    Given an integer n, return an array ans of length n + 1 
    where ans[i] is the number of 1's in binary representation of i.
    """
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


# Test cases
def test_countBits():
    test_cases = [
        (2, [0, 1, 1]),
        (5, [0, 1, 1, 2, 1, 2]),
        (0, [0]),
        (1, [0, 1]),
        (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]),
    ]
    
    print("Testing countBits function...\n")
    
    for i, (n, expected) in enumerate(test_cases, 1):
        result = countBits(n)
        passed = result == expected
        
        print(f"Test Case {i}:")
        print(f"  Input: n = {n}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print(f"  Status: {'✓ PASSED' if passed else '✗ FAILED'}")
        
        # Show binary representations for better understanding
        if n <= 10:
            print(f"  Binary breakdown:")
            for j in range(n + 1):
                print(f"    {j}: {bin(j)[2:]:>4} -> {result[j]} one(s)")
        print()
    
    print("All tests completed!")


# Alternative implementations for comparison
def countBits_builtin(n):
    """Using Python's built-in bin() and count()"""
    return [bin(i).count('1') for i in range(n + 1)]


def countBits_bit_trick(n):
    """Using i & (i-1) trick"""
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans


# Run tests
if __name__ == "__main__":
    test_countBits()
    
    # Compare different implementations
    print("\n" + "="*50)
    print("Comparing different implementations:")
    print("="*50)
    
    n = 8
    result1 = countBits(n)
    result2 = countBits_builtin(n)
    result3 = countBits_bit_trick(n)
    
    print(f"\nFor n = {n}:")
    print(f"DP (right shift):  {result1}")
    print(f"Built-in:          {result2}")
    print(f"Bit trick:         {result3}")
    print(f"All match: {result1 == result2 == result3}")
