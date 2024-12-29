from typing import List


class Solution():
    def __init__(self, filename: str = "input"):
        self._cards = []
        with open(filename) as f:
            for line in f:
                parts = line.rstrip("\n").split(": ")
                id = int(parts[0].lstrip("Card "))
                winning, general = parts[1].split(" | ")
                winning = [int(x) for x in winning.split(" ") if x.isnumeric()]
                general = [int(x) for x in general.split(" ") if x.isnumeric()]
                self._cards.append(Card(id, winning, general))

    def total_worth(self):
        return sum([card.worth() for card in self._cards])

class Card():
    def __init__(self, id: int, winning_numbers: List[int], numbers: List[int]) -> None:
        self.id = id
        self.winning_numbers = set(winning_numbers)
        self.numbers = numbers

    def worth(self) -> int:
        res = 0

        for num in self.numbers:
            if num in self.winning_numbers:
                if res == 0:
                    res = 1
                else:
                    res *= 2

        return res

def main():
    sln = Solution()
    total_worth = sln.total_worth()
    print(f"Total worth of the deck: {total_worth}")

if __name__ == "__main__":
    main()
