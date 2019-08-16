### 17. Instructor Do: Review Gas Cloud (10 mins)

**Files:** 

[gas_cloud.ipynb](Activities/10-Stu_Gas_Cloud/Solved/gas_cloud.ipynb)

Review the solved notebook cell by cell, pausing to ask students about their implementations when necessary. 

* To create a wordcloud, students essentially need only to copy and paste code from the previous demo. Reiterate that sometimes we need to make small changes to our preprocess function depending on what the output is going to be used for. In this case, we need to join the output because the wordcloud takes one string as input. 

Go over the challenge section next; ask students how they implemented it before reviewing the code. 

* We need to create bigrams in order to show them in a wordcloud, but how can we do this if the wordcloud module automatically word tokenizes any string we give it? One work-around is to use a character to join the two words of each bigram, essentially fooling the wordcloud tokenizer to think that they are one word. Here, we use the underscore as the join character.

```python
def process_text_bg(doc):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    re_clean = regex.sub('', doc)
    words = word_tokenize(re_clean)
    lem = [lemmatizer.lemmatize(word) for word in words]
    sw_words = [word.lower() for word in lem if word.lower() not in sw]
    bigrams = ngrams(sw_words, 2)
    output = ['_'.join(i) for i in bigrams]
    return ' '.join(output)
```

* Note that there are many "nonsense" bigrams prominent in this wordcloud. Is this a case where adding stopwords can help?

![wordcloud](Images/wordcloud.PNG)