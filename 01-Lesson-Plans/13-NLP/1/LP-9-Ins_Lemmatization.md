### 9. Instructor Demo: Lemmatization (0:07 mins)

Lemmatization is a technique that transforms various morphologies of a word into its base form. This may sound fancy, but it's pretty intuitive. If we're looking to summarize a document with the most frequent words in it, words like "stock" and "stocks," for the most part, should mean the same, as does words like "run" and "ran." NLTK's lemmatizer takes words in different forms (past tense, plural form, etc.) and transforms them to the base form (present tense, singular).

**Files:**

Solved: [lemmatization.ipynb](\Activities\05-Ins_Lemmatization\Solved\lemmatization.ipynb)

* Note that the lemmatizer is smart enough to not only transform those words that have simple plural forms, but also those that words like "goose" that have complex plurals. 

![lemma1](Images/lemma1.PNG)

* The lemmatizer does not automatically lemmatize any part of speech - the default is noun, which means that plural forms will be tranformed to singular. If you want to lemmatize verbs or adjectives, you can use the 'pos' argument to change the default part of speech. So, changing pos to 'a' for adjective allows us to lemmatize words like "greater" to their root, "great."

![lemma2](Images/lemma2.PNG)

* Note that it's possible to lemmatize every part of speech for any given word - all we need to do is apply the lemmatize function to the word with a different pos argument on each pass. In practice, however, noun lemmatizations are usually enough, since the most informative words for most NLP analyses are nouns. It's also important to note that lemmatization is not a step one would want to apply for any kind of analysis - measures of sentiment would be biased if the words were adjective lemmatized beforehand, for example. 
