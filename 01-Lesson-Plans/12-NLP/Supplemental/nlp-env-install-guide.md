# Natural Language Processing Environment Installation Guide

This guide serves as a step by step process for setting up and validating the tools required for the natural language processing (NLP) portion of the curriculum. Without these tools, class activities and code cannot be completed.

This guide will include installation and verification steps for the following technologies:

## News API Python Client Library

In this unit, you will learn how to analyse text and sentiment from news articles using the [New API service](https://newsapi.org/). In order to interact with this service, you should install the [News API Python client library](https://newsapi.org/docs/client-libraries/python) as follows.

Open the terminal, and execute the following command.

```shell
pip install newsapi-python
```

### Verify the News API Python Client Installation

Once the `newsapi-python` library download is complete, verify the installation completed successfully.

* Open the terminal and use the `conda-list` function with a `grep` argument to identify if the `newsapi-python` library installed successfully.

```shell
conda list | grep newsapi-python
```

![News API verification](Images/news-api-verify.png)

## IBM Watson Python Library

In this unit, you will learn how to the [IBM Watson Tone Analyzer](https://www.ibm.com/watson/services/tone-analyzer/) to analyze tone on text communications. In order to use this service, you need to install the [IBM Watson Python Library](https://pypi.org/project/ibm-watson/) as follows.

Open the terminal, and execute the following command.

```shell
pip install --upgrade "ibm-watson>=3.0.3"
```

### Verify the IBM Watson Python Library Installation

Once the `ibm-watson` library download is complete, verify the installation completed successfully.

* Open the terminal and use the `conda-list` function with a `grep` argument to identify if the `ibm-watson` library installed successfully.

```shell
conda list | grep ibm-watson
```
![IBM Watson verification](Images/ibm-watson-verify.png)
