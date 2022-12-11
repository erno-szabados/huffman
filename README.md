# huffman
Huffman encoding in python based on a heap. In its current form a demonstration of the algorithm.

How does it work

Create the frequency table for a given string.
Create a heap named queue from the frequency table. The queue is created by heapifying the frequency table.
Create the Huffman tree. The tree is created by combining the two lowest frequencies and reinserting a new node that contains these as child nodes.
Create the Huffman code table by recursively iterating over the tree.
Create the Huffman code dictionary, sorted by code length.

Gives encoder and decoder routines.

Usage

Instantiate the class with the text. the constructor performs all steps required to build the dictionary. Call encode to get the encoded text.

h = huffman(text=text)
h.encode(h.text)

The python file includes a simple test that demos the use.
