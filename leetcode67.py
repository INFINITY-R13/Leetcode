# LeetCode 67: Add Binary


def addBinary_manual(a: str, b: str) -> str:
    """Manual bit-by-bit addition"""
    result = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1
    
    while i >= 0 or j >= 0 or carry:
        bit_a = int(a[i]) if i >= 0 else 0
        bit_b = int(b[j]) if j >= 0 else 0
        
        total = bit_a + bit_b + carry
        result.append(str(total % 2))
        carry = total // 2
        
        i -= 1
        j -= 1
    
    return ''.join(reversed(result))


def addBinary_builtin(a: str, b: str) -> str:
    """Using Python built-in conversion"""
    return bin(int(a, 2) + int(b, 2))[2:]


# Test cases
test_cases = [
    ("11", "1", "100"),           # 3 + 1 = 4
    ("1010", "1011", "10101"),    # 10 + 11 = 21
    ("0", "0", "0"),              # 0 + 0 = 0
    ("1", "1", "10"),             # 1 + 1 = 2
    ("1111", "1111", "11110"),    # 15 + 15 = 30
    ("10100000100100110110010000010101111011011001101110111111111101000000101111001110001111100001101", 
     "110101001011101110001111100110001010100001101011101010000011011011001011101111001100000011011110011", 
     "110111101100010011000101110110100000011101000101011001000011011000001100011110011010010011000000000")
]

print("Testing Binary Addition")
print("=" * 80)

for i, (a, b, expected) in enumerate(test_cases, 1):
    result_manual = addBinary_manual(a, b)
    result_builtin = addBinary_builtin(a, b)
    
    print(f"\nTest {i}:")
    print(f"  a = {a}")
    print(f"  b = {b}")
    print(f"  Expected:  {expected}")
    print(f"  Manual:    {result_manual} {'✓' if result_manual == expected else '✗'}")
    print(f"  Built-in:  {result_builtin} {'✓' if result_builtin == expected else '✗'}")
    
    # Verify both methods match
    assert result_manual == result_builtin == expected, f"Test {i} failed!"

print("\n" + "=" * 80)
print("All tests passed! ✓")