### 4. Student Do: Bossy Words (15 mins)

On this activity, students will use the knowledge from previous lesson to create a word cloud based on TF-IDF weights. The main objective of this activity is to let them to learn what is the difference of creating a word cloud based on term relevance instead of terms occurrence.

**Instructions:**

* [README.md](Activities/04-Stu_Bossy_Words/README.md)

**Files:**

* [bossy_words.ipynb](Activities/04-Stu_Bossy_Words/Unsolved/bossy_words.ipynb)

---

### 5. Instructor Do: Review Who are the Bossy Words? (5 mins)

Open the [solution](Activities/04-Stu_Bossy_Words/Solved/bossy_words.ipynb) and review the code by highlighting the following:

* The `reuters.categories()` method retrieves all the categories for a given document as is explained on the [Reuters Corpus documentation](https://www.nltk.org/book/ch02.html#reuters-corpus).

  ```python
  >>> reuters.categories('training/9865')
  ['barley', 'corn', 'grain', 'wheat']
  ```

* A comprehension list is used in combination with the `reuters.categories()` method to retrieve the news articles that are under the `money-fx` and `money-supply` categories.

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

* When the DataFrame is created, the `sum()` method is used to calculate a measure similar to the word frequency in order to have a parameter to order the terms for creating the word cloud.

  ```python
  money_news_df = pd.DataFrame(
    list(zip(vectorizer.get_feature_names(), np.ravel(X.sum(axis=0)))),
    columns=["Word", "Frequency"],
  )
  ```

* On the challenge section, the most tricky part could be to code the search by any of the terms passed as parameter. The clue is to use the [`any()` function](https://stackoverflow.com/a/16505590/4325668) in the condition of the `found_terms` comprehension list as it's explained on [this article](https://stackoverflow.com/a/25102099/4325668).
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
