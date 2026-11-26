def aliceWins(n: int) -> bool:
    if n < 10:
        return False
    remaining = n
    required = 10
    is_alice_turn = True
    while remaining >= required and required > 0:
        remaining -= required
        required -= 1
        is_alice_turn = not is_alice_turn
    # Current player cannot move
    return not is_alice_turn
