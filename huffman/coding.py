#!/bin/env python

def count(text):
  '''
  counts occurences of all characters in the text, returning them as a list of
  tuples ( letter, frequency )
  '''
  return [ (char, text.count(char)) for char in set(text) ]

def make_binary_tree(tree):
  '''
  makes a binary tree by grouping tuples with the smallest frequencies, creating
  intermediate nodes with the sum of these frequencies:
  '''
  while len(tree) > 1:
    tree.sort(key=lambda x:x[1])
    tree = [ ( ( tree[0], tree[1] ), tree[0][1] + tree[1][1] ) ] + tree[2:]
  return tree[0]

def dump(tree, depth=0):
  '''
  supporting function to more visually dump a tree
  '''
  try:
    l, r = tree[0] # this can fail when r isn't there -> ValueError
    print("  "*depth, tree[1])
    dump(l, depth+1)
    dump(r, depth+1) 
  except ValueError:
    print("  "*depth, tree)

def compact(tree):
  '''
  removes the frequencies from the tree ( (l, r), freq ) -> (l, r)
  '''
  try:
    l, r = tree[0] # this can fail when r isn't there -> ValueError
    return ( compact(l), compact(r) ) # here it would be too late ;-)
  except ValueError:
    return tree[0]

def make_encoding(tree, prefix='', encoding={}):
  '''
  traverses the tree, constructing a dictionary with the corresponding encoding
  '''
  try:
    l, r = tree # this can fail when r isn't there -> ValueError
    make_encoding(l, prefix+"0", encoding)
    make_encoding(r, prefix+"1", encoding) # here it would be too late ;-)
  except ValueError:
    encoding[tree] = prefix
  return encoding

def encode(text, encoding):
  '''
  encodes each character according to an encoding dictionary
  '''
  return "".join( [ encoding[char] for char in text ] )

def decode(code, tree):
  '''
  decodes characters, traversing the encoding tree up to a leave
  '''
  chars = []
  node = tree
  for direction in code:
    node = node[int(direction)]
    if len(node) == 1:
      chars.append(node)
      node = tree
  return "".join(chars)

def pack(tree):
  '''
  serializes a binary encoding tree.
  0 bit indicates a node in the tree, 1 a leaf followed by an 8 bits character.
  e.g. ( 'a', ('b', ('c', 'd'))) becomes 01a01b01c1d

  '''
  if len(tree) == 1: return "1" + tree
  return "0" + pack(tree[0]) + pack(tree[1])

def unpack(packed):
  '''
  deserializes a binary encoding tree
  e.g. 01a01b01c1d becomes ( 'a', ('b', ('c', 'd')))
  '''
  if packed[0] == "1":
    return packed[1], packed[2:]
  else:  # p[0] == "0"
    l, packed = unpack(packed[1:])
    r, packed = unpack(packed)
  return (l, r), packed


if __name__ == "__main__":
  import sys

  text = "hello world"
  verbose = True

  if len(sys.argv) > 1:
    try:
      with open(sys.argv[1], "r") as file:
        text = file.read()
      verbose = False
    except:
      text = " ".join(sys.argv[1:])

  if verbose:
    print(len(text) * 8, text)
  else:
    print(len(text) * 8, "bits")
  # 88 hello world

  frequencies = count(text)
  if verbose: print(frequencies)
  # [('h', 1), ('e', 1), ('l', 3), ('o', 2), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]

  tree = make_binary_tree(frequencies)
  if verbose: print(tree)
  # ((((((('r', 1), ('d', 1)), 2), (((' ', 1), ('w', 1)), 2)), 4), ((('l', 3), ((((('h', 1), ('e', 1)), 2), ('o', 2)), 4)), 7)), 11)
  if verbose: dump(tree)
  # 11
  #   4
  #     2
  #       ('r', 1)
  #       ('d', 1)
  #     2
  #       (' ', 1)
  #       ('w', 1)
  #   7
  #     ('l', 3)
  #     4
  #       2
  #         ('h', 1)
  #         ('e', 1)
  #       ('o', 2)

  tree = compact(tree)
  if verbose: print(tree)
  # ((('r', 'd'), (' ', 'w')), ('l', (('h', 'e'), 'o')))

  encoding = make_encoding(tree)
  if verbose: print(encoding)
  # {'r': '000', 'd': '001', ' ': '010', 'w': '011', 'l': '10', 'h': '1100', 'e': '1101', 'o': '111'}

  c = encode(text, encoding)
  if verbose:
    print(len(c), len(c)/(len(text)*8), c)
  else:
    print(len(c), "bits", len(c)/(len(text)*8), "%")
  # 32 0.36363636363636365 11001101101011101001111100010001

  packed = pack(tree)
  if verbose: print(packed)
  # 0001r1d01 1w01l001h1e1o

  unpacked = unpack(packed)[0]
  if verbose: print(unpacked)
  # ((('r', 'd'), (' ', 'w')), ('l', (('h', 'e'), 'o')))

  decoded = decode(c, unpacked)
  if verbose: print(decoded)
  # hello world
