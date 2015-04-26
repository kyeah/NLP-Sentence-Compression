from __future__ import print_function

import nltk
import sys

"""
Quick script to tokenize files with one line per sentence.
input: file to tokenize
output: filename to output
"""

num_args = len(sys.argv)

if num_args < 2 || num_args % 2 == 0:
    print("Argument parameters: <input file> <output filename> ...")

for i in range(1, len(sys.argv), 2):
    input_filename = sys.argv[i]
    output_filename = sys.argv[i+1]

    with open(input_filename, 'r') as f:
        with open(output_filename, 'w') as fw:
            for line in f:
                line = line.rstrip()
                if not line: continue
            
                tokenized = " ".join(nltk.word_tokenize(line.decode('utf-8')))
                print(tokenized.encode('utf-8'), file=fw)
