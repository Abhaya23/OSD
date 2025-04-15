import random

class Yatzy:
    def __init__(self):
        self.dice = [random.randint(1, 6) for _ in range(5)]
        self.locked = [False] * 5  # Track locked dice

    def roll(self):
        """Roll unlocked dice."""
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)
        return self.dice

    def toggle_lock(self, index):
        """Lock/unlock a die (0-4)."""
        self.locked[index] = not self.locked[index]

    # Scoring Methods
    def Ones(self):
        return self.dice.count(1) * 1

    def Twos(self):
        return self.dice.count(2) * 2

    def Threes(self):
        return self.dice.count(3) * 3

    def Fours(self):
        return self.dice.count(4) * 4

    def Fives(self):
        return self.dice.count(5) * 5

    def Sixes(self):
        return self.dice.count(6) * 6

    def OnePair(self):
        counts = [self.dice.count(val) for val in range(1, 7)]
        pairs = [val * 2 for val, count in enumerate(counts, 1) if count >= 2]
        return max(pairs) if pairs else 0

    def TwoPairs(self): #
        counts = [self.dice.count(val) for val in set(self.dice)]
        pairs = [val for val, count in zip(set(self.dice), counts) if count == 2]
        return sum(pairs) * 2 if len(pairs) == 2 else 0

    def ThreeAlike(self):
        for val in set(self.dice):
            if self.dice.count(val) >= 3:
                return val * 3
        return 0

    def FourAlike(self):
        for val in set(self.dice):
            if self.dice.count(val) >= 4:
                return val * 4
        return 0

    def Small(self):
        return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0

    def Large(self):
        return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def FullHouse(self):
        counts = sorted([self.dice.count(val) for val in set(self.dice)])
        return sum(self.dice) if counts == [2, 3] else 0

    def Chance(self):
        return sum(self.dice)

    def Yatzy(self):
        return 50 if len(set(self.dice)) == 1 else 0
