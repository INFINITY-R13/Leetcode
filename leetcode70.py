# LeetCode Problem 70: Climbing Stairs


def climbStairs(n):
    """
    Calculate the number of distinct ways to climb n steps.
    Each time you can climb 1 or 2 steps.
    """
    if n <= 2:
        return n
    
    prev2 = 1  # ways(1)
    prev1 = 2  # ways(2)
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


# Test cases
print("Testing Climbing Stairs:")
print(f"n=1: {climbStairs(1)} ways")  # Expected: 1
print(f"n=2: {climbStairs(2)} ways")  # Expected: 2
print(f"n=3: {climbStairs(3)} ways")  # Expected: 3
print(f"n=4: {climbStairs(4)} ways")  # Expected: 5
print(f"n=5: {climbStairs(5)} ways")  # Expected: 8
print(f"n=10: {climbStairs(10)} ways")  # Expected: 89