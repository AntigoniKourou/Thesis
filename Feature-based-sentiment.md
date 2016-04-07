Sentiment classification at both the document and sentence (or clause) levels are useful, but
* They do not find what people liked and disliked.
* They do not identify the targets of opinions, i.e. Entities and their aspects. Without knowing targets, opinions are of limited use. We need to go to the entity and aspect level.

Much of the research is based on online reviews. For reviews, aspect-based sentiment analysis is easier because the entity (i.e., product name) is usually known and reviewers simply express positive and negative opinions on different aspects of the entity.
Although similar, it is somewhat different from the traditional named entity recognition (NER). E.g., one wants to study opinions on phones given Motorola and Nokia, find all phone brands and models in a corpus, e.g., Samsung, Moto.

Extraction may use:
* frequent nouns and noun phrases
* Sometimes limited to a set known to be related to the entity of interest or
using part discriminators
* e.g., for a scanner entity
* opinion and target relations
* Proximity or syntactic dependency
* Standard IE methods
* Rule-based or supervised learning
* Often HMMs or CRFs (like standard IE)

Extract aspects using double propagation DP (Qiu et al. 2009; 2011)
* Like co-training
* an opinion should have a target, entity or aspect.
* DP extracts both aspects and opinion words.
* Knowing one helps find the other.

The DP method
* DP is a bootstrapping method
* Input: a set of seed opinion words, no aspect seeds needed
* Based on dependency grammar (Tesniere 1959).
