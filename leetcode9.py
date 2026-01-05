# 9. Palindrome Number
"""Given an integer x, return true if x is a palindrome, and false otherwise."""


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original == reversed_num

# Test cases
test_numbers = [121, -121, 10, 0, 12321, 123, 1, 9009]

print("Palindrome Checker Results:")
print("-" * 40)
for num in test_numbers:
    result = is_palindrome(num)
    print(f"{num:>6} -> {'✓ Palindrome' if result else '✗ Not a palindrome'}")
