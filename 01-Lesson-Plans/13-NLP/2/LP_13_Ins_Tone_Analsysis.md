### 13. Instructor Do: Tone Analysis (15 mins)

**Files:**

* [Lesson Slides](#)

* [tone_analysis.ipynb](Activities/13-Ins_Tone_Analysis/Solved/tone_analysis.ipynb)

* [keys.sh](Activities/13-Ins_Tone_Analysis/Solved/keys.sh)

On this activity students will be introduced to tone analysis and how they can score tone of human speech using the **IBM Watson Tone Analyzer service**.

Start by opening the lesson slides, go to the _Tone Analysis_ section and highlight the following:

* Tone analysis offers new possibilities to sentiment analysis since it goes beyond the simple classic classification as positive, negative or neutral and looks to understand human emotions.

* Tone analysis is a complex and costly task since it requires to train algorithms with thousands of documents that need to be previously tagged to understand the emotion behind the words.

* IBM Watson Tone Analyzer is a cloud service to analyze tone on text communications, due to the cost of analyzing tone this service is only available now in English and French.

* IBM Watson Tone Analyzer can be used via its Python API.

After the brief definition of tone analysis and the intro to IBM Watson Tone Analyzer, slack out [the URL for this service](https://cloud.ibm.com/catalog/services/tone-analyzer) and guide students on creating their IBM Cloud account and on setting up their Tone Analyzer instance. Follow the slides as a guided tour by remarking the following:

* One great advantage of IBM Cloud is that there is no need to use a credit card to access the _lite_ version of its services, student only need to fill out their personal account information.

* Ask your TAs to assist students on personal IBM Cloud account creation, it's important to every student to have his or her personal account.

* If it's possible, follow the account creation and the Tone Analyzer instance creation together with students by using your personal e-mail or a secondary e-mail to better assist students on the process.

* Remind student not to share their API keys as plain text on their code and encourage them to create environment variables instead.

Once all students have their API keys and URLs, live code the demo using the solved version of the Jupyter notebook as a guide; encourage students to follow you to give a try to this service.

While live coding the solution highlight the following:

* Install the IBM Watson Python library using `pip` as follows. This demo runs using version 3.

```bash
pip install --upgrade "ibm-watson>=3.0.3"
```

* Slack out the [Tone Analyzer API Docs link](https://cloud.ibm.com/apidocs/tone-analyzer?code=python) for future reference.

* The Tone Analyzer service is imported from the `ibm_watson` library as follows:

```python
from ibm_watson import ToneAnalyzerV3
```

* The Tone Analyzer response is given in JSON format, so the [`json_normalize` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.json.json_normalize.html) is imported from Pandas to transform the JSON response to a DataFrame.

```python
from pandas.io.json import json_normalize
```

The IBM Watson Tone Analyzer has two main methods:

* `tone()`: It refers to the general tone analysis aimed to score tone on short text (such as reviews, e-mails or social media) or even larger texts (such as articles or blog post).

* `tone_chat()`: It refers to the customer engagement tone analysis designed to monitor customer service and support conversations based on utterances between an agent and a customer.

The `tone()` method is presented first, explain students that it only needs to receive a text to score, however, additional parameters could be used to define the `content_language` (only `en` for English or `fr` for `french` are available in the current version) or the `accept_language` that is the language to be used for the name of tones.

```python
# Define text to analyze
text = """
Team, I know that times are tough!
Product sales have been disappointing for the past three quarters.
We have a competitive product, but we need to do a better job of selling it!
"""

# Analyze the text's tone with the 'tone' method.
tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json',
    content_language='en',
    accept_language='en'
).get_result()

# Display tone analysis results
print(json.dumps(tone_analysis, indent=2))
```

As can be seen on the result, the tone is given for the entire document on the `document_tone` element as well as for each sentence of the document on the `sentences_tone` element.

```json
{
  "document_tone": {
    "tones": [
      {
        "score": 0.6165,
        "tone_id": "sadness",
        "tone_name": "Sadness"
      },
      {
        "score": 0.829888,
        "tone_id": "analytical",
        "tone_name": "Analytical"
      }
    ]
  },
  "sentences_tone": [
    {
      "sentence_id": 0,
      "text": "Team, I know that times are tough!",
      "tones": [
        {
          "score": 0.801827,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    },
    {
      "sentence_id": 1,
      "text": "Product sales have been disappointing for the past three quarters.",
      "tones": [
        {
          "score": 0.771241,
          "tone_id": "sadness",
          "tone_name": "Sadness"
        },
        {
          "score": 0.687768,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    },
    {
      "sentence_id": 2,
      "text": "We have a competitive product, but we need to do a better job of selling it!",
      "tones": [
        {
          "score": 0.506763,
          "tone_id": "analytical",
          "tone_name": "Analytical"
        }
      ]
    }
  ]
}
```

The `JSON` response is transformed into a Pandas DataFrame using the `json_normalize()` function.

![Sample document tone as DataFrame](Images/document_tone_df.png)

To finish the demo the `tone_chat()` method is presented. Explain students that this method is intended to analyze tone from customer engagement conversation between an agent and a customer, where all the utterances are passed as parameter to score the tone of each one.

```python
# Define conversational utterances
utterances = [
    {
        "text": "Hello, I'm having a problem with your product.",
        "user": "customer"
    },
    {
        "text": "OK, let me know what's going on, please.",
        "user": "agent"
    },
    {
        "text": "Well, nothing is working :(",
        "user": "customer"
    },
    {
        "text": "Sorry to hear that.",
        "user": "agent"
    }
]

# Analyze utterances using the 'tone_chat' methos
utterance_analysis = tone_analyzer.tone_chat(
    utterances = utterances,
    content_language='en',
    accept_language='en'
).get_result()
print(json.dumps(utterance_analysis, indent=2))
```

As can be seen on the `JSON` response, all the tone scores for each utterance are under the `utterances_tone` element.

```json
{
  "utterances_tone": [
    {
      "utterance_id": 0,
      "utterance_text": "Hello, I'm having a problem with your product.",
      "tones": [
        {
          "score": 0.686361,
          "tone_id": "polite",
          "tone_name": "Polite"
        }
      ]
    },
    {
      "utterance_id": 1,
      "utterance_text": "OK, let me know what's going on, please.",
      "tones": [
        {
          "score": 0.92724,
          "tone_id": "polite",
          "tone_name": "Polite"
        }
      ]
    },
    {
      "utterance_id": 2,
      "utterance_text": "Well, nothing is working :(",
      "tones": [
        {
          "score": 0.997795,
          "tone_id": "sad",
          "tone_name": "Sad"
        }
      ]
    },
    {
      "utterance_id": 3,
      "utterance_text": "Sorry to hear that.",
      "tones": [
        {
          "score": 0.730982,
          "tone_id": "polite",
          "tone_name": "Polite"
        },
        {
          "score": 0.672499,
          "tone_id": "sympathetic",
          "tone_name": "Sympathetic"
        }
      ]
    }
  ]
}
```

Finally the `JSON` file is converted to a Pandas DataFrame using the `json_normalize` method. Remark students the use of the `meta` argument to include the `utterance_id` and `utterance_text` on each row.

![Sample utterances tone](Images/char_tone_df.png)

Slack out the Tone Analyzer docs for the [`tone()`](https://cloud.ibm.com/docs/services/tone-analyzer?topic=tone-analyzer-utgpe) and [`tone_chat()`](https://cloud.ibm.com/docs/services/tone-analyzer?topic=tone-analyzer-utco) methods and ends the activity by answering any reminder question.
