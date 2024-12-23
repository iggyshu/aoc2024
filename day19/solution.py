from typing import List
from collections import deque


class Solution:
    def __init__(self, filename: str = "input") -> None:
        with open(filename) as f:
            lines = f.readlines()
            self._patterns = lines[0].rstrip("\n").split(", ")
            self._designs = []
            for i in range(2, len(lines)):
                self._designs.append(lines[i].rstrip("\n"))

    def valid_designs(self) -> List[str]:
        valid = []

        for design in self._designs:
            if self.test(design):
                valid.append(design)

        return valid

    def test(self, design: str) -> bool:
        is_valid = True

        curr = deque()

        return is_valid


def main():
    pass


if __name__ == "__main__":
    main()
