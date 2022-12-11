# Copyright 2022 Erno Szabados
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from heapq import heappush, heappop, heapify

# a class to implement the huffman algorithm using heapq.

class huffman:
    """A class to implement the huffman algorithm."""
    def __init__(self, text) -> None:
        """Initialize the huffman class."""
        self.freq_table = {}
        self.tree = []
        self.queue = []
        self.code_table = {}
        self.text = text
        self._create_freq_table(self.text)
        self.create_queue()
        self.create_tree()
        self.create_code_table()

    def _create_freq_table(self, text):
        """Create the frequency table for a given string.
           items in the table are of the form (char, freq).
           """
        self.freq_table = {}
        for char in text:
            if char in self.freq_table:
                self.freq_table[char] += 1
            else:
                self.freq_table[char] = 1

    def create_queue(self):
        """Create a queue from the frequency table.
           The queue is a list of tuples of the form (freq, char).
           The queue is created by heapifying the frequency table.
           """
        self.queue = [[t[1], t[0]] for t in list(self.freq_table.items())]
        heapify(self.queue)

    def create_tree(self):
        """Create the huffman tree.
           The tree is a list of tuples of the form (char, freq).
           The tree is created by combining the two lowest frequencies."""
        for _ in range(0, len(self.queue) - 1):
            l, r = heappop(self.queue), heappop(self.queue)
            '''The tuple is of the form (freq, char, left, right)'''
            z = [l[0] + r[0], '', l, r]
            heappush(self.queue, z)
        self.tree = heappop(self.queue)

    def _create_code_table(self, subtree, code=''):
        """Create the huffman code table by recursively iterating over the tree.
           The code table is a dictionary of the form {char: code}
           The tree is a list of tuples of the form (freq, char, left, right)"""
        # recursively iterate over the tree
        # l, r may be None or subtrees 
        _, c, l, r, *_ = subtree + [None] * 10
        if type(l) is list:
            self._create_code_table(l, code + '0')
        if type(r) is list:
            self._create_code_table(r, code + '1')
        if c != '':
            self.code_table[c] = code

    def create_code_table(self):
        """Create the huffman code table.
           The code table is a dictionary of the form {char: code}
           The tree is a list of tuples of the form (freq, char, left, right)
           The code table is sorted by the length of the code."""
        self._create_code_table(self.tree)
        self.code_table = dict(sorted(self.code_table.items(), key=lambda item: len(item[1])))
        print("Code table:")
        print(self.code_table)

    def encode(self, text):
        """Encode a string using the huffman code table."""
        code = ''
        for char in text:
            code += self.code_table[char]
        return code

    def decode(self, code):
        """Decode a string using the huffman tree."""
        decoded = ''
        subtree = self.tree
        for bit in code:
            if bit == '0':
                subtree = subtree[2]
            else:
                subtree = subtree[3]
            if subtree[1] != '':
                decoded += subtree[1]
                subtree = self.tree
        return decoded

if __name__ == "__main__":
    text = "the quick brown fox jumps over the lazy dog."
    h = huffman(text=text)
    h.encode(h.text)
    print("Encoded text:")
    print(h.encode(h.text))
    print("Decoded text:")
    print(h.decode(h.encode(h.text)))



