import pytest

from huffman.coding import count, make_binary_tree, compact, make_fixed_length_lookup_table

@pytest.mark.benchmark(group="lookup")
def test_benchmark_building_lookup_table(benchmark):
  with open("large/bible.txt", "r") as file:
     text = file.read()

  frequencies = count(text)
  tree = make_binary_tree(frequencies)
  tree = compact(tree)
  benchmark(make_fixed_length_lookup_table, tree)
