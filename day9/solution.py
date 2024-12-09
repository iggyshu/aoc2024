from typing import List


def read_diskmap(filename: str = "input.txt") -> str:
    with open(filename) as f:
        lines = f.readlines()
        return lines[0].rstrip("\n")


def diskmap_to_blocks(diskmap: str) -> List[str]:
    blocks = []
    id = 0
    for i, size in enumerate(diskmap):
        unit = ""
        if i % 2 == 0:
            # even indices are block files sizes
            unit = str(id)
            id += 1
        else:
            # odd indices are free space blocks
            unit = "."
        for _ in range(int(size)):
            blocks.append(unit)
    return blocks


def compress(blocks: List[str]) -> List[str]:
    left, right = 0, len(blocks) - 1
    D = list(blocks)

    while left < right:
        while D[left] != ".":
            left += 1
        while D[right] == ".":
            right -= 1
        if left > right:
            break
        D[left], D[right] = D[right], D[left]
        left += 1
        right -= 1

    return D


def checksum(compressed_blocks: List[str]) -> int:
    res = 0
    for id, value in enumerate(compressed_blocks):
        if value == ".":
            break
        res += id * int(value)
    return res


def main():
    diskmap = read_diskmap()
    blocks = diskmap_to_blocks(diskmap)
    compressed_blocks = compress(blocks)
    chk = checksum(compressed_blocks)
    print(f"Checksum: {chk}")


if __name__ == "__main__":
    main()
