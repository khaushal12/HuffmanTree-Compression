# Name : Khaushal Rajendran
# CCID : khaushal
# ID : 1740414
# CMPUT 274, Fall 2021
# Assignment 2 Huffman Coding

import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    data = pickle.load(tree_stream)
    return data


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    leaf = tree

    while isinstance(leaf,huffman.TreeBranch):
      bit = bitreader.readbit()

      if bit == 0:
        leaf = leaf.getLeft()

      elif bit == 1:
        leaf = leaf.getRight()

    ans = leaf.getValue()
    return ans


    

def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    data = read_tree(compressed)
    read = bitio.BitReader(compressed)
    write = bitio.BitWriter(uncompressed)


    while True:
      try:
        write.writebits(decode_byte(data,read), 8)

      except Exception:
        break

    write.flush()


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pickle.dump(tree, tree_stream)

def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''
    write_tree(tree, compressed)
    table = huffman.make_encoding_table(tree)
    read = bitio.BitReader(uncompressed)
    write = bitio.BitWriter(compressed)
    EOF = False

    while not EOF:
      try:
        x = read.readbits(8)
        for i in table[x]:
          write.writebit(i)

      except EOFError:
        EOF = True
        for a in table[None]:
          write.writebit(a)
        break
    write.flush()
