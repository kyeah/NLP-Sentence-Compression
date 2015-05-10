# -*- coding: utf-8 -*-

import fileinput
import sys
import json

"""
This is a non-optimized implementation of the phrase alignment method described in Koehn (2003).
It utilizes word alignments and incrementally builds longer phrases from words and phrases with
adjacent alignment points.

Author: Kevin Yeh
"""
def align_phrases(srctext, trgtext, alignment):

    def extract(f_start, f_end, e_start, e_end):
        """
        Builds phrase alignments by iterating over given word alignment.
        """

        # Validate alignment points for consistency
        if f_end < 0:
            return {}
        
        for e,f in alignment:
            if ((f_start <= f <= f_end) and
               (e < e_start or e > e_end)):
                return {}

        # Align phrases (also adds unalugned foreign phrases in trgtext)
        phrases = set()
        fs = f_start

        # Iterate over foreign alignment starting point
        while True:
            fe = f_end

            # Iterate over foreign alignment endpoint
            while True:

                # Add phrase pair ([e_start, e_end], [fs, fe]) to set of phrases
                src_phrase = " ".join(srctext[i] for i in range(e_start,e_end+1))
                trg_phrase = " ".join(trgtext[i] for i in range(fs,fe+1))

                # Include alignment point for use in ranking
                phrases.add(((e_start, e_end+1), src_phrase, trg_phrase))
                fe += 1

                # fe is either aligned or out-of-bounds
                if fe in f_aligned or fe == trglen:
                    break

            fs -=1 
            # fs is either aligned or out-of-bounds
            if fs in f_aligned or fs < 0:
                break

        return phrases

    srctext = srctext.split()
    trgtext = trgtext.split()
    srclen = len(srctext)
    trglen = len(trgtext)

    # Keep track of which source and target words are aligned
    e_aligned = [i for i,_ in alignment]
    f_aligned = [j for _,j in alignment]

    aligned_phrases = set()
    for e_start in range(srclen):
        for e_end in range(e_start, srclen):
            
            # Find the minimally matching foreign phrase
            f_start, f_end = trglen-1 , -1
            for e,f in alignment:
                if e_start <= e <= e_end:
                    f_start = min(f, f_start)
                    f_end = max(f, f_end)

            # Extract phrase pairs
            phrases = extract(f_start, f_end, e_start, e_end)
            if phrases:
                aligned_phrases.update(phrases)

    return aligned_phrases

"""
Command entry point.
"""
if len(sys.argv) != 6:
    print "Format: python phrase_aligner.py <srcfile> <trgfile> <word alignment> <srcdict> <trgdict>"
    sys.exit(0)

src     = sys.argv[1]  # Tokenized source file, one sentence per line.
target  = sys.argv[2]  # Tokenized target file, one sentence per line.
aligned = sys.argv[3]  # Word alignment file in standard format.
srcdict = sys.argv[4]  # File to write phrase alignment mappings, from src => trg
trgdict = sys.argv[5]  # File to write phrase alignment mappings; from trg => src

fs = open(src, 'r').readlines()
ft = open(target, 'r').readlines()
fa = open(aligned, 'r').readlines()

elist = {}
dlist = {}

for (srctext, trgtext, alignmenttext) in zip(fs, ft, fa):
    print srctext
    print trgtext
    print alignmenttext
    
    alignment = [(int(a[0]), int(a[1])) for a in [x.split("-") for x in alignmenttext.rstrip().split(" ")]]
    phrases = align_phrases(srctext, trgtext, alignment)
    print(phrases)
    for p, a, b in phrases:
        if a in elist:
            elist[a][1].append(b)
        else:
            elist[a] = [p, [b]]

        if b in dlist:
            dlist[b][1].append(a)
        else:
            dlist[b] = [p, [a]]

with sf as open(srcdict, 'w')):
    json.dump(elist, sf)

with tf as open(trgdict, 'w')):
    json.dumpflist, sf)

# Refer to match matrix.
#             0      1      2   3  4     5   6   7    8
#srctext = "michael assumes that he will stay in the house"
#             0      1    2    3  4  5   6  7   8     9
#trgtext = "michael geht davon aus , dass er im haus bleibt"
#alignment = [(0,0), (1,1), (1,2), (1,3), (2,5), (3,6), (4,9), (5,9), (6,7), (7,7), (8,8)]

#phrases = phrase_extraction(srctext, trgtext, alignment)

# Keep track of translations of each phrase in srctext and its
# alignement using a dictionary with keys as phrases and values being
# a list [e_alignement pair, [f_extractions, ...] ]


##dlist = {}
##for p, a, b in phrases:
##    if a in dlist:
##        dlist[a][1].append(b)
##    else:
##        dlist[a] = [p, [b]]

# Sort the list of translations based on their length.  Shorter phrases first.
##for v in dlist.values():
##    v[1].sort(key=lambda x: len(x))


# Function to help sort according to book example.
##def ordering(p):
##    k,v = p
##    return v[0]
#
##for i, p in enumerate(sorted(dlist.items(), key = ordering), 1):
##    k, v = p
##    print "({0:2}) {1} {2} — {3}".format( i, v[0], k, " ; ".join(v[1]))
