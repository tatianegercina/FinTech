### 4. Student Do: Who are the Bossy Words? (15 mins)

On this activity students will use the knowledge from previous lesson to create a word cloud based on TF-IDF weights. The main objective of this activity is to let them to learn what is the difference of creating a word cloud based on term relevance instead of terms occurrence.

**Instructions:**

* [README.md](Activities/04-Stu_Bossy_Words/README.md)

**Files:**

* [bossy_words.ipynb](Activities/04-Stu_Bossy_Words/Unsolved/bossy_words.ipynb)

---

### 5. Instructor Do: Review Who are the Bossy Words? (5 mins)

Open the [solution](Activities/04-Stu_Bossy_Words/Solved/bossy_words.ipynb) and review the code by highlighting the following:

* Using a comprehension list is quite easy to retrieve the news articles that are under the `money-fx` and `money-supply` categories. The first part of the solution is to get all the document identifiers that lay on either of these categories. There are 883 documents.
  ```python
  categories = ["money-fx", "money-supply"]
  all_docs_id = reuters.fileids()
  money_news_ids = [
      doc
      for doc in all_docs_id
      if categories[0] in reuters.categories(doc)
      or categories[1] in reuters.categories(doc)
  ]
  ```
* The working corpus is created using a comprehension list that retrieves the full text of all the articles under the categories of interest. Note that the text is switched to lower case.
  ```python
  money_news = [reuters.raw(doc).lower() for doc in money_news_ids]
  ```

* When the DataFrame is created, the `sum()` method is used to calculate a measure similar to the word frequency in order to have a parameter to order the terms for creating the word cloud. You can [slack-out this link](https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html#ex:tfidf) where the rationale and validity behind the sum of TF-IDF weights is explained, it's part of the book [_Introduction to Information Retrieval_](https://nlp.stanford.edu/IR-book/) written by Christopher D. Manning, Prabhakar Raghavan and Hinrich Schütze.
  ```python
  money_news_df = pd.DataFrame(
    list(zip(vectorizer.get_feature_names(), np.ravel(X.sum(axis=0)))),
    columns=["Word", "Frequency"],
  )
  ```
* For the challenge section, the most tricky part could be to code the search by any of the terms passed as parameter. The clue is to use the [`any()` function](https://stackoverflow.com/a/16505590/4325668) in the condition of the `found_terms` comprehension list as it's explained on [this article](https://stackoverflow.com/a/25102099/4325668).
  ```python
  def retrieve_docs(terms):
    result_docs = []
    for doc_id in money_news_ids:
        found_terms = [
            word
            for word in reuters.words(doc_id)
            if any(term in word.lower() for term in terms)
        ]
        if len(found_terms) > 0:
            result_docs.append(doc_id)
    return result_docs
  ```

Ask if there are any questions before moving on.
