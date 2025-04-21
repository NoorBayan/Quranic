# The Quranic Corpus

 <p align="center"> 
 <img src = "https://raw.githubusercontent.com/NoorBayan/Quranic/main/Images/logo.jpg" width = "300px"/>
 </p>


The Quranic Corpus is a groundbreaking linguistic resource that unlocks the rich and complex tapestry of the Arabic language as it appears in the sacred text of Islam. This comprehensive dataset offers scholars, linguists, and Quran application developers a wealth of information, empowering them to delve deeper into the intricacies of Quranic grammar, morphology, and syntax.

# Serving the Needs of Diverse Audiences:
The Quranic Corpus caters to a wide range of users, from seasoned academics seeking to advance their research to devout Muslims wishing to enrich their understanding of the Quran. By providing a detailed and systematic analysis of the Quranic text, the corpus empowers individuals to explore the language of the Quran in unprecedented ways.

# Key Features:
Extensive coverage: The corpus encompasses the entirety of the Quran, providing a comprehensive overview of the language used in the sacred text.
Multi-layered analysis: The corpus offers a granular analysis of the Quranic text, encompassing orthography, morphology, syntax, and dependency relations.
Detailed annotations: Each token in the corpus is enriched with meticulously crafted annotations, providing valuable insights into its linguistic features.
Versatile applications: The corpus can be leveraged for a variety of purposes, including research on Quranic Arabic, development of Quranic applications, and educational resources for learning Arabic.

# A Valuable Tool for Advancing Knowledge:
The Quranic Corpus represents a significant contribution to the field of Quranic studies and Arabic linguistics. By providing a comprehensive and accessible resource, the corpus opens up new avenues for research and empowers scholars, students, and enthusiasts alike to unlock the mysteries of the Quranic language.

# Data Structure:
The table follows a structured format with clear column names and defined data types.
The data is organized logically, grouped by related linguistic elements and their functions.

# Linguistic Elements:
## 1. Core Information:
*	*tid:* Unique identifier for *each* table row.
*	*sentence_id, verse_id, word_id, tok_id:* Serial counters for specific elements within the corpus.
*	*location:* Code representing token location within the Quran (Verse:Surah:Word:Token).
*	*chapter_id, verse_id:* Serial counters for Quranic chapters and verses.
  
## 2. Script and Representation:
*	*uthmani_token/imlaai_token*: Token representations in Uthmani and Imlaai scripts, respectively.
*	*uthmani_unicode/imlaai_unicode*: Unicode representations of corresponding tokens.
*	*phonetic, trans*: Phonetic encoding and English translation of each word.

## 3. Morphological Analysis:
*	pos, pos_ar: Part-of-speech tags (English and Arabic).
*	features: Morphological characteristics based on the original corpus.
*	segment: Token type (prefix, suffix, or stem).
*	lemma, lemma_ar: Word lemma in Unicode and Classical Arabic.
*	root, root_ar: Word root in Unicode and Classical Arabic.

## 4. Verb Conjugation:
*	Verb_form: System used to derive verbs and related words, indicating meaning variations.
*	Prefix, Suffix: Types and functions of prefixes and suffixes attached to words.
*	verb_aspect: Indicates completeness of an action (perfect, imperfect, imperative).
*	nominal_state: Definiteness or indefiniteness of nouns (definite/indefinite).
*	verb_mood: Function of verbs based on speaker's intent (indicative, subjunctive, jussive).

## 5. Syntactic Analysis:
*	special_group: Specific verb groups with unique syntactic behaviors.
*	nominal_case: Grammatical roles of nouns in sentences (nominative, accusative, genitive).
*	derived_nouns: Types of nouns formed from verbs (active participle, passive participle, verbal noun).
*	verb_voice: Active or passive voice of verbs.
*	Person, Gender, Number: Grammatical attributes indicating who/what, masculine/feminine, singular/plural/dual.

## 6. Dependency Relations:
*	rel_label, rel_label_ar: Relational dependency labels in English and Arabic.
*	ref_token_id: Identifier of the head token in a dependency relation.
*	is_constituent: Indicates whether a token is the head of a constituent (0) or not (1).

## 7. Constituent Analysis:
*	constituent_node: Classification of binary constituent relations (Dependent-Token/Constituent to Head-Token/Constituent).
*	constituent_position: Start and end positions of each constituent within the sentence.
*	constituents: Surface form of each constituent in Uthmani script.
*	constituent_label: Syntactic category of each constituent (nominal sentence, verbal sentence, etc.).

