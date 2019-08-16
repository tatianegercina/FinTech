### 5. Instructor Do: Describing America (10 mins)

**Files:**

* [describing_america.ipynb](Activities/02-Stu_Describing_America/Solved/describing_america.ipynb)

Open the solved notebook and go over each section of the activity and each code block in turn. 

* For the first part of this activity, we want to create a function that returns the most common adjective from each inaugural address. We can make use of the Counter function for this:

```python
def most_freq_adj(text):
    doc = nlp(text)
    adjs = [token.text.lower() for token in doc if token.pos_ == 'ADJ']
    return Counter(adjs).most_common(1)
```

* In the second part of this activity, we want to first discover the most-used adjectives in the whole corpus. We make a small change to the function above so that it returns all adjectives in each text instead of just the most common. Then, we simply make use of the Counter function over all the adjectives.

* Next, we want to track the usage of these frequent adjectives in speeches over time. To do this, we first need to count the occurrence of each word in each speech, which we can do with a function like this:

```python
def get_counts(text, word):
    tok = word_tokenize(text)
    tok = [word.lower() for word in tok]
    return tok.count(word)
```

* Once we get the counts for each word, we can put the three lists in a DataFrame. In order to create a chart over time, though, we need a x-axis with dates. Luckily, the years of the speeches are part of each fileid - we can extract those years and turn it into a DateTime index with two lines of code:

```python
dates = [i.split('-')[0] for i in ids]
adj_df.index = pd.to_datetime(dates)
```

* The chart of word occurrences should look something like this:

![describe](Images/describe1.PNG)

* For the third part of this activity, we need to make use of the spacy's dependency parsing. The function that we define to extract words that describe "America" is below. Notice that we extract any adjectives that have a "head" (in this case, the word is describing) the word America.

```python
def describe_america(text):
    doc = nlp(text)
    adjs = [token.text.lower() for token in doc if (token.pos_ == 'ADJ' and token.head.text == 'America')]
    return adjs
```