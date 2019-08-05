### 8. Instructor Do: Review Crude Stopwords (8 mins)

**Files:**

* [crude_stopwords.ipynb](Activities/04-Stu_Crude_Stopwords/Solved/crude_stopwords.ipynb)

Reiterate that stopwording is very domain and circumstance specific. Using the same set of stopwords for every corpus is rarely a good idea. The NLTK set is a good start, but chances are that you'll want to augment it with your own set after inspecting the results. 

* Note the order in which we apply the regex cleaning, word tokenizing and stopwording. 

```python
def clean_text(article):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    
    re_clean = regex.sub('', article)
    words = word_tokenize(re_clean)
    output = [word.lower() for word in words if word.lower() not in sw]
    return output
```

* Read the list of additional words that we decided to drop in the second solved implementation. Ask students if they agree with these, and which words they might add or drop from this list. 

![crude_stopwords](Images/crude_stopwords.PNG)

* Tell students that the extent to which we want to add stopwords is a trade-off. The more stopwords, the fewer words we have to look through in a final analysis. However, this also raises the chances that we delete informative words. 