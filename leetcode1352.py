class ProductOfNumbers:

    def __init__(self):
        # prefix[i] = product of the last (i) non-zero numbers since the most recent 0
        # prefix[0] = 1 acts as a sentinel so that product of the whole current segment
        # is simply prefix[-1]
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Any future product that reaches back past this zero must be 0.
            # Reset the prefix list so that only numbers after this zero are kept.
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # If k is larger than the length of the current non-zero segment,
        # the requested window must contain the most recent 0 → product is 0.
        if k >= len(self.prefix):
            return 0
        # Otherwise the product of the last k numbers is
        # prefix[-1] / prefix[-1-k]
        return self.prefix[-1] // self.prefix[-1 - k]
