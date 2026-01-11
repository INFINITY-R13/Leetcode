# LeetCode Problem 58: Length of Last Word


def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])

# Test cases
if __name__ == "__main__":
    # Test Example 1
    s1 = "Hello World"
    print(f"Input: \"{s1}\"")
    print(f"Output: {lengthOfLastWord(s1)}")
    print(f"Expected: 5\n")
    
    # Test Example 2
    s2 = "   fly me   to   the moon  "
    print(f"Input: \"{s2}\"")
    print(f"Output: {lengthOfLastWord(s2)}")
    print(f"Expected: 4\n")
    
    # Test Example 3
    s3 = "luffy is still joyboy"
    print(f"Input: \"{s3}\"")
    print(f"Output: {lengthOfLastWord(s3)}")
    print(f"Expected: 6\n")
    
    # Additional test cases
    s4 = "a"
    print(f"Input: \"{s4}\"")
    print(f"Output: {lengthOfLastWord(s4)}")
    print(f"Expected: 1\n")
    
    s5 = "   a   "
    print(f"Input: \"{s5}\"")
    print(f"Output: {lengthOfLastWord(s5)}")
    print(f"Expected: 1")