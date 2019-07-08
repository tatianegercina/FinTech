### 15. Instructor Do: Word Cloud (10 mins)

Frequency analysis is a useful technique, but counts of words or ngrams are difficult and boring to read through for an audience. If only there was a visualization that can achieve the same purpose, but with some color and flair. Enter word clouds! These visualizations are now pretty common and get their share of flack for not being the most rigorous of methods for visualizing text frequency, but there are still few better alternatives for quickly and viscerally summarizing a text. 

**Files:** 

[wordcloud.ipynb](Activities/09-Ins_Word_Cloud/Solved/wordcloud.ipynb)

* First, we need to import the wordcloud library, which will do most of the heavy lifting for this activity. Note that we also import matplotlib's pyplot module; although we won't be using pyplot substantively, since the wordcloud library is built on top of the matplotlib library there are some useful matplotlib functions that we can use to create our wordcloud. 

* We can copy over most of the preprocessing code from previous activites. Alert students to one small but important change - whereas before we were returning a list of words, this time we want to return one string instead. So, as a last step, we use a join to create that string. We still want to lemmatize and stopword, so word tokenizing is necessary as an intermediate step. But, since the wordcloud funciton takes only a single string as an argument, we must join these words back together in the preprocessing function. 

```python
def process_text(doc):
    sw = set(stopwords.words('english'))
    regex = re.compile("[^a-zA-Z ]")
    re_clean = regex.sub('', doc)
    words = word_tokenize(re_clean)
    lem = [lemmatizer.lemmatize(word) for word in words]
    output = [word.lower() for word in lem if word.lower() not in sw]
    return ' '.join(output)
```

* Creating the wordcloud itself is easy - two lines will do it. Tell students that the wordcloud function does a lot of things in the background that we've done explicity, like tokenizing and counting words, and then sizes each word that is displayed based on the frequency with which it appears in the text. Do the words that show up largest here make sense for the topic, "gold"? (It's possible that you'd want to add some additional stopwords here, since some of the largest words don't seem informative in this context.)

![cloud1](Images/cloud1.PNG)

* There are many ways to customize your word cloud. Some of the most basic include changing the size and the maximum number of words that appear in it. If we think the cloud above was too crowded, for example, we can reduce the maximum words argument and make it a little bigger. 

![cloud2](Images/cloud2.PNG)