## 1.1 Lesson Plan - Welcome to FinTech!

---

### Overview

Today's class will focus on getting students settled down within the FinTech course as well as introducing students to the evolving financial services industry known as FinTech. In particular, instructors, teacher assistants, student success managers, and students will introduce themselves to the class and then proceed to outlining the course agenda and requirements. Lastly, students will participate in group discussions regarding the nature of FinTech (what is it exactly?) and end the class with an overview of the unit 1 homework.

### Class Objectives

By the end of class, students will be able to:

* Define what a simulation is and why it's used.
* Deconstruct the components of the Monte Carlo Simulation process: probability distributions and iterations.
* Interpret probability distributions (normal/bell curve) and random number generators.
* Comprehend the use of confidence intervals and what they suggest.
* Implement a single Monte Carlo simulation on the future price trajectory of a stock.
* Execute multiple Monte Carlo simulations on the future price trajectories of a stock.
* Break down Portfolio Forecasting in the context of Monte Carlo Simulations on stock price trajectories and portfolio returns.
* Implement multiple Monte Carlo simulations on the potential returns of a stock portfolio.

### Instructor Notes

* Today's lesson deals heavily with statistical concepts, particularly probability. Try to be as clear as possible and be mindful of students who may become easily confused as this lesson will surely push the boundaries of most students' comfort levels when it comes to statistics.

* When overviewing the concept of probability distributions, also make sure to stress the notion of randomness. Probability merely implies that there is a chance that a specific result or event may occur but makes no guarantees, which is why results can differ with each iteration.

* Once students are comfortable with probability distributions, namely normal distributions, students should be able to process the idea that Monte Carlo simulations on stock investments seeks to chart the different paths (and probabilities) in which a stock can vary about its average daily return. Overview the code in detail so that this becomes more apparent.

* Towards the end of class, students will begin applying Monte Carlo simulations to portfolio returns. Therefore, they will need to combine the concepts of portfolio optimization (taught in the Pandas unit) with the concept of portfolio forecasting (taught in today's lesson). Walk through the steps in details as students can easily get lost in this myriad of technical concepts!

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. University Do/SSM Do: Introductions (15 mins)

The first part of class consists of introductions from the university, program director, student services director, and/or career director.

**Instructor/TAs**: Just hang tight and calm your nerves for now. Your time for introductions will be coming up shortly.

---

### 2. Instructor Do: Class Introductions (40 mins)

At this point, it's your turn to introduce yourself, as well as have the TAs and students introduce themselves one at a time. This is an important icebreaking activity; have fun with it!

* Open the [slideshow](). Use it as a guide for the rest of the lesson. Remember to stay on schedule, and, if necessary, ask your TAs to help keep track of time.

* Have every student in class introduce themselves. Feel free to refer to the slides or come up with questions of your own. Try to keep things lighthearted as students share their backgrounds.

* When all students have had a chance to introduce themselves, have the TAs introduce themselves as well.

* Finally, introduce yourself and showcase a project or two to demonstrate your chops in the data field.

---

### 3. Course overview (15 mins)

* Continuing in the slideshow, we will now enumerate the topics that will be covered throughout the course.

* Walking students through our narrative:
    * We begin with an introduction to FinTech and Finance as it currently stands, discussing the current financial landscape and some of the current industry-standard methods/tools such as excel.

    * Then, we move into the direction where the industry is *going* by jumping into Python. We'll spend several weeks covering the basics of the languags and popular modern libraries such as Pandas and Matplotlib before turning our sights on building predictive time series analyses. This will culminate in our first major project using what we've learned up until now to build the best portfolio strategy possible.

    * From there, we'll supercharge the financial models that we are building using everyone's favorite buzzword: Machine Learning. We'll spend about a week on the introductor material and then get into applications in financial advising, algorithmic trading, and dynamic pricing.

    * In the last major leg of the journey, we'll dive into the oft-misunderstood world of blockchain and cryptocurrencies in order to understand the inefficiencies that they can potentially solve as well as how to develop automatically-executing smart contracts using the Solidity platform.

* If you finish this ahead of schedule, feel free to take one or two questions, but don't get bogged down.
    * Students will often like to ask if we will cover "X" technology. If you know for certain that we will then feel free to answer, otherwise it is a good idea to deflect to office hours so that you can look through the curriculum for an exact answer or offer to help the find resources when they reach an appropriate point in the course.

---

### X. Instructor Do: Intro to Fintech (15 mins)

* What exactly *is* fintech anyway? Through the next few slides we aim to clarify what the field is and isn't, as well as allowing students to explore their own ideas about the field.

* Ask the class, before moving on, what _they_ think fintech is?

---

### Instructor Do: Introduce Homework (10 mins)

* Before heading out for the night, make sure to introduce the first homework assignment so students can begin thinking about what company they want to do their case study on.

* This week's homework has students researching a contemporary FinTech company and developing a case study around it. They should strive to answer as many as possible of the following questions:

    * Current landscape in company sector:
        * Which financial industry it is in?
        * Trends and competitors in this industry; 
    * Company’s business activities
        * What “problem” does this company solve?
        * Who is their intended customer?
        * What solution does this company offer that their competitor does not or cannot? (What is the unfair advantage they utilize?)
    * Which technologies are they currently using and how are they implementing them?
    * What are they doing right? What could be improved? 
    * If you were to advise them – what products or  services would you suggest they add to their  services (whether another company already has  them or something that is your pure imagination)?
    * Why do you think it would benefit them? 
    * What technologies would your proposed ideas  incorporate? Why are those technologies  appropriate for your solution?

    * At the end of the week, students will produce a short, **informal** (5 min) presentation that will lead to a larger discussion with the class on 1.3 and a final report next week.

---

### Instructor Do: Review Group discussion (10 mins)

* After taking a few responses, bring up the next slide.

* Trilogy's definition for the scope of this class:

```

    The use of technology, especially software, 
    to compete with "traditional" banking processes.

```

* In a broader sense, technology has been in the banking and finance world for many, many years. However, the recent explosion in the number of available technologies for developers and engineers to use has created the chance for newcomers to take advantage of the "missed opportunities" that more mature banking institutions have been unable to take advantage of.

* It's not the banks' fault, they have lots of regulations to adhere to.

* Examples: Kenya's M-Pesa, Betterment, 

* Fintech solutions offer the opportunity to continue to optimize financial services for more speed, better profit margins, and a wider customer base than ever before.

* We'll get into the specific subdomains and trends on day 2

---

### Student Do: Discuss Definitions of Fintech (25 mins)


* Students are all here for a course on fintech, but may not have clarity on what exactly that is.

* Slack out (or simply speak the following assignment):

```md
    - You're all here for a course on fintech, but what exactly _is_ fintech?

    - Take the next few minutes to discuss with those around you about what you think fintech both _is_ and _isn't_.

```