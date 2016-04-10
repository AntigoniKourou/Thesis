Sentiment lexicon: lists of words and expressions sentiments/opinions.
* Not just individual words, but also phrases and idioms.
* Many sentiment lexica can be found on the web. They often have thousands of terms, and are quite useful.

Sentiment words or phrases (also called polar words,opinion bearing words, etc). Many of them are context dependent, not just application domain dependent. Three main ways to compile such lists:
* Manual approach: not a bad idea for a one-time effort
* Corpus-based approach: Often use a double propagation between opinion words and the items they modify, require a large corpus to get good coverage. ---> Rely on big corpa (Hazivassiloglou and McKeown, 1997; Turney, 2002; Yu
and Hazivassiloglou, 2003; Kanayama and Nasukawa, 2006; Ding, Liu and Yu, 2008). ---> Turney, 2002) and (Yu and Hazivassiloglou, 2003) are similar, assign opinion orientations (polarities) to words/phrases. (Yu and Hazivassiloglou, 2003) is slightly different from (Turney, 2002), use more seed words (rather than two) and use log-likelihood ratio
(rather than PMI). 
Find domain opinion words is insufficient. A word may indicate different opinions in same domain. ---> Ding, Liu and Yu (2008) and Ganapathibhotla and Liu (2008) exploited sentiment consistency (both
inter and intra sentence) based on contexts. It finds context dependent opinions. Context: (adjective, aspect), e.g., (long, battery_life) It assigns an opinion orientation to the pair. Other related work (Wu and Wen, 2010; Lu et al., 2011)

* Dictionary-based approach. Typically use WordNet synsets and hierarchies to acquire opinion
words. Usually do not give domain or context dependent meanings
Start with a small seed set of opinion words.
* Bootstrap the set to search for synonyms and antonyms in
WordNet iteratively (Hu and Liu, 2004; Kim and Hovy, 2004;
Valitutti, Strapparava and Stock, 2004; Mohammad, Dunne
and Dorr, 2009). Kamps et al., (2004) proposed a WordNet distance method to
determine the sentiment orientation of a given adjective.
* Semi-supervised learning (Esuti and Sebastiani, 2005)
Use supervised learning. Given two seed sets: positive set P, negative set N. The two seed sets are then expanded using synonym and antonymy relations in an online dictionary to generate the expanded sets P' and N'. Using all the glosses in a dictionary for each term in P' U N' and converting them into a vector.
- Build a binary classifier: Tried various learners.
* Multiple runs of bootstrapping (Andreevskaia and Bergler, 2006) Basic bootstrapping with given seeds sets
(adjectives)
1. First pass: seed sets are expanded using synonym,
antonyms, and hyponyms relations in WordNet.
2. Second pass: it goes through all WordNet glosses and
identifies the entries that contain in their definitions the
sentiment-bearing words from the extended seed set and
adds these head words to the corresponding category
(+ve, -ve, neutral)
3. Third pass: clean up using a POS tagger to make sure
the words are adjectives and remove contradictions.

Each word is then assigned a fuzzy score
reflecting the degree of certainty that the word is
opinionated (+ve/-ve). The method performs multiple runs of
bootstrapping using non-overlapping seed sets.  A net overlapping score for each word is computed based on how
many times the word is discovered in the runs as +ve (or -ve) The score is normalized based on the fuzzy membership.

**Which approach to use?**
* Both corpus and dictionary based approaches
are needed.
* Dictionary usually does not give domain or
context dependent meanings. Corpus is needed for that
* Corpus-based approach is hard to find a very
large set of opinion words. Dictionary is good for that
* In practice, corpus, dictionary and manual
approaches are all needed.