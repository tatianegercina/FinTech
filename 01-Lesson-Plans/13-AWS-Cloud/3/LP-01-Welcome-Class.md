## 13.3 Lesson Plan - Amazon Lex and Robo Advisors

---

### Overview

In Today's class, students will be introduced to conversational user interfaces (CUIs) also they will learn how CUIs are disrupting finance and banking. By the end of the class, students will create a robo advisor using Amazon Lex, Amazon Lambda and Slack.

### Class Objectives

By the end of the unit, students will be able to:

* Describe the applications of conversational interfaces for finance and banking.

* Recognize how machine learning contributes to create conversational interfaces.

* Create conversational interfaces using Amazon Lex.

* Apply their Python skills to add new features to an Amazon Lex bot using Amazon Lambda.

* Deploy a robo advisor application on Slack.

### Instructor Notes

* There are several misconceptions and myths about what can be achieved with a Robo Advisor, make sure students understand what a Robo Advisor is and invite them to think about the endless possibilities of this technology for FinTech.

* Today's class may be challenging for students because they are going to deal with different AWS services and the Slack API, so be sure to get familiar with all the activities before class.

* Amazon Lambda functions will be created and edited using the online code editor. This editor sometimes has issues or freezes up, so tell students to backup their code with a local Python script.

* Testing Amazon Lambda functions could be tricky and frustrating, so have your TAs assisting students while they are coding and testing them.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 13.3 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (5 mins)

In this activity, students will be introduced to conversational user interfaces (CUIs); they will learn how CUIs are disrupting on financial services and what are the tools they will use to create a robo advisor.

**Files:**

* [Lesson 13.3 Slides]()

Welcome students back and explain that Today we will learn about conversational user interfaces, one of the coolest applications of natural language processing; explain to students that they will create a robo advisor with conversational capabilities by the end of the day.

Open the lesson slides and move to the _Conversational User Interfaces (CUIs) and Robo Advisors_ section, highlight the following:

* On the early yeas of computing history, people used to communicate with computers using text interfaces and some non-human-friendly commands.

* Thanks to AI, and specially to the advances on natural language processing (NLP), nowadays we can communicate with computer systems using human language through conversational user interfaces via voice or text.

* Chatbots are the most common applications of CUIs, however, Amazon Alexa, Apple Siri or Google Assistant are also examples of CUIs.

* Financial services providers are using CUIs by offering Robotic Advisors or Robo Advisors, as an additional communication channel for customers.

Engage students by highlighting the benefits of this technology on finance and banking, slack out [this article from Deloitte](../Suplemental/deloitte-nl-fsi-chatbots-adopting-the-power-of-conversational-ux.pdf) were they can learn more about the impact of chatbots in financial services.

Present to students the use cases shown on the _Example Chatbots Use Cases_ slide, ask a couple of them if they are familiar with services like these and what were their experience.

Explain to the class the technologies we will use Today and highlight the following:

* By the end of Today's class we will create a robo advisor using AWS.

* Amazon Lex is a service for building conversational interfaces into any application using voice and text.

* Amazon Lambda is a computing service that runs code in response to events. We will use this service to program the actions of the robo advisor.

* The robo advisor will be deployed as a Slack application were users will interact with it.

Answer any additional question before moving forward.
