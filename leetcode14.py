# 14. Longest Common Prefix
"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string ""."""


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    strs.sort()
    first = strs[0]
    last = strs[-1]
    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
        
    return first[:i]


# Test cases
test_cases = [
    (["flower", "flow", "flight"], "fl"),
    (["dog", "racecar", "car"], ""),
    (["interspecies", "interstellar", "interstate"], "inters"),
    (["throne", "throne"], "throne"),
    ([""], ""),
    (["a"], "a"),
    (["ab", "a"], "a"),
    ([], ""),
]

print("Testing longestCommonPrefix function:\n")
for i, (input_strs, expected) in enumerate(test_cases, 1):
    result = longestCommonPrefix(input_strs)
    status = "✓ PASS" if result == expected else "✗ FAIL"
    print(f"Test {i}: {status}")
    print(f"  Input:    {input_strs}")
    print(f"  Expected: '{expected}'")
    print(f"  Got:      '{result}'")
    print()
