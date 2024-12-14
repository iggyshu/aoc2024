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


def find_spaces(D):
    def is_empty(index):
        return D[index] == "."

    spaces = []
    left = 0
    while left < len(D):
        while left < len(D) and not is_empty(left):
            left += 1

        if left >= len(D):
            break

        temp = left
        while temp < len(D) and is_empty(temp):
            temp += 1

        spaces.append((left, temp))

        left = temp

    return spaces


def find_files(D):
    files = []
    left = 0
    while left < len(D):

        def is_empty(index):
            return D[index] == "."

        while left < len(D) and is_empty(left):
            left += 1

        temp = left
        while temp < len(D) and D[temp] == D[left]:
            temp += 1

        files.append((left, temp))

        left = temp

    return files


def compress_full_files(blocks: List[str]) -> List[str]:
    def size(chunk):
        return chunk[-1] - chunk[0]

    D = list(blocks)

    spaces = find_spaces(D)
    files_reversed = find_files(D)[::-1]

    for i, file in enumerate(files_reversed):
        for j, space in enumerate(spaces):
            if size(file) <= size(space) and file[0] > space[0]:
                left = space[0]
                right = file[0]
                while right < file[1]:
                    D[left], D[right] = D[right], D[left]
                    left += 1
                    right += 1
                if size(file) == size(space):
                    del spaces[j]
                else:
                    spaces[j] = left, space[1]
                break

    return D


def checksum(compressed_blocks: List[str]) -> int:
    res = 0
    for id, value in enumerate(compressed_blocks):
        if value == ".":
            continue
        res += id * int(value)
    return res


def main():
    diskmap = read_diskmap()
    blocks = diskmap_to_blocks(diskmap)
    # compressed_blocks = compress(blocks)
    # chk = checksum(compressed_blocks)
    # print(f"Checksum: {chk}")
    fullfile_compression = compress_full_files(blocks)
    chk_files = checksum(fullfile_compression)
    print(f"Full file checksum: {chk_files}")


if __name__ == "__main__":
    main()
