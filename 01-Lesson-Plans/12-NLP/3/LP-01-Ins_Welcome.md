## 12.3 Lesson Plan - Text Extraction

---

### Overview

This lesson introduces the concepts of POS tagging and named entity recognition. Students will practice both techniques using spacy, a model-based tool for natural language processing in Python.

### Class Objectives

By the end of the unit, students will be able to:

* Understand spacy capabilities and where to find documentation		
		
* Be able to use POS tagged text to extract specific words	

* Use dependency parsed text to extract descriptors		

* Extract specific types of entities from text		

* Correlate text features to real-world series like stock prices

* Create a dashboard from NLP sentiment features	

### Instructor Notes

* It may not be immediately obvious to students why POS tagging and named entity extraction are important techniques in natural language processing. While their outputs will not always be directly used for analysis, these processes are critical for sifting through text to its most important or pertinent aspects.

* Be sure to emphasize the use of correct preprocessing, which is different for every use case - in this class, hardly any preprocessing will be needed. 

* The activities today may be challenging for students as they introduce unfamiliar concepts and are very open-ended. Be sure to provider support along with your TA's, and spend some time in review to ask why students made certain choices in their projects. 

### Files

[Lesson 12.3 Slides](https://docs.google.com/presentation/d/1Z_y26sYoNnuKd_sOd38MHf_Qu6xo33uufneRqPFT6ho/edit#slide=id.p)

[Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome Class (5 mins)

Welcome students back to class. Today's class will introduce a few new concepts, but will also help put everything together that we've learned in this unit. We'll work with spacy, another useful tool for general-purpose NLP, and go through a few activities that make use of this tool and others from this unit. The activities today should be rewarding and fun, and students are encouraged to think about out of the box approaches to meet the requirements. Pause for questions about either the homework or previous lessons, then open the slides to the introduction on spacy. 

### 2. Intro to spacy

Tell students that to implement part of speech tagging and named entity recognition (more on these later), we will be using spacy. 

* Spacy is different from NLTK in that it is mainly statistical-based instead of rule-based, meaning that spacy's core functions depend on language models learned from tagged text instead of programmed rules. This makes spacy more flexible and in many cases more accurate than some of the NLTK tools. 

* We will be using spacy for part of speech tagging, named entity recognition, and dependency parsing. These tasks are more suitable for model-based solutions because they are complex and depend highly on context.

* In addition, spacy also provides tools for tasks like tokenization and lemmatization, which we've already learned with NLTK, and creating word vectors, which is beyond the scope of this unit but is a foundation for deep learning for NLP.

* In comparison to NLTK, spacy's language models trades off accuracy for speed, so if the corpus is large then students may prefer a simpler, rule-based solution.

Ask students to check out spacy's documentation at https://spacy.io/usage
