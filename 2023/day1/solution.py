class Solution():
    def __init__(self, filename: str) -> None:
        with open(filename) as f:
            self._lines = f.readlines()
            for i, line in enumerate(self._lines):
                self._lines[i] = line.rstrip("\n")


    def sum_of_calibration_values(self):
        res = 0
        for line in self._lines:
            left, right = 0, len(line) - 1
            while not(line[left]).isnumeric():
                left += 1
            while not(line[right]).isnumeric():
                right -= 1
            res += int(f"{line[left]}{line[right]}")
        return res

def main():
    solution = Solution(filename="input")
    res = solution.sum_of_calibration_values()
    print(f"Sum of calibration values: {res}")

if __name__ == "__main__":
    main()
