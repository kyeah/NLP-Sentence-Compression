Paraphrastic Sentence Compression
==================================

Hello! This is a WIP course research project investigating the use of deep-linking multilingual word alignments and cross-domain parallel corpora for improving paraphrastic sentence compression results. Check back around May 15 for the completed project and associated paper. :)

## Preparing Data

### Obtaining Parallel Sentences
The parallel corpora used are:
* [Europarl DE-EN and FR-EN](http://www.statmt.org/europarl/)
* [News Commentary DE-EN](http://www.statmt.org/wmt13/translation-task.html#download)
* [de-news](http://homepages.inf.ed.ac.uk/pkoehn/publications/de-news/)

Due to large file sizes, these are excluded from the final packaging.

### Tokenizing

To tokenize sentences from parallel corpora, a tokenizer script is provided in the root directory. 

Some extra dependencies are required to run the script.
* Download the nltk library through `sudo pip install nltk`.
* Run `python` in the terminal, and `nltk.download()`. This will open an installion directory, from which you can install the necessary punkt tokenizer models.

Finally, you can run the tokenizer script.

```
python tokenizer.py <input filename 1> <output filename 1> ...
```

### Word Alignment

The unsupervised Berkeley Aligner is provided for the use of language-agnostic word alignment.

### Phrase Extraction

Koehn 2003 Implementation, or find another one online.

### Sentence Compression

## Rambling Plans
1. Map of word/phrase extracted alignments using techniques of Koehn 2003
2. For different corpora, languages
=> In Parallel + argmax combination with different languages on same corpus
=> In Series with multiple corpora (deep linking)
   -- Same domain vs. cross-domain paraphrasing (Future work: Twitter, translation into microblogging forms of communication etc.)
=> Combination of the two (Multiple different languages to start with, ORDERING of languages within series)

http://stackoverflow.com/questions/25109001/phrase-extraction-algorithm-for-statistical-machine-translation

Twitter Decompression is possible, but existing corpora cannot publically provide tweets, leading to many mining problems.
=> Rate limiting limits the ability to mine these tweets in a reasonable time span, especially for an academic project.
=> Many of the tweets have been deleted for one reason or another, drastically reducing the size of the corpus.
