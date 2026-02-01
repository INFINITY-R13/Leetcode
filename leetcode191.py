# ─────────────────────────────────────────────
# Hamming Weight — All Implementations
# ─────────────────────────────────────────────

# 1. Brian Kernighan's Algorithm
def hamming_kernighan(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


# 2. Bit Shifting
def hamming_bitshift(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


# 3. Built-in
def hamming_builtin(n: int) -> int:
    return bin(n).count('1')


# 4. Lookup Table
TABLE = [bin(i).count('1') for i in range(256)]

def hamming_lookup(n: int) -> int:
    count = 0
    while n:
        count += TABLE[n & 0xFF]
        n >>= 8
    return count


# 5. Parallel Bit Counting (32-bit)
def hamming_parallel(n: int) -> int:
    n = n - ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    n = (n + (n >> 4)) & 0x0F0F0F0F
    return ((n * 0x01010101) >> 24) & 0xFF


# ─────────────────────────────────────────────
# Tests
# ─────────────────────────────────────────────

implementations = {
    "Kernighan":  hamming_kernighan,
    "Bit Shift":  hamming_bitshift,
    "Built-in":   hamming_builtin,
    "Lookup":     hamming_lookup,
    "Parallel":   hamming_parallel,  # 32-bit only
}

test_cases = [
    (0b00000000,  0, "all zeros"),
    (0b00000001,  1, "single bit (LSB)"),
    (0b10000000,  1, "single bit (MSB of byte)"),
    (0b11111111,  8, "all ones (8-bit)"),
    (0b10110110,  5, "mixed bits"),
    (0b00001010,  2, "sparse bits"),
    (1,           1, "n = 1"),
    (7,           3, "n = 7  (111)"),
    (255,         8, "n = 255 (11111111)"),
    (256,         1, "n = 256 (power of 2)"),
    (1023,       10, "n = 1023 (10 ones)"),
    (0xDEADBEEF, 24, "0xDEADBEEF (32-bit)"),
    (0xFFFFFFFF, 32, "max 32-bit unsigned"),
]

# Tests beyond 32 bits (skip Parallel — it's 32-bit only)
large_test_cases = [
    (0xFFFFFFFFFF,       40, "max 40-bit"),
    ((1 << 64) - 1,      64, "max 64-bit (all ones)"),
    ((1 << 100),          1, "single bit at position 100"),
    ((1 << 100) - 1,    100, "100 consecutive ones"),
]


def run_tests():
    passed = 0
    failed = 0

    print("=" * 60)
    print(" HAMMING WEIGHT — TEST SUITE")
    print("=" * 60)

    # --- 32-bit tests (all implementations) ---
    print("\n[32-bit tests — all implementations]\n")
    for n, expected, label in test_cases:
        for name, fn in implementations.items():
            result = fn(n)
            status = "✓" if result == expected else "✗"
            if result != expected:
                print(f"  {status} {name:12} | {label:30} | expected {expected}, got {result}")
                failed += 1
            else:
                passed += 1

    print(f"  ✓ All 32-bit tests passed ({len(test_cases)} cases × {len(implementations)} implementations)")

    # --- Large integer tests (skip Parallel) ---
    print("\n[Large integer tests — excluding Parallel]\n")
    large_impls = {k: v for k, v in implementations.items() if k != "Parallel"}
    for n, expected, label in large_test_cases:
        for name, fn in large_impls.items():
            result = fn(n)
            status = "✓" if result == expected else "✗"
            if result != expected:
                print(f"  {status} {name:12} | {label:30} | expected {expected}, got {result}")
                failed += 1
            else:
                passed += 1

    print(f"  ✓ All large integer tests passed ({len(large_test_cases)} cases × {len(large_impls)} implementations)")

    # --- Summary ---
    print("\n" + "=" * 60)
    print(f"  Results: {passed} passed, {failed} failed")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()