### 13. Instructor Do: Tone Analysis (15 mins)

In this activity students will be introduced to tone analysis and how they can score tone of human speech using the **IBM Watson Tone Analyzer service** and its Python library.

**Files:**

* [Lesson Slides](#)

* [tone_analysis.ipynb](Activities/13-Ins_Tone_Analysis/Solved/tone_analysis.ipynb)

* [keys.sh](Activities/13-Ins_Tone_Analysis/Solved/keys.sh)

Start by opening the lesson slides, go to the _Tone Analysis_ section and highlight the following:

* Tone analysis offers new possibilities to sentiment analysis since it goes beyond the simple classic classification as positive, negative or neutral and looks to understand human emotions.

* Tone analysis is a complex and costly task since it requires to train algorithms with thousands of documents that need to be previously tagged to understand the emotion behind the words.

* IBM Watson Tone Analyzer is a cloud service to analyze tone on text communications, due to the cost of analyzing tone this service is only available now for English and French languages.

* IBM Watson Tone Analyzer can be used via its Python API.

After the brief definition of tone analysis and the intro to IBM Watson Tone Analyzer, slack out [the URL for this service](https://cloud.ibm.com/catalog/services/tone-analyzer) and guide students on creating their IBM Cloud account and setting up their Tone Analyzer instance. Ask TAs to assist students on creating their personal IBM Cloud account and follow the lesson slides as a guided tour by highlighting the following:

* Students will use the Lite plan of Tone Analyzer, it allows to make 2,500 API call per month for free and no credit card is required to use it.

* Student only need to fill out their personal account information on the registration form.

  ![IBM Cloud registration form](Images/ibm_cloud_registration_form.png)

* Students will receive an email like this, they just have to click on the **Confirm account** button to start using the Tone Analyzer service.

  ![IBM Cloud confirmation e-mail sample](Images/ibm_cloud_registration_form.png)

* After the new IBM Cloud accounts is confirmed, students will see their dashboard. The **Create resource** button should be clicked to continue.

  ![IBM Cloud dashboard](Images/ibm_cloud_dashboard.png)

Once students have access to their IBM Cloud dashboard, they need to create an instance of the **Tone Analyzer Service**. On the **Catalog** students should type `label:lite tone analyzer` on the search box to find the service; once the service appears on the results, ask students to click on the **Tone Analyzer Service** to configure the instance.

  ![IBM Cloud catalog](Images/ibm_cloud_catalog.png)

* To create the Tone Analyzer instance, just the _Service name_ should be provided on the **Tone Analyzer configuration page**. After clicking the **Create** button, the instance is ready to be used.

  ![Tone Analyzer configuration page](Images/tone_analyzer_create_instance.png)

Now the Tone Analyzer instance is ready to use, ask students get their API key and the instance URL by clicking on the **Show credentials** link.

  ![Tone Analyzer instance sample](Images/show_tone_analyzer_credentials.png)

* Students will find their credentials under the section entitled _Step 1: Using the general-purpose endpoint via the POST request method_.

* Students will see the API key and the instance URL as it's shown bellow. The URL can differ from the image but it ends with `/api`.

  ![Tone Analyser credentials](Images/get_tone_analyzer_key.png)

Ask students to create two environment variables, one for the API key and other for the URL. Open the [unsolved Jupyter notebook](Activities/13-Ins_Tone_Analysis/Solved/tone_analysis.ipynb) and switch to the code demo highlighting the following:

* The IBM Watson Python library need to be installed using `pip` as follows. This demo runs using version 3.

  ```bash
  pip install --upgrade "ibm-watson>=3.0.3"
  ```

* The Tone Analyzer service is imported from the `ibm_watson` library as follows:

  ```python
  from ibm_watson import ToneAnalyzerV3
  ```

* The Tone Analyzer response is given in JSON format, so the [`json_normalize` function](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.json.json_normalize.html) is imported from Pandas to transform the JSON response to a DataFrame.

  ```python
  from pandas.io.json import json_normalize
  ```

* The Tone Analyzer service should be initialized passing as parameters the version that is going to be used, the API key and the URL.

  ```python
  tone_analyzer = ToneAnalyzerV3(version="2017-09-21", iam_apikey=tone_api, url=tone_url)
  ```

* The IBM Watson Tone Analyzer has two main methods:

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

# Analyze the text's tone with the 'tone()' method.
tone_analysis = tone_analyzer.tone(
    {'text': text},
    content_type='application/json',
    content_language='en',
    accept_language='en'
).get_result()

# Display tone analysis results
print(json.dumps(tone_analysis, indent=2))
```

* On the `JSON` response, the tone is given for the entire document on the `document_tone` element as well as for each sentence of the document on the `sentences_tone` element.

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

* The `JSON` response is transformed into a Pandas DataFrame using the `json_normalize()` function.

  ![Sample document tone as DataFrame](Images/document_tone_df.png)

Next the `tone_chat()` method is presented. Explain students that this method is intended to analyze tone from customer engagement conversation between an agent and a customer, where all the utterances are passed as parameter to score the tone of each one.

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

* On the `JSON` response, all the tone scores for each utterance are under the `utterances_tone` element.

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

* The `JSON` response is converted to a Pandas DataFrame using the `json_normalize` method. The `meta` argument is used to include the `utterance_id` and `utterance_text` on each row.

  ![Sample utterances tone](Images/char_tone_df.png)

Slack out the Tone Analyzer docs for the [`tone()`](https://cloud.ibm.com/docs/services/tone-analyzer?topic=tone-analyzer-utgpe) and [`tone_chat()`](https://cloud.ibm.com/docs/services/tone-analyzer?topic=tone-analyzer-utco) methods and close the activity by answering any reminder question.
