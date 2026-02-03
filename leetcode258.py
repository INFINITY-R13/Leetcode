# LeetCode Problem 258: Add Digits


def addDigits(num: int) -> int:
    """
    Repeatedly add all digits until the result has only one digit.
    
    Approach 1: Simulation
    """
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num


def addDigits_optimized(num: int) -> int:
    """
    Repeatedly add all digits until the result has only one digit.
    
    Approach 2: Mathematical (Digital Root)
    """
    if num == 0:
        return 0
    return 1 + (num - 1) % 9


# Test cases
test_cases = [
    0,
    9,
    10,
    38,
    99,
    123,
    456,
    1234,
    9999,
]

print("Testing Simulation Approach:")
print("-" * 40)
for num in test_cases:
    result = addDigits(num)
    print(f"Input: {num:4d} -> Output: {result}")

print("\n" + "=" * 40)
print("Testing Optimized Approach:")
print("-" * 40)
for num in test_cases:
    result = addDigits_optimized(num)
    print(f"Input: {num:4d} -> Output: {result}")

# Verify both approaches give same results
print("\n" + "=" * 40)
print("Verification (both methods match):")
print("-" * 40)
all_match = True
for num in test_cases:
    result1 = addDigits(num)
    result2 = addDigits_optimized(num)
    match = "✓" if result1 == result2 else "✗"
    print(f"{match} Input: {num:4d} -> Method1: {result1}, Method2: {result2}")
    if result1 != result2:
        all_match = False

print("\n" + "=" * 40)
if all_match:
    print("✓ All tests passed! Both methods produce identical results.")
else:
    print("✗ Mismatch detected!")