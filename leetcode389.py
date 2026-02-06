# LeetCode 389: Find the Difference


# Solution 1: XOR Approach (Most Efficient)
def findTheDifference_xor(s: str, t: str) -> str:
    result = 0
    
    # XOR all characters in both strings
    for char in s:
        result ^= ord(char)
    
    for char in t:
        result ^= ord(char)
    
    return chr(result)


# Solution 2: Sum Difference (Most Concise)
def findTheDifference_sum(s: str, t: str) -> str:
    return chr(sum(ord(c) for c in t) - sum(ord(c) for c in s))


# Solution 3: Counter/HashMap
def findTheDifference_counter(s: str, t: str) -> str:
    from collections import Counter
    
    count_s = Counter(s)
    count_t = Counter(t)
    
    for char in count_t:
        if count_t[char] > count_s.get(char, 0):
            return char


# Solution 4: Sorted Approach
def findTheDifference_sorted(s: str, t: str) -> str:
    s_sorted = sorted(s)
    t_sorted = sorted(t)
    
    for i in range(len(s)):
        if s_sorted[i] != t_sorted[i]:
            return t_sorted[i]
    
    return t_sorted[-1]


# Test cases
def test_solutions():
    test_cases = [
        ("abcd", "abcde", "e"),
        ("", "y", "y"),
        ("a", "aa", "a"),
        ("ae", "aea", "a"),
    ]
    
    solutions = [
        ("XOR", findTheDifference_xor),
        ("Sum", findTheDifference_sum),
        ("Counter", findTheDifference_counter),
        ("Sorted", findTheDifference_sorted),
    ]
    
    for s, t, expected in test_cases:
        print(f"\nTest: s = '{s}', t = '{t}'")
        print(f"Expected: '{expected}'")
        
        for name, func in solutions:
            result = func(s, t)
            status = "✓" if result == expected else "✗"
            print(f"  {status} {name}: '{result}'")


if __name__ == "__main__":
    test_solutions()
    
    # Interactive testing
    print("\n" + "="*50)
    print("Interactive Test:")
    s = input("Enter string s: ")
    t = input("Enter string t: ")
    
    result = findTheDifference_xor(s, t)
    print(f"\nThe added letter is: '{result}'")