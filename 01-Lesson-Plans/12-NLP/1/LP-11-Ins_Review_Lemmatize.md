### 11. Instructor Do: Review Lemmatize (5 mins)

**Files:** 

[lemmatize.ipynb](Activities/06-Stu_Lemmatize/Solved/lemmatize.ipynb)

* For this exercise, the key fact to note is the order in which we apply the various processing steps. Explain to students that it's usually appropriate to lemmatize before stopwording so that the different forms of stopwords are more likely to be caught. 

```python
def process_text(article):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    re_clean = regex.sub('', article)
    words = word_tokenize(re_clean)
    lem = [lemmatizer.lemmatize(word) for word in words]
    output = [word.lower() for word in lem if word.lower() not in sw]
    return output
```

