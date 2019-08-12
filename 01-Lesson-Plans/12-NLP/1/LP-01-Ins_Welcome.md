## 12.1 Lesson Plan - Introduction to NLP

---

### Overview

Welcome to the natural language processing unit! NLP is an exciting area of machine learning research and is used in a variety of contexts, from algo trading to chatbots. Today's class will explore what NLP is and give students a solid foundation on preprocessing documents for NLP as well as introduce them to some simple analytical methods. 

### Class Objectives

By the end of the class, students will be able to:

* Understand what NLP is, why we use it

* Understand and be able to implement the NLP workflow

* Demonstrate ability to tokenize texts into sentences and words, including handling punctuations and non-alpha characters gracefully

* Implement lematization and stop wording with the understanding of pros and cons of various choices	

* Experiment with a few ways of counting tokens and displaying the most frequent ones	

* Define concept of ngrams and implement with scikit-learn		

* Create wordcloud to show most frequent terms in a text		

### Instructor Notes

* There is plenty of jargon in NLP. While we try to explain things in plain English as often as possible, some terms of art like token or corpus are inescapable. One option for helping keep all the new terms straight is writing down unfamiliar terms on a slide or whiteboard so that students can refer to it as needed. 

* Each step in this lesson ties into the next, and every section is critical to learn in order to students to be able to implement the NLP workflow. Pause and ask for questions often.

* Students may expect to start off doing cool things like text modeling or sentiment analysis, and that's ok - these are coming in the next couple of lessons! However, it's good to remind them that preprocessing text, like any other kind of data, is critical to prevent the garbage in, garbage out phenomenon. 

### Files

[Lesson 12.1 Slides](https://docs.google.com/presentation/d/14mUeh58Ao2tANYEo4au54nBMiUzUL179vrwO7_HqT8E/edit)

[Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome Class (5 mins)

Welcome students back to class and explain that today is the start of the NLP unit. We'll talk about what NLP is and how it's used in finance in just a little bit, but first pose the following question. 

* When was the last time that a student made a decision - could be financial, career, or purchase - based on what they read in a news story? What about the story made them want to make that decision? 

    **Sample Answer**: I bought 10 shares of TSLA because of a news article about sales of the Model 3. The tone of the story - optimistic - as well as the specific numbers they cited made me bullish about the company. 

Take a few answers from volunteers (or call on a couple of students).

* Common answers might include statistics cited in a story, something novel that was described, or the tone in which the author wrote about something. 

* Scaling this process with computers - reading and understanding the text of documents - is a key task in NLP and is a central use case in financial applications. 

* Computers don't "understand" the stories in the way that we do, but they can identify key features - like the ones given by students - and make decisions based off of those features. 

Hopefully your students are excited and ready to dive into the content at this point! Open the slides for this lesson and begin the next section. 


### 2. Instructor Do: Intro to NLP (10 mins)

Open the slides and be sure to hit on the following talking points. Pause after each slide for questions.

* Our objectives today are focused on preprocessing - the stage of the NLP workflow when written documents are transformed into units of data that are more easily processed by a computer. 

* NLP spans a wide field of research that intersects computer science, statistics, linguistics, and other disciplines. Understanding and generating human language are two large tasks that encompass many smaller tasks - voice recognition, optical character recognition, summarization, topic representation, etc, etc. 

* Finance-specific use cases have mostly been centered around using NLP for quantitative trading. Other settings include fraud detection and chatbots for client interaction (which we will introduce in the next unit).

* The NLP workflow is characterized by four steps - preprocessing, extraction, analysis, and representation. It's not unlike a typical machine learning workflow for any type of data. However, unstructured text data can take much more work to get into useable form than structured, numerical data. 

Ask students if they have any questions about NLP in general or the direction of today's class. If not, it's time to move on to the first topic: tokenization. 