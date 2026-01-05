# 13. Roman to Integer
"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M"""


def romanToInt(s: str) -> int:    
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
            total += roman_numerals[s[i + 1]] - roman_numerals[s[i]]
            i += 2
        else:
            total += roman_numerals[s[i]]
            i += 1

    return total 