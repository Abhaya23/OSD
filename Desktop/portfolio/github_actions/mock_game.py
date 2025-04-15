import random

class Yatzy:
    def __init__(self):
        self.dice = [random.randint(1, 6) for _ in range(5)]
        self.locked = [False] * 5

    def roll(self):
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)

    def toggle_lock(self, idx):
        if 0 <= idx < 5:
            self.locked[idx] = not self.locked[idx]

    # Upper section
    def ones(self): return self.dice.count(1) * 1
    def twos(self): return self.dice.count(2) * 2
    def threes(self): return self.dice.count(3) * 3
    def fours(self): return self.dice.count(4) * 4
    def fives(self): return self.dice.count(5) * 5
    def sixes(self): return self.dice.count(6) * 6

    # Lower section
    def one_pair(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 2:
                return i * 2
        return 0

    def two_pairs(self):
        pairs = []
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 2:
                pairs.append(i)
                if len(pairs) == 2:
                    return sum(x * 2 for x in pairs)
        return 0

    def three_of_a_kind(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 3:
                return i * 3
        return 0

    def four_of_a_kind(self):
        for i in range(6, 0, -1):
            if self.dice.count(i) >= 4:
                return i * 4
        return 0

    def small_straight(self):
        return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0

    def large_straight(self):
        return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def full_house(self):
        values = set(self.dice)
        if len(values) == 2 and any(self.dice.count(x) == 3 for x in values):
            return sum(self.dice)
        return 0

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        return 50 if self.dice.count(self.dice[0]) == 5 else 0


def play_game():
    scorecard = {
        'Ones': None, 'Twos': None, 'Threes': None, 'Fours': None, 'Fives': None, 'Sixes': None,
        'One Pair': None, 'Two Pairs': None, 'Three of a Kind': None, 'Four of a Kind': None,
        'Small Straight': None, 'Large Straight': None, 'Full House': None,
        'Chance': None, 'Yatzy': None
    }

    while None in scorecard.values():
        game = Yatzy()
        rolls_left = 2  # Initial + 2 rerolls

        print("\n" + "=" * 50)
        print(f"🎯 Categories remaining: {len([v for v in scorecard.values() if v is None])}")

        while rolls_left >= 0:
            print(f"\n🎲 Roll {2 - rolls_left + 1}/3")
            print(f"Dice: {game.dice}")
            print(f"Locked positions: {[i for i, locked in enumerate(game.locked) if locked]}")

            action = input("🔒 Lock/unlock dice (0-4), e.g., '1 3', or press Enter to roll: ").strip()
            if action:
                for idx in map(int, action.split()):
                    if 0 <= idx <= 4:
                        game.toggle_lock(idx)

            game.roll()
            rolls_left -= 1

        print(f"\n🎲 Final dice: {game.dice}")

        # Build available score options
        available_scores = {
            category: getattr(game, category.lower().replace(" ", "_").replace("-", "_"))()
            for category in scorecard if scorecard[category] is None
        }

        # Show options as a numbered list
        print("\n📝 Available categories:")
        numbered_categories = list(available_scores.items())
        for idx, (cat, score) in enumerate(numbered_categories, start=1):
            print(f"{idx}. {cat}: {score}")

        # Let player choose category by number or name
        while True:
            choice = input("\nChoose a category to score (number or name): ").strip().lower()
            selected = None

            # Try numeric selection
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(numbered_categories):
                    selected = numbered_categories[index][0]

            # Try name selection
            else:
                for cat in available_scores:
                    if choice == cat.lower():
                        selected = cat
                        break

            if selected:
                scorecard[selected] = available_scores[selected]
                print(f"\n✅ Scored '{selected}' with {available_scores[selected]} points.")
                break
            print("❌ Invalid choice. Please enter the number or name of an available category.")

    # Final score display
    print("\n" + "=" * 50)
    print("🏁 Final Scorecard:")
    total = 0
    for category, score in scorecard.items():
        print(f"{category}: {score}")
        total += score or 0
    print(f"\n🎉 TOTAL SCORE: {total}")


if __name__ == "__main__":
    play_game()
