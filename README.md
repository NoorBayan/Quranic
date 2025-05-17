<p align="center">
  <img src="https://raw.githubusercontent.com/NoorBayan/Quranic/main/Images/logo.jpg" alt="Quranic Corpus Logo" width="250px"/>
</p>

# The Quranic Treebank: A Comprehensive Linguistic Resource for Classical Arabic

Welcome to the **Quranic Treebank**, a groundbreaking linguistic resource meticulously crafted to unlock the rich and complex tapestry of Classical Arabic as manifested in the Holy Quran. This comprehensive dataset empowers scholars, linguists, computational researchers, and application developers with an unparalleled depth of information, enabling profound exploration into the intricacies of Quranic grammar, morphology, and syntax.

This resource is not merely a collection of text but a deeply annotated corpus, designed to be **computationally accessible and linguistically robust**, serving as a foundational benchmark for research and development in Arabic Natural Language Processing (NLP).

---

## Table of Contents
* [Bridging Tradition and Technology](#bridging-tradition-and-technology)
* [Key Highlights & Features](#key-highlights--features)
* [Deep Dive into the Data Structure](#deep-dive-into-the-data-structure)
  * [Core & Positional Information](#1-core--positional-information)
  * [Orthographic Representations](#2-orthographic-representations)
  * [Morphological Analysis](#3-morphological-analysis)
  * [Syntactic Analysis (Hybrid Framework)](#4-syntactic-analysis-hybrid-framework)
* [IIRAB Vis: Interactive Syntactic Visualization Tool](#iirab-vis-interactive-syntactic-visualization-tool)
  * [Key Visualization Features](#key-visualization-features)
  * [Experience IIRAB Vis: Interactive Demo (Google Colab)](#experience-iirab-vis-interactive-demo-google-colab)

---

## Bridging Tradition and Technology

The Quranic Treebank aims to serve a diverse audience, from seasoned academics advancing cutting-edge research in historical linguistics and NLP, to students of Arabic and Islamic studies seeking to deepen their comprehension of the Quran's linguistic miracle. By providing a systematic, multi-layered analysis, this corpus empowers users to:

*   **Conduct Advanced Linguistic Research:** Investigate complex grammatical phenomena, morphological patterns, and syntactic structures.
*   **Develop NLP Applications:** Train and evaluate models for parsing, morphological analysis, diacritization, machine translation, and more.
*   **Enhance Quranic Studies:** Facilitate a nuanced understanding of Quranic Arabic for students and researchers, including non-native speakers.
*   **Create Educational Resources:** Build innovative tools and platforms for teaching and learning Classical Arabic and Quranic sciences.

---

## Key Highlights & Features

*   🌟 **Comprehensive Coverage:** Encompasses the **entire text of the Holy Quran**, ensuring exhaustive representation.
*   📚 **Multi-Layered Annotation:** Offers granular analysis across **orthographic, morphological, and syntactic layers**, all meticulously interlinked.
*   💻 **Computationally Engineered:** Specifically designed for **machine readability and computational processing**, addressing limitations of previous resources.
*   🔗 **Hybrid Syntactic Framework:** Implements a novel hybrid **Constituency and Dependency** analysis, capturing the nuanced syntax of Classical Arabic.
*   🔍 **Meticulous Detail:** Each token is enriched with detailed annotations, reflecting deep linguistic insight and validated by experts against authoritative grammatical references.
*   🌐 **Publicly Accessible:** Freely available to the global research community to foster collaboration and innovation.

---

## Deep Dive into the Data Structure

The Quranic Treebank is organized as a primary tabular dataset (extended CoNLL-X format) where each row represents a token. The columns provide rich linguistic information:

### 1. Core & Positional Information
*   `tid`: Unique sequential identifier for each token entry.
*   `sentence_id`, `verse_id`, `word_id`, `tok_id`: Hierarchical identifiers for sentences (NLP-defined), Quranic verses, words, and tokens within words.
*   `location`: Traditional Quranic location code (Surah:Verse:Word:Token).
*   `chapter_id`: Numerical identifier for the Surah (Chapter).

### 2. Orthographic Representations
*   `uthmani_token` & `imlaai_token`: Token in Uthmani (Quran-specific) and Imlaai (standard CA) scripts.
*   `uthmani_unicode` & `imlaai_unicode`: Buckwalter transliteration for Uthmani and Unicode for Imlaai script.
*   `phonetic`: Phonetic transliteration of the token.
*   `trans`: English translation corresponding to the token/segment.

### 3. Morphological Analysis
*   `pos` & `pos_ar`: Part-of-Speech (POS) tags (English-based and traditional Arabic terminology).
*   `features`: Original morphological feature string (from source corpus).
*   `segment`: Identifies token as prefix, suffix, or stem.
*   `lemma` & `lemma_ar`: Word lemma (dictionary form) in transliteration/Unicode and Arabic script.
*   `root` & `root_ar`: Word root (typically triliteral) in transliteration/Unicode and Arabic script.
*   **Grammatical Features:** Detailed columns for `verb_form` (pattern), `prefix` type, `suffix` type, `verb_aspect` (perfect, imperfect, imperative), `nominal_state` (definite/indefinite), `verb_mood` (indicative, subjunctive, jussive), `nominal_case` (nominative, accusative, genitive), `derived_nouns` (active/passive participle, verbal noun), `verb_voice` (active/passive), `person`, `gender`, and `number`.

### 4. Syntactic Analysis (Hybrid Framework)
*   `special_group`: Identifies membership in special syntactic verb groups (e.g., *kāna wa-akhawātuhā*).
*   **Dependency Relations:**
    *   `rel_label` & `rel_label_ar`: Syntactic dependency relation labels (English & Arabic terminology).
    *   `ref_token_id`: Identifier of the head token in the dependency relation.
*   **Constituency Analysis:**
    *   `is_constituent`: Flag indicating if the token heads a phrasal constituent.
    *   `constituent_node`: *(Recheck definition: previously 'Classification of binary constituent relations', might need clarification or renaming based on your exact schema)*
    *   `constituent_position`: Start and end token IDs defining the span of the constituent.
    *   `constituents`: Surface string of the constituent (Uthmani script).
    *   `constituent_label`: Syntactic category label of the constituent (e.g., Nominal Sentence (NS), Verbal Sentence (VS)).

---

## IIRAB Vis: Interactive Syntactic Visualization Tool

To complement the Quranic Treebank, we introduce **IIRAB Vis**, a dedicated visualization interface built upon the Noor framework. IIRAB Vis is engineered to provide an intuitive and powerful means to explore the complex, multi-layered syntactic analyses present in the treebank.

<p align="center">
  <!-- Add a compelling screenshot of IIRAB Vis here if possible -->
  <!-- <img src="link_to_iirab_vis_screenshot.png" alt="IIRAB Vis Screenshot" width="600px"/> -->
</p>

### Key Visualization Features:

*   ✨ **Interactive Syntactic Trees:** Dynamically explore the parse structures of Quranic verses.
*   🔄 **Hybrid Representation Rendering:** Natively visualizes the integrated constituency and dependency structures.
*   👁️ **Ellipsis Resolution Display:** Clearly shows explicitly resolved elliptical constructions (from TAQDIR module).
*   📖 **Iʿrāb Integration:** Bridges computational analysis with traditional Arabic grammatical concepts, facilitating deeper understanding.
*   📊 **Rich Detail Display:** Showcases comprehensive morphological and syntactic annotations associated with each node and relation.

### Experience IIRAB Vis: Interactive Demo (Google Colab)

Get a hands-on experience with IIRAB Vis and its capabilities without any local setup through our interactive Google Colab notebook! This notebook demonstrates:

1.  Loading the Quranic Treebank data and necessary libraries.
2.  Selecting Quranic verses (by Surah and Ayah).
3.  Generating and displaying the rich, interactive syntactic visualizations.
4.  Exploring various analytical views and detailed annotations.

<p align="center">
  <a href="https://colab.research.google.com/drive/138KR4gRFv28pGiprnPcCzeiiJDyEuJBS?usp=drive_link" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
  </a>
</p>

**How to Use the Interactive Notebook:**

The notebook is designed for ease of use. As illustrated below, you can typically:
1.  **Run Setup Cells:** Execute the initial cells to load data and libraries.
2.  **Input Selection:** Use dropdowns or input fields to select a specific Surah (chapter) and Ayah (verse).
3.  **View Output:** The corresponding syntactic visualization and/or traditional Iʿrāb will be displayed.

<p align="center">
  <img src="https://raw.githubusercontent.com/NoorBayan/Quranic/main/Images/Iirab.jpg" alt="How to use the Colab Notebook - IIRAB Vis Demo" width="700px"/>
  <br/><em>Example: Navigating the Colab Notebook for verse analysis.</em>
</p>

This interactive demo is an excellent starting point for researchers, students, and developers looking to leverage the Noor framework, the Quranic Treebank, and the IIRAB Vis tool for their work on Classical Arabic.



---

