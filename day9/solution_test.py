from solution import read_diskmap, diskmap_to_blocks, compress, checksum


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
