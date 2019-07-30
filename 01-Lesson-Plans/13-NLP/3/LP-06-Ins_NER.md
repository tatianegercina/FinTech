### 6. Instructor Demo: Named Entity Recognition (0:10 mins)

This activity introduces students to named entity recognition (NER), a process that extracts specific types of nouns ("named entities") from text. Named entities are often proper nouns, but NER tools often can also extract things like currency, dates, and times. Like POS tagging and dependency parsing, NER gives us a way of being more precise with our text analysis, only extracting the words that meet a specific grammatical or semantic criteria.

**Files:**

* Solved: [ner.ipynb](Activities/03-Ins_NER/Solved/ner.ipynb)

Open the notebook and walk through the code.

* Similar to the tokens that we used to get POS and dependencies, we can access the tagged entities through the .ents attribute and its child attributes, .text and .label_

```python
for ent in doc.ents:
    print(ent.text, ent.label_)
```

* We can also use displacy here to visually examine an article, which makes seeing the named entities a lot easier.

![ner_2](Images/ner_2.PNG)

* Again, like with with POS or dependencies, we can filter for particular types of entities with a list comprehension.

```python
print([ent.text for ent in doc.ents if ent.label_ == 'GPE'])
```

Before moving on to the next student activity, ask the class to search for spacy documentation (https://spacy.io/api/annotation#named-entities) to find out what entity types exist and what each label means. 

