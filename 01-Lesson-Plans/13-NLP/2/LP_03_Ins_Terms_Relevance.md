### 3. Instructor Do: Terms relevance (Understanding TF-IDF) (10 mins)

**Files:**

* [Lesson 13.2 Slides](#)
* [03_Ins_Terms_Relevance.ipynb](Activities/03-Ins_Terms_Relevance/Solved/03_Ins_Terms_Relevance.ipynb)

Start this activity by opening the lesson slides on the **Terms Relevance (Understanding TF-IDF)** section and highlighting the following points:

* Analyzing text could be confusing due to human speech complexity, that's why term relevance is important it since offers a way to understand how important a word is to a document in a collection of documents or corpus.

* TF-IDF is a weighting factor composed by the term frequency (TF) and the inverse document frequency (IDF).

* Do not invest to much time on the TF-IDF formulas, just explain how they work in general, in contrast invest a little more time on the rationale behind these measures.

* If you are new to this topic, you can learn more about it on the[tf-idf article on Wikipedia](https://en.m.wikipedia.org/wiki/Tf%E2%80%93idf), the [text feature extraction section on the `sklean` user guide](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) as well as on [this article on KDnuggets](https://www.kdnuggets.com/2018/08/wtf-tf-idf.html) where TF-IDF is manually calculated.

* Finish the presentation by explaining what the bag of words representation is, remark that this method by itself could be useful to analyze single documents.

After finishing the presentation it's time to show how TF-IDF can be done with Python using the `sklearn` library; open the [Jupyter starter file](Activities/03-Ins_Terms_Relevance/Unsolved/03_Ins_Terms_Relevance.ipynb) and remark the following about the initial imported libraries:

* `nltk` and `nltk.corpus` are used to retrieve the [Reuters Corpus](https://www.nltk.org/book/ch02.html#reuters-corpus).

* From `sklearn` the [`CountVectorizer` class](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) will be use to implement the bag of words method, the [`TfidfVectorizer` class](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) will be used to calculate the TF-IDF.

Continue the explanation by live coding the solution and highlight the following:

* The Reuters Corpus is initially downloaded for convenience to ensure it's available for the activity.

  ```python
  nltk.download('reuters')
  ```

* The `reuters.fileids()` method retrieves a list with all the documents unique identifiers in the corpus.

* After selecting a single document from the Reuters Corpus, an instance of the `CountVectorizer()` class is created by indicating that English stop words will be ignored.
  ```python
  vectorizer = CountVectorizer(stop_words='english')
  ```

* Next the [`fit_transform()` method](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer.fit_transform) will retrieve a matrix with the terms counting, in this example a single document is passed as parameter, but also a list of documents can be passed instead.
  ```python
  X = vectorizer.fit_transform([doc_text])
  ```

* Once the term-document matrix is calculated the `get_feature_names()` method is used to retrieve the list of unique words found.

* If the `X` matrix is printed, you will notice that it contains row data that shows the counting of each term in the document, where each term is represented by a tuple where the first element is the number of document and the second element is the term's numeric identifier.
  ![Raw term-document matrix data](Images/raw_bag_of_words.png)

* A more human readable version of the _bag of words_ is created with the following DataFrame.
  ![term-document matrix as a dataframe](Images/df_bag_of_words.png)

To calculate the TF-IDF a set of 1000 documents from the Reuters Corpus is used as follows:

* A list of 1000 documents is created by taking the first 1000 document ids from the Reuters Corpus.
  ```python
  all_docs_id = reuters.fileids()
  corpus_id = all_docs_id[0:1000]
  corpus = [reuters.raw(doc) for doc in corpus_id]
  ```

* Next a `TfidfVectorizer()` instance is created by passing the stop words in English as parameter.
  ```python
  vectorizer = TfidfVectorizer(stop_words='english')
  ```

* Following the `fit_transform()` method is called passing the 1000 documents collection as parameter; a matrix with the TF-IDF value for each term on every single document is retrieved.
  ```python
  X_corpus = vectorizer.fit_transform(corpus)
  ```

* The shape of the matrix gives some interesting information. There is a row per document and a column for each term found in the corpus.
  ![TF-IDF matrix shape rationale](Images/tf_idf_matrix.png)

* Finally to create a human readable TF-IDF matrix a DataFrame is created, it's important to remark that the mean value of TF-IDF per term is used to create the DataFrame.
  ![TF-IDF DataFrame](Images/tf_idf_df.png)

* Close the activity by presenting the highest and lowest ten TF-IDF scores by mentioning that highest values normally represent more interesting terms for analysis than lowest values.

* If there is time ask the class what they think about the numbers identified as terms (tokens) by the algorithm. In fact the importance of these terms resides on the context of the documents; for example a year or an amount could be relevant if you are talking about an historical fact.
