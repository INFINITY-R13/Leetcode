# LeetCode 405: Convert a Number to Hexadecimal


def toHex(num: int) -> str:
    """
    Convert a 32-bit integer to hexadecimal string.
    For negative integers, two's complement method is used.
    
    Args:
        num: A 32-bit integer
        
    Returns:
        Hexadecimal representation as a lowercase string
    """
    # Handle zero case
    if num == 0:
        return "0"
    
    # For negative numbers, convert to 32-bit two's complement
    # In Python, we can use bitwise AND with 0xFFFFFFFF to get the 32-bit representation
    if num < 0:
        num = num & 0xFFFFFFFF
    
    # Hexadecimal digits
    hex_chars = "0123456789abcdef"
    result = []
    
    # Convert to hexadecimal
    while num > 0:
        remainder = num % 16
        result.append(hex_chars[remainder])
        num = num // 16
    
    # Reverse since we built it backwards
    return ''.join(reversed(result))


# Test cases
def test_toHex():
    test_cases = [
        (26, "1a"),
        (-1, "ffffffff"),
        (0, "0"),
        (255, "ff"),
        (-2, "fffffffe"),
        (16, "10"),
        (1, "1"),
        (100, "64"),
        (-100, "ffffff9c"),
        (2147483647, "7fffffff"),   # Max positive 32-bit int
        (-2147483648, "80000000"),  # Min negative 32-bit int
    ]
    
    print("Running test cases...\n")
    all_passed = True
    
    for num, expected in test_cases:
        result = toHex(num)
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"{status} toHex({num:12d}) = {result:10s} (expected: {expected})")
    
    print("\n" + ("="*50))
    if all_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed! ✗")
    print("="*50)


if __name__ == "__main__":
    test_toHex()
    
    # Interactive testing
    print("\n" + "="*50)
    print("Try your own inputs:")
    print("="*50)
    
    while True:
        try:
            user_input = input("\nEnter a number (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            
            num = int(user_input)
            result = toHex(num)
            print(f"Hexadecimal: {result}")
            
            # Verification using built-in (for comparison)
            if num >= 0:
                builtin = hex(num)[2:]
            else:
                builtin = hex(num & 0xFFFFFFFF)[2:]
            print(f"Verification:  {builtin}")
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break