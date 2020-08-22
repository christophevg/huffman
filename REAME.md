# Huffman

> Simple and straigthforward implementation of Huffman coding - as a small exercise.

Running the script as is, it performs all steps in the Huffman coding process on a predefined "hello world" string...

```bash
$ python huffman.py
88 hello world
[('h', 1), ('e', 1), ('l', 3), ('o', 2), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
((((((('r', 1), ('d', 1)), 2), (((' ', 1), ('w', 1)), 2)), 4), ((('l', 3), ((((('h', 1), ('e', 1)), 2), ('o', 2)), 4)), 7)), 11)
 11
   4
     2
       ('r', 1)
       ('d', 1)
     2
       (' ', 1)
       ('w', 1)
   7
     ('l', 3)
     4
       2
         ('h', 1)
         ('e', 1)
       ('o', 2)
((('r', 'd'), (' ', 'w')), ('l', (('h', 'e'), 'o')))
{'r': '000', 'd': '001', ' ': '010', 'w': '011', 'l': '10', 'h': '1100', 'e': '1101', 'o': '111'}
32 0.36363636363636365 11001101101011101001111100010001
0001r1d01 1w01l001h1e1o
((('r', 'd'), (' ', 'w')), ('l', (('h', 'e'), 'o')))
{'000': 'r', '001': 'd', '010': ' ', '011': 'w', '10': 'l', '1100': 'h', '1101': 'e', '111': 'o'}
hello world
```

Command line arguments are considered a string...

```bash
$ python huffman.py hello world from cli
160 hello world from cli
[('h', 1), ('e', 1), ('l', 4), ('o', 3), (' ', 3), ('w', 1), ('r', 2), ('d', 1), ('f', 1), ('m', 1), ('c', 1), ('i', 1)]
((((((((('c', 1), ('i', 1)), 2), ((('f', 1), ('m', 1)), 2)), 4), ('l', 4)), 8), ((((('r', 2), ('o', 3)), 5), (((' ', 3), ((((('w', 1), ('d', 1)), 2), ((('h', 1), ('e', 1)), 2)), 4)), 7)), 12)), 20)
 20
   8
     4
       2
         ('c', 1)
         ('i', 1)
       2
         ('f', 1)
         ('m', 1)
     ('l', 4)
   12
     5
       ('r', 2)
       ('o', 3)
     7
       (' ', 3)
       4
         2
           ('w', 1)
           ('d', 1)
         2
           ('h', 1)
           ('e', 1)
(((('c', 'i'), ('f', 'm')), 'l'), (('r', 'o'), (' ', (('w', 'd'), ('h', 'e')))))
{'c': '0000', 'i': '0001', 'f': '0010', 'm': '0011', 'l': '01', 'r': '100', 'o': '101', ' ': '110', 'w': '11100', 'd': '11101', 'h': '11110', 'e': '11111'}
68 0.425 11110111110101101110111001011000111101110001010010100111100000010001
00001c1i01f1m1l001r1o01 001w1d01h1e
(((('c', 'i'), ('f', 'm')), 'l'), (('r', 'o'), (' ', (('w', 'd'), ('h', 'e')))))
{'0000': 'c', '0001': 'i', '0010': 'f', '0011': 'm', '01': 'l', '100': 'r', '101': 'o', '110': ' ', '11100': 'w', '11101': 'd', '11110': 'h', '11111': 'e'}
hello world from cli
```

Download a large file, e.g. from [https://corpus.canterbury.ac.nz/descriptions/](https://corpus.canterbury.ac.nz/descriptions/) and provide it to the script...

```bash
$ wget http://corpus.canterbury.ac.nz/resources/large.zip
--2020-08-19 10:36:08--  http://corpus.canterbury.ac.nz/resources/large.zip
Resolving corpus.canterbury.ac.nz (corpus.canterbury.ac.nz)... 132.181.17.8
Connecting to corpus.canterbury.ac.nz (corpus.canterbury.ac.nz)|132.181.17.8|:80... connected.
HTTP request sent, awaiting response... 302 Moved Temporarily
Location: https://corpus.canterbury.ac.nz/resources/large.zip [following]
--2020-08-19 10:36:08--  https://corpus.canterbury.ac.nz/resources/large.zip
Connecting to corpus.canterbury.ac.nz (corpus.canterbury.ac.nz)|132.181.17.8|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3256280 (3,1M) [application/zip]
Saving to: ‘large.zip’

large.zip            100%[===================>]   3,10M   367KB/s    in 10s     

2020-08-19 10:36:20 (303 KB/s) - ‘large.zip’ saved [3256280/3256280]

$ unzip large.zip -d large
Archive:  large.zip
  inflating: bible.txt               
  inflating: E.coli                  
  inflating: world192.txt            

$ python huffman.py large/bible.txt
32379136 bits
17747595 bits 0.5481182388560337 %
```

## TODO
- implement it with "real bits" ;-) 

## References

* [https://en.wikipedia.org/wiki/Huffman_coding](https://en.wikipedia.org/wiki/Huffman_coding)
