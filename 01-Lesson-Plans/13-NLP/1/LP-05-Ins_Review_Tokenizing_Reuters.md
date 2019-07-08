### 5. Instructor Do: Review Tokenizing Reuters (5 mins)

**Files:**

* [tokenizing_reuters.ipynb](Activities/02-Stu_Tokenizing_Reuters/Solved/tokenizing_reuters.ipynb)

Begin by explaining that when we perform NLP tasks, we're often doing it on many documents at once. This is one reason why keeping everything in a DataFrame is a good idea - it allowed us to keep track of the various versions of any given document, and allows us to add metadata - such as the fileid of the article in this case - to each document in a corpus.

Open the [solved file](Activities/02-Stu_Tokenizing_Reuters/Solved/tokenizing_reuters.ipynb), and discuss the following discussion points for review:

* Unlike in the demo, we want to tokenize multiple articles. Since we know how to get one article in a given category, we should be able to get all of the articles under category 'cpi' and store them in a list with a simple for loop. 

```python
raw_stories = []
ids = []
for id in cpi_ids:
    raw_stories.append(reuters.raw(id))
    ids.append(id)
```

* Just like with the raw articles, we can store sentences in a list. Note that once we apply sent_tokenize to each article, we get a list of sentences back. So, the sentence tokenized list we create is actually a list of lists. 

![sentences_list_of_lists](Images/sentences_list_of_lists.PNG)

* The word tokenized list is a little trickier to create. Recall that the sentences are stored in a list of lists. If we apply word_tokenize to each of these lists and try to store the results in another list, we'll get three layers of lists: the first of which are articles, the second of which are sentences, and the third of which are words. The activity asks for a list of tokenized words for each article, which we create with two loops. 

```python
# word tokenize all sentences
word_tokenized = []

for story in sentence_tokenized:
    # get all for each article, which is already sentence tokenized
    words = []
    for sent in story:
        words = words + word_tokenize(sent)
    # append all words for each article to the word_tokenized list
    word_tokenized.append(words)
```