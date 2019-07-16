# Tokenizing Reuters

In this activity you will practice sentence and word tokenization on some articles from the Reuters corpus. 

## Instructions

* Search the reuters corpus for articles under the category "cpi"
* Use the fileid for each story as the unique identifier
* Sentence tokenize and word tokenize each article
* Place the raw articles, the sentence tokenized articles, and the word tokenized articles in a DataFrame with appropirate column headers for each column. Each row in the sentence_tokenized column should contain a list of sentences, and each row in the word_tokenized column should contain a list of words. You should place the fileid of each story in the index of the DataFrame.

## Hint
* You should sentence tokenize the text before word tokenizing it, and apply the word tokenizer to each sentence.
* You can combine several lists into a DataFrame, and inclue column headers, by using dictionary syntax with the pandas.DataFrame function. 