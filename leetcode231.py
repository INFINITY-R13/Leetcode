def isPowerOfTwo(n):
    """
    Check if n is a power of two using bit manipulation.
    A power of two has exactly one bit set to 1.
    n & (n-1) removes the rightmost set bit, so for powers of two this equals 0.
    """
    return n > 0 and (n & (n - 1)) == 0


# Test cases
test_cases = [
    (1, True),      # 2^0 = 1
    (2, True),      # 2^1 = 2
    (3, False),     # Not a power of 2
    (4, True),      # 2^2 = 4
    (5, False),     # Not a power of 2
    (8, True),      # 2^3 = 8
    (16, True),     # 2^4 = 16
    (32, True),     # 2^5 = 32
    (64, True),     # 2^6 = 64
    (100, False),   # Not a power of 2
    (128, True),    # 2^7 = 128
    (256, True),    # 2^8 = 256
    (0, False),     # Edge case: 0
    (-1, False),    # Edge case: negative
    (-16, False),   # Edge case: negative power of 2
    (1024, True),   # 2^10 = 1024
    (1000000, False), # Not a power of 2
    (1048576, True),  # 2^20 = 1048576
]

# Run tests
print("Testing isPowerOfTwo function:\n")
print(f"{'n':<12} {'Expected':<12} {'Result':<12} {'Status':<12}")
print("-" * 50)

all_passed = True
for n, expected in test_cases:
    result = isPowerOfTwo(n)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    if result != expected:
        all_passed = False
    print(f"{n:<12} {expected:<12} {result:<12} {status:<12}")

print("-" * 50)
if all_passed:
    print("\n✓ All tests passed!")
else:
    print("\n✗ Some tests failed!")