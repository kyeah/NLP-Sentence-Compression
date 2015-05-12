import fileinput
import sys
import json

"""
This script acquiries paraphrases over phrase-aligned dictionaries generated
from parallel bilingual corpora.

Depth 1: Bilingual single-corpus or cross-domain paraphrase extraction.
  e.g. python paraphraser.py 1 <phrases> <en-de> <de-en>

Depth 2+: Deep-linking paraphrase extraction across multiple languages.
  e.g. python paraphraser.py 2 <phrases> <en-de> <de-sp> <sp-en>

Parallel: Basic single-corpus extraction using multiple corpora.
  e.g. python paraphraser.py parallel <phrases.txt> <en-de> <de-en> <en-fr> <fr-en> ...
"""

def find_paraphrases_in_series(phrase, dicts):
    phrases = []

    # Iterate over pairs of dicts at a time
    it = iter(dicts)
    for d1 in it:
        d2 = next(it)
        translations = d1[phrase][1]
        for translation in translations:
            phrases += d2[translation][1]

    return phrases

def find_paraphrases_in_series(phrase, dicts):
    phrases = [phrase]

    # Iterate over dictionaries
    for d in dicts:
        translated_phrases = []
        for p in phrases:
            translations = d[p][1]
            translated_phrases += translations
        phrases = translated_phrases

    return phrases

def rank_phrases():
    """
    Rank paraphrases using a monolingual distributional similarity metric
    """

"""
Command entry point.
"""
dicts = []
init_phrases = []
depth = sys.argv[1]

# Depth = positive integer, or "parallel" with pairs of dicts
if depth == "parallel" and len(sys.argv) % 2 != 0:
    print("Exiting: parallel acquisition requires pairs of dictionaries.")
    sys.exit(0)

if depth != "parallel":
    depth = int(depth)
    if depth < 0:
        print("Exiting: depth must be a positive integer.") 
        sys.exit(0)

# Read in test phrases
with open(sys.argv[2], 'r') as f:
    while line = f.readLine():
        init_phrases.append(line.rstrip())

# Read in phrase-aligned dictionaries
for fn in sys.argv[3:4+depth]:
    with open(fn, 'r') as f:
        dicts.append(json.load(f))

# Acquire paraphrases
paraphrases = {}
for phrase in init_phrases:
    if depth == parallel:
        phrases = find_paraphrases_in_parallel(phrase, dicts)
    else:
        phrases = find_paraphrases_in_series(phrases, dicts)
    paraphrases[phrase] = phrases

for key in paraphrases:
    print "Phrase:", key
    for phrase in paraphrases[key]:
        print phrase
        print ""
