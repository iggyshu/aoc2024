class Solution():
    _digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

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

    def sum_of_calibration_values_with_digits(self):
        res = 0
        for line in self._lines:
            left, right = 0, len(line) - 1
            while left + 1 < len(line) and not(line[left]).isnumeric():
                left += 1
            while right > 0 and not(line[right]).isnumeric():
                right -= 1
            left_val, right_val = line[left], line[right]
            for key, val in self._digits.items():
                loc = line.find(key)
                rloc = line.rfind(key)
                if 0 <= loc <= left:
                    left_val = val
                    left = loc
                if 0 <= rloc >= right:
                    right_val = val
                    right = rloc
            sol = f"{left_val}{right_val}"
            print(f"solution to line ({line}), ({sol})")
            res += int(f"{left_val}{right_val}")
        return res


def main():
    solution = Solution(filename="input")
    res_one = solution.sum_of_calibration_values()
    print(f"Sum of calibration values: {res_one}")
    res_two = solution.sum_of_calibration_values_with_digits()
    print(f"Sum of calibration values with digits: {res_two}")

if __name__ == "__main__":
    main()
