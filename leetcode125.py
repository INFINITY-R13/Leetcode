# LeetCode Problem 125: Valid Palindrome


def isPalindrome(s: str) -> bool:
    # Filter and convert: keep only alphanumeric chars and convert to lowercase
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if it's a palindrome by comparing with its reverse
    return filtered == filtered[::-1]


# Alternative two-pointer approach (more space-efficient)
def isPalindrome_TwoPointer(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("ab", False),
        ("aba", True),
        ("abc", False),
        ("0P", False),
        ("a.", True),
        (".,", True),
        ("A man, a plan, a canal -- Panama!", True),
        ("Was it a car or a cat I saw?", True),
        ("Madam, I'm Adam", True),
        ("12321", True),
        ("123456", False),
    ]
    
    print("Testing isPalindrome (filter approach):")
    print("=" * 60)
    for s, expected in test_cases:
        result = isPalindrome(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}'")
        print(f"  Expected: {expected}, Got: {result}")
        print()
    
    print("\n" + "=" * 60)
    print("Testing isPalindrome_TwoPointer:")
    print("=" * 60)
    for s, expected in test_cases:
        result = isPalindrome_TwoPointer(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}'")
        print(f"  Expected: {expected}, Got: {result}")
        print()