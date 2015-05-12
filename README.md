Paraphrastic Sentence Compression
==================================

Hello! This is a WIP course research project investigating the use of deep-linking multilingual word alignments and cross-domain parallel corpora for improving paraphrastic sentence compression results. Check back around May 15 for the completed project and associated paper. :)

## Preparing Data

### Obtaining Parallel Sentences
The parallel corpora used are:
* [Europarl DE-EN and FR-EN](http://www.statmt.org/europarl/)
* [News Commentary DE-EN](http://www.statmt.org/wmt13/translation-task.html#download)
* [de-news](http://homepages.inf.ed.ac.uk/pkoehn/publications/de-news/)
* [Bible DE-SP and SP-EN](http://homepages.inf.ed.ac.uk/s0787820/bible/)

Due to their large file sizes, these corpora are excluded from the final packaging. The Bible corpora need to be pre-processed out of the initial XML format, which can be done with the following command:

```
python bible_parser.py <xmlfile> <outputfile>
```

### Tokenizing

To tokenize sentences from parallel corpora, a tokenizer script is provided in the root directory. 

Some extra dependencies are required to run the script.
* Download the nltk library through `sudo pip install nltk`.
* Run `python` in the terminal, and `nltk.download()`. This will open an installion directory, from which you can install the necessary punkt tokenizer models.

Finally, you can run the tokenizer script.

```
python tokenizer.py <input filename 1> <output filename 1> ...
```

You may wish to normalize your sentences by lowercasing them.

```
cat <input> | perl lowercase.perl > <output filename>
```

## Paraphrase Extraction

### Word Alignment

The unsupervised Berkeley Aligner is provided for the use of language-agnostic word alignment. Alignment may take serveral hours and a large amount of memory, so it is recommended to submit the condor jobs provided. Make sure to submit them from within the berkeleyaligner directory, and modify the absolute paths accordingly.

### Phrase Alignment

Koehn 2003 Implementation, or find another one online. An unoptimized implementation of the word-alignment based technique found in Koehn 2003 is provided, which outputs two maps from Lang1 phrases to arrays of aligned Lang2 phrases.

```
python phrase_aligner.py <srcfile> <trgfile> <word alignment file> <srcdict filename> <trgdict filename>
```

### Extracting Paraphrases

To extract paraphrases, a universal script is provided for basic, parallel, and deep-linking paraphrase acquisition over the generated phrase-aligned dictionaries. These dictionaries are the JSON-formatted files produced in the previous step.

```
Depth 1: Bilingual single-corpus or cross-domain paraphrase extraction.
  e.g. python paraphraser.py 1 data/phrases.txt <en-de> <de-en>

Depth 2+: Deep-linking paraphrase extraction across multiple languages.
  e.g. python paraphraser.py 2 data/phrases.txt <en-de> <de-sp> <sp-en>

Parallel: Basic single-corpus extraction using multiple corpora.
  e.g. python paraphraser.py parallel data/phrases.txt <en-de> <de-en> <en-fr> <fr-en> ...
```

### Ranking Paraphrases

To rank paraphrases, an implementation of WordNet-based distributional similarity was used ([gangeli:sim](https://github.com/gangeli/sim)). You can run similarity tests with the following commands:

```
javac -cp sim/dist/sim-release.jar ParaphraseRanker.java
java -cp sim/dist/sim-release.jar:. -Dwordnet.database.dir=sim/etc/WordNet-3.1/dict -mx3g ParaphraseRanker <paraphrase file>
```