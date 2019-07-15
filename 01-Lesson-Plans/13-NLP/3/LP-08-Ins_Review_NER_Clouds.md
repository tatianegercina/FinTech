### 8. Instructor Do: Review NER Clouds (10 mins)

**Files:**

* [ner_clouds.ipynb](Activities/04-Stu_NER_Clouds/Solved/ner_clouds.ipynb)

Open the solved notebook and walk through the activity code.

* As with most NLP tasks, it's advantageous to manually inspect a few of the documents in a corpus if you're unfamiliar with the corpus in order to understand it better. Here, we can use the displacy tool to make this easier for us.

* Having decided to extract organizations and geopolitcal entities, we can use the following code to extract them from the corpus. 

```python
doc = nlp(articles)
entities = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'ORG']]
```

* Before creating the wordcloud, remember that we need to do a little preprocessing. First, the wordcloud only takes in a single string, so we need to join all the entities together. Before doing this, though, we should make all entities lowercase and replace spaces with underscores so that multi-word entities are not split apart. 

```python
entities = [i.lower().replace(' ', '_') for i in entities]
```

![ner](Images/ner1.png)

Ask students to talk about their own strategies for selecting entity types and whether their selections resulted in informative wordclouds.


