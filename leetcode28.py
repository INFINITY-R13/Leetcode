# LeetCode Problem 28: Implement strStr()

def strStr(haystack, needle):
    # Handle the edge case where needle is empty
    # By convention, an empty string is found at position 0
    if not needle:
        return 0
    
    # We only need to check positions where the needle could fit
    # If needle is longer than haystack, it can't possibly match
    if len(needle) > len(haystack):
        return -1
    
    # Try each possible starting position in haystack
    # We stop at len(haystack) - len(needle) because beyond that point,
    # there isn't enough room left for the needle to fit
    for i in range(len(haystack) - len(needle) + 1):
        # Check if the needle matches starting at position i
        # This slice extracts a substring of the same length as needle
        if haystack[i:i + len(needle)] == needle:
            return i
    
    # If we've checked all positions and found no match, return -1
    return -1


# Test cases
if __name__ == "__main__":
    # Test 1: Basic match
    print(f"Test 1: strStr('hello', 'll') = {strStr('hello', 'll')}")  # Expected: 2
    
    # Test 2: Match at the beginning
    print(f"Test 2: strStr('hello', 'he') = {strStr('hello', 'he')}")  # Expected: 0
    
    # Test 3: No match
    print(f"Test 3: strStr('hello', 'world') = {strStr('hello', 'world')}")  # Expected: -1
    
    # Test 4: Empty needle
    print(f"Test 4: strStr('hello', '') = {strStr('hello', '')}")  # Expected: 0
    
    # Test 5: Needle longer than haystack
    print(f"Test 5: strStr('hi', 'hello') = {strStr('hi', 'hello')}")  # Expected: -1
    
    # Test 6: Complete match
    print(f"Test 6: strStr('abc', 'abc') = {strStr('abc', 'abc')}")  # Expected: 0
    
    # Test 7: Match at the end
    print(f"Test 7: strStr('mississippi', 'issip') = {strStr('mississippi', 'issip')}")  # Expected: 4
    
    # Test 8: Single character
    print(f"Test 8: strStr('a', 'a') = {strStr('a', 'a')}")  # Expected: 0