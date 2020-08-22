import pytest

from huffman.coding import count, make_binary_tree, compact, make_encoding, encode, pack, unpack
from huffman.coding import decode_using_traversal, decode_using_fixed_keylength_lookup

def setup_encoded():
  with open("large/bible.txt", "r") as file:
     text = file.read()

  frequencies = count(text)
  tree = make_binary_tree(frequencies)
  tree = compact(tree)
  encoding = make_encoding(tree)
  encoded = encode(text, encoding)
  packed = pack(tree)
  unpacked = unpack(packed)[0]
  return text, encoded, unpacked

@pytest.mark.benchmark(group="decoding")
def test_decode_using_traversal(benchmark):
  text, encoded, unpacked = setup_encoded()
  decoded = benchmark(decode_using_traversal, encoded, unpacked)
  assert decoded == text

@pytest.mark.benchmark(group="decoding")
def test_decode_using_fixed_keylength_lookup(benchmark):
  text, encoded, unpacked = setup_encoded()
  decoded = benchmark(decode_using_fixed_keylength_lookup, encoded, unpacked)
  assert decoded == text
