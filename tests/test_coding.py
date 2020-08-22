from huffman.coding import count, make_binary_tree, compact, make_encoding, encode, pack, unpack, decode

def test_roundtrip(benchmark):
  with open("large/bible.txt", "r") as file:
     text = file.read()

  frequencies = count(text)
  tree = make_binary_tree(frequencies)
  tree = compact(tree)
  encoding = make_encoding(tree)
  c = encode(text, encoding)
  packed = pack(tree)
  unpacked = unpack(packed)[0]
  decoded = benchmark(decode, c, unpacked)
  assert decoded == text

