### 3. Instructor Do: Terms relevance (Understanding TF-IDF) (10 mins)

This activity introduces terms relevance from the perspective of TF-IDF (Term Frequency — Inverse Document Frequency), also students will lean how TF-IDF can be implemented using `sklearn`.

Do not invest to much time on the TF-IDF formulas, just explain how they work in general and invest a little more time on the rationale behind these measures and its implementation using `sklearn`.

**Files:**

* [Lesson 13.2 Slides](#)

* [03_Ins_Terms_Relevance.ipynb](Activities/03-Ins_Terms_Relevance/Solved/03_Ins_Terms_Relevance.ipynb)

Open the lesson slides a move to the **Terms Relevance (Understanding TF-IDF)** section and highlighting the following points:

* In a world of words analyzing text could be confusing due to human speech complexity, that's why measuring term relevance is useful since it offers a way to understand how important a word is to a document into a collection of documents or corpus.

* A **corpus** (_corpora_ in plural) is a large, structured and organized collection of text documents that normally verses on a specific matter; there are monolingual or single language corpora, as well as multilingual or multiple language corpora.

* **TF-IDF** is a weighting factor intended to measure how important a word is to a document in a corpus.

* **TF** indicates that if a word appears multiple times in a document, it can be concluded that it's relevant and should be more meaningful than other words in the same text.

* **IDF** comes to action when you're analyzing several documents. If a word also appears many times along a collection of documents, maybe it's just a frequent word and not a relevant one.

* A **high weight in TF-IDF** is reached by terms with high TF and a low document frequency of the term in the corpus, normally these are more interesting terms to analyze.

* A **low weight in TF-IDF** is reached by terms with low TF and a high document frequency of the term in the corpus, normally these are quite common terms across the corpus that could be less interesting to analyze.

* The **bag-of-words model** is a technique in NLP to represent the important words or tokens in a document without worrying about sentence structure. A bag-of-words model can then be used to compare documents based on the number of important words that they share.

After finishing the lecture slides, switch to the code demo and show how TF-IDF can be calculated with Python using the `sklearn` library; open the [Jupyter starter file](Activities/03-Ins_Terms_Relevance/Unsolved/03_Ins_Terms_Relevance.ipynb) and highlight the following points:

* `nltk` and `nltk.corpus` are used to retrieve the [Reuters Corpus](https://www.nltk.org/book/ch02.html#reuters-corpus).

* From `sklearn` the [`CountVectorizer` class](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) will be used to implement the bag of words model, and the [`TfidfVectorizer` class](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) will be used to calculate the TF-IDF.

Continue the explanation by live coding the solution and highlight the following:

* The Reuters Corpus is initially downloaded for convenience to ensure it's available for the activity.

  ```python
  nltk.download('reuters')
  ```

* The `reuters.fileids()` method retrieves a list with all the document's unique identifiers in the corpus.

* After selecting a single document from the Reuters Corpus, an instance of the `CountVectorizer()` class is created. The `stop_words='english'` parameter will ignore all English language stop words when vectorizing the text.

  ```python
  vectorizer = CountVectorizer(stop_words='english')
  ```

* The [`fit_transform()`](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.fit_transform) method retrieves a matrix of the terms counts, in this example a single document is passed as parameter, but also a list of documents can be passed instead.

  ```python
  X = vectorizer.fit_transform([doc_text])
  ```

* The `get_feature_names()` method is used to retrieve the list of unique words found.

  ```python
  words = vectorizer.get_feature_names()
  ```

When the `X` matrix is printed, you will notice that it contains raw data that shows the counting of each term represented by a tuple `(n, t)  c`; `t` is the term's numeric identifier, `n` refers to the _nth_ document where the term `t` was found and `c` is the term's counting on the document `n`. Since we have only one document on this example the first term is always `0`.
  ![Raw term-document matrix data](Images/raw_bag_of_words.png)

* A more human readable version of the _bag of words_ is created with the following DataFrame.
  ![term-document matrix as a DataFrame](Images/df_bag_of_words.png)

To calculate the TF-IDF a set of 1000 documents from the Reuters Corpus is used as follows:

* A list of 1000 documents is created by taking the first 1000 document ids from the Reuters Corpus.

  ```python
  all_docs_id = reuters.fileids()
  corpus_id = all_docs_id[0:1000]
  corpus = [reuters.raw(doc) for doc in corpus_id]
  ```

* A `TfidfVectorizer()` instance is created by passing the stop words in English as parameter.

  ```python
  vectorizer = TfidfVectorizer(stop_words='english')
  ```

* The `fit_transform()` method is called passing the 1000 documents collection as parameter; a matrix with the TF-IDF value for each term on every single document is retrieved.

  ```python
  X_corpus = vectorizer.fit_transform(corpus)
  ```

* The shape of the matrix gives some interesting information. There is a row per document and a column for each term found in the corpus.
  ![TF-IDF matrix shape rationale](Images/tf_idf_matrix.png)

* Finally, a DataFrame is created to create a human readable TF-IDF matrix. The mean value of the TF-IDF is used to create the DataFrame.
  ![TF-IDF DataFrame](Images/tf_idf_df.png)

Conclude the activity by presenting the highest and lowest ten TF-IDF scores. Explain that highest values normally represent less common and more interesting terms for analysis, they have a high term frequency (in some documents) and a low document frequency of the term in the whole collection of documents.

If there is time ask the class what they think about the numbers identified as terms (tokens) by the algorithm. In fact the importance of these terms resides on the context of the documents; for example a year or an amount could be relevant if you are talking about an historical fact.
