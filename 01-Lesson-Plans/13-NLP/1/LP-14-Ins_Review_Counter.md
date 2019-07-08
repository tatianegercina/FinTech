### 14. Instructor Do: Review Counter (10 mins)

**Files:** 

[counter.ipynb](Activities/08-Stu_Counter/Solved/counter.ipynb)

* To begin, we do a quick copy and paste from the previous activity in order to get a preprocessing function that can output lemmatized, stopworded, and tokenized words. We'll use this function as a helper in our main counter functions.

* Go over the first word counter function below line by line. Given a list of articles as a corpus, we have two options. We can either treat each article separately and clean and count words for each in turn, or combine all the articles into one big string and preprocess and count that string all at once. Since the latter is more efficient, both computationally and in terms of lines of code written, we choose that method. Recall that the join() method can be used to combine multiple strings into one longer string. We next run the defined process_text function over this string in order to get the list of words needed for the Counter function. Once the most frequent words are selected with most_common, all we need to do is to put them into a DataFrame. One way of transforming the dictionary is to turn it into a list of tuples first with the .items() method, as we do below. 

```python
def word_counter(corpus): 
    # Combine all articles in corpus into one large string
    big_string = ' '.join(corpus)
    processed = process_text(big_string)
    top_10 = dict(Counter(processed).most_common(10))
    return pd.DataFrame(list(top_10.items()), columns=['word', 'count'])
```

* The bigram counter is very similar. Instead of going right to the Counter function after we preprocess the text, we apply the ngram function first, with 2 as the n argument. We then return a similar DataFrame as above. 

```python
def bigram_counter(corpus): 
    # Combine all articles in corpus into one large string
    big_string = ' '.join(corpus)
    processed = process_text(big_string)
    bigrams = ngrams(processed, n=2)
    top_10 = dict(Counter(bigrams).most_common(10))
    return pd.DataFrame(list(top_10.items()), columns=['bigram', 'count'])
```