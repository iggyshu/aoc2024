from solution import (
    read_diskmap,
    diskmap_to_blocks,
    compress,
    checksum,
    compress_full_files,
    find_spaces,
    find_files,
)


def test_read_diskmap():
    diskmap = read_diskmap("test_input.txt")

    assert len(diskmap) == 19


def test_diskmap_to_blocks():
    diskmap = read_diskmap("test_input.txt")
    blocks = diskmap_to_blocks(diskmap)
    assert "".join(blocks) == "00...111...2...333.44.5555.6666.777.888899"


def test_compress():
    diskmap = read_diskmap("test_input.txt")
    blocks = diskmap_to_blocks(diskmap)
    compressed_blocks = compress(blocks)
    assert "".join(compressed_blocks) == "0099811188827773336446555566.............."


def test_checksum():
    diskmap = read_diskmap("test_input.txt")
    blocks = diskmap_to_blocks(diskmap)
    compressed_blocks = compress(blocks)
    assert checksum(compressed_blocks) == 1928


def test_find_spaces():
    diskmap = read_diskmap("test_input.txt")
    blocks = diskmap_to_blocks(diskmap)
    spaces = find_spaces(blocks)
    assert spaces == [
        (2, 5),
        (8, 11),
        (12, 15),
        (18, 19),
        (21, 22),
        (26, 27),
        (31, 32),
        (35, 36),
    ]


def test_find_files():
    diskmap = read_diskmap("test_input.txt")
    blocks = diskmap_to_blocks(diskmap)
    spaces = find_files(blocks)
    assert spaces == [
        (0, 2),
        (5, 8),
        (11, 12),
        (15, 18),
        (19, 21),
        (22, 26),
        (27, 31),
        (32, 35),
        (36, 40),
        (40, 42),
    ]


def test_compress_full_files():
    diskmap = read_diskmap("test_input.txt")
    blocks = diskmap_to_blocks(diskmap)
    print("UNCOMPRESSED: " + "".join(blocks))
    compressed_blocks = compress_full_files(blocks)
    print("COMPRESSED: " + "".join(compressed_blocks))
    assert "".join(compressed_blocks) == "00992111777.44.333....5555.6666.....8888.."
    assert checksum(compressed_blocks) == 2858
