## 15.2 Lesson Plan: Egad! It's Alive!

---

### Overview

Today's class will expand upon students' component knowledge of algorithmic trading and abstract one level higher to create a full-fledged trading framework encapsulated in a single application. In particular, students will learn how to wrap their previous code (data collection, signal generation, backtesting, evaluation, and dashboard creation) into functions that will be called via a single workflow. In other words, students will automate the manual component calculations done in the previous class to produce an end-to-end trading dashboard containing all relevant metrics and functionality.

Furthermore, students will not only learn how to "go live" with their trading frameworks by establishing a connection to an actual financial API such as the Kraken Cryptocurrency Exchange API (which provides 24-hour market access and generous API request privileges), but also further their understanding of dataflows by implementing asynchronous tasks and streaming capabilities that allows for a more robust trading dashboard that can update its underlying data without having to re-draw its overall dashboard each time.

### Class Objectives

By the end of class, students will be able to:

* Design an end-to-end workflow for a trading framework (data collection > signal generation > backtesting > evaluation > dashboard creation).

* Abstract their previous day's algorithmic trading calculations into functions and execute an end-to-end implementation of a working trading framework.

* Utilize live financial data by connecting their trading frameworks to the Kraken Cryptocurrency Exchange API.

* Persist or save their trading data to a database such as sqlite.

* Perform asynchronous tasks and loops using asyncio.

* Implement asyncio with their trading frameworks to fetch data and update the dashboard in parallel.

* Enhance their trading dashboards with data streaming capabilities.

* Deploy their algorithmic trading application online via Heroku.

### Instructor Notes

* Today's lesson will tie together the concepts and coding solutions from the previous day into a single robust trading framework that can produce an end-to-end implementation of a trading dashboard with working metrics.

* The goal of today's lesson is to demonstrate how to architect and implement a full stack trading application (back-end and front-end functionality), and also dispel the esoteric nature of developing a production-level algorithmic trading application.

* This lesson will primarily focus on developing the *infrastructure* of the trading framework and therefore will not contain as much domain-specific trading knowledge.

* Review sessions will be geared towards allowing students to ask as many questions as possible. Questions should be prioritized over instructor posed review questions. While we want to provide as much opportunity as possible for students to ask questions, it is also important that the class is paced so that all material is covered.

* Encourage students to review supplementary resources, to reach out to TAs individually for assistance, and to attend office hours to address any unanswered questions or confusion.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson 15.2 Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this here.

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

In this section, students will review the algorithmic trading concepts taught in the previous class to prepare them for today's consolidation of multiple trading functions (signal generation, backtesting, trade evaluation, etc.) into a single trading framework. This section is a key opportunity to take a step back and understand the *process* of algorithmic trading, so as to later transition to the architecture or infrastructure of an algorithmic trading framework.

Welcome students to the second day of algorithmic trading and quickly review the following:

* What is algorithmic trading?

  **Answer:** Algorithmic trading is the concept of utilizing a machine to automate the process of buying and selling assets based on specific trading signal criteria and decision-making logic.

* What is a trading signal?

  **Answer:** A trading signal is the point at which a technical indicator, such as the crossover of two moving averages (short MA and long MA), suggests an opportunity for action--namely whether an individual trader or algorithmic trading program should issue a buy or sell order for a security (such as a stock) at that point in time.

* What is backtesting?

  **Answer:** Backtesting is the process for measuring the overall performance of a trading strategy using historical stock prices to simulate executed trades dictated by the calculated trading signals and trade decision logic.

* What are algorithmic trading evaluation metrics?

  **Answer:** Metrics that showcase information such as overall portfolio or per-trade performance. Examples include cash balance, total portfolio value, per-trade profits and losses, and dates of entry and exit trades.

* What is a trading dashboard?

  **Answer:** Like other dashboards, a *trading dashboard* consolidates and presents multiple facets of information pertaining to the performance of an algorithmic trading application, allowing a user to interact with the data via tables and plots (visualizations).

Mention to students that going forward in today's class, they should not only keep in mind the distinct purposes or functions of each trading calculation, but the chronology and dependencies of each function as well.

Answer any questions before moving on.
