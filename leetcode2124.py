def checkString(s: str) -> bool:
    seen_b = False
    for c in s:
        if c == 'b':
            seen_b = True
        elif seen_b:  # found 'a' after a 'b'
            return False
    return True
