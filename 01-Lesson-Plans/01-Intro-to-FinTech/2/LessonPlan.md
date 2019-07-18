## 1.2 Lesson Plan: Deep Dive into FinTech

---

### Overview

Today's class will focus on command line basics and setting up an Anaconda virtual environment. It will then further investigate the key factors leading to the exponential growth of the FinTech industry.

Specifically, students will be introduced to basic command line and virtual environment skills, which will help them use more advanced CLI tools in the next lesson as well as future units in the course; learn more about the history of FinTech and the areas that have been disrupted through innovation; and collaborate with others to produce predictions on various FinTech domains in the form of future news headlines.

### Class Objectives

By the end of class, students will be able to:

* Use the command line to execute basic file system operations.

* Download and upload files to GitHub using the git GUI.

* Describe the factors that led to the evolution of the FinTech industry.

* Map out the disrupted domains of the FinTech industry.

* Make predictions in the form of future news headlines for a particular FinTech domain.

### Instructor Notes

* Slack out the [Anaconda Installation Guide](../../02-Python/Supplemental/AnacondaInstallGuide.md) and ask students to complete the install and verify it with a TA before the end of the next class. This should help catch installation issues with Python outside of the class time.

* Students may have trouble grasping the notion of the command line. You can explain it like this: when students double-click on a folder to change directories, they are essentially executing a backend `cd` command. The GUI that a student sees is merely a visual overlay of the backend operations of the computer.

* While important, the concept of Anaconda virtual environments and environment variables do not have to be as in-depth at this point in the course. The associated activity mainly acts as a technical pre-cursor to the future units in the course, and ensures that students should be able to complete future activities without dependency issues/conflicts.

* Emphasize that understanding the history of FinTech is just as important as knowing what FinTech is. Employers will measure candidates not only by their technical skills, but also by their contextual knowledge of what is happening in the financial services industry.

### Class Slides and Timetracker

The slides for today can be viewed on Google Drive here: [Slides](https://docs.google.com/presentation/d/1_7OIXTJY_Yli-E9KO7n4ZlGcylu9IMEsvJuFkhYivpc/edit?usp=sharing)

To add slides to the student-facing repository, download the slides as a PDF by navigating to File > "Download as" and choose "PDF document." Then, add the PDF file to your class repository along with other necessary files. [Instructions Here](https://docs.google.com/document/d/14MiAunWj30hu-pYLGDz9JOM5XbGjunn1hZ6iyym4w2w/edit)

* Note: Editing access is not available for this document. If you wish to modify the slides, please create a copy by navigating to File > "Make a copy...".

The Timetracker for today can be viewed here: [Timetracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome (10 min)

**File:** [Slides 1-3](https://docs.google.com/presentation/d/1_7OIXTJY_Yli-E9KO7n4ZlGcylu9IMEsvJuFkhYivpc/edit?usp=sharing)

Take some time to welcome students back to class and introduce the topics that will be covered in this lesson: command line and Anaconda virtual environment, and a brief history of FinTech. This lesson will give students both the skills and knowledge required to gain a deeper understanding of the changing landscape within the FinTech ecosystem.

Cover the following points:

* While future units and activities will utilize more advanced tools and technical concepts (API’s, Algorithmic Trading, etc.), today’s lesson will start small. We’ll begin by practicing the fundamentals for technical programming so that students can begin on their FinTech journey.

* Students will begin working with fundamental developer tools such as the command line, a text-based utility for performing file system operations and executing programs. They will also learn to create an Anaconda virtual environment, a managed file space which exists as its own isolated environment with corresponding dependencies, residing on a physical computer. By the end of the day, students will join the ranks of millions of developers who also use the command line for file system operations and third-party CLIs (ex. conda).

* Today's lesson will include a brief insight to the factors leading up to the current state of FinTech, the financial sectors or FinTech domains that technology has helped to disrupt, and a collaborative activity researching the factors for change of a particular FinTech domain for each group.

* Understanding and being able to discuss FinTech's history is useful, particularly when applying to jobs; it will show employers that you care enough to familiarize yourself with the industry, as well as showcase an understanding of potential opportunities and pitfalls within the industry.

Encourage the students and get them excited for the lesson. Tell them that today will be a crash course in both hard and soft skills; students will learn technical skills and contextual knowledge to aid them in their future careers in FinTech.

---

### 2. Instructor Do: Introduction to the Command Line (10 min)

In this section, students will learn the basics of using the command line to perform basic file system operations on their machines.

**File:** [Slides 4-7](https://docs.google.com/presentation/d/1_7OIXTJY_Yli-E9KO7n4ZlGcylu9IMEsvJuFkhYivpc/edit?usp=sharing)

Open the slideshow and present the following questions and answers:

* What is the command line?

  **Answer:** The command line, or terminal, is an interface in which a user can type and execute text-based commands.

* When should you use the command line?

  **Answer:** The command line can be used at any time in place of the graphical user interface (GUI). The GUI is merely a visual overlay to the programs executed via the command line. Also, when remotely connecting to a server, such as via the Secure Shell Protocol (SSH), a GUI will not be provided.

* Why use the command line?

  **Answer:** Using the command line is efficient, as it does not expend the additional processing needed to produce the visuals associated with a graphical user interface (GUI).

Open the command line and demo the following commands. Tell students that on a Mac, the command line is accessed via Terminal, while Windows uses Git Bash.

* `cd` changes the directory.

* `cd ~` navigates to the home directory.

* `cd ..` moves up one directory.

* `ls` lists files in the folder.

* `pwd` shows the current directory.

* `mkdir <FOLDERNAME>` creates a new directory with the folder name as `<FOLDERNAME>`.

* `touch <FILENAME>` creates a new empty file with the file name as `<FILENAME>`.

* `code <FILENAME>` opens a file in the VS Code editor.

* `cat <FILENAME>` reads a file and outputs to the terminal.

* `rm <FILENAME>` deletes a file.

* `rm -r <FOLDERNAME>` deletes a folder recursively; make sure to note the -r.

* `open .` opens the current folder on Macs.

* `explorer .`opens the current folder in Git Bash.

* `open <FILENAME>` opens a specific file on Macs.

* `explorer <FILENAME>` opens a specific file in Git Bash.

![terminal-example](Images/terminal-example.png)

Slack out [CommonCommands.txt](Activities/01-Ins_Terminal/Solved/CommonCommands.md) for students to use as a reference.

Answer any questions before moving on.

---

### 3. Student Do: File System Operations (15 min)

In this activity, students will perform their own file system operations via the command line.

**File:** [README.md](Activities/02-Stu_Terminal/README.md)

### 4. Instructor Do: Review File System Operations (5 min)

Open [file_system_operations.sh](Activities/02-Stu_Terminal/Solved/file_system_operations.sh) and cover the following points:

* `mkdir` creates folder directories.

* `cd` navigates into specified folder directories.

* `touch` creates an empty file.

* `cat` reads files and outputs the results to the console.

* `code` opens files in the VS Code.

* `cd ..` navigates up one level.

* `cp` copies files from source to target.

* `rm -r` recursively deletes all files in a folder (that may have sub-folders).

* `mv` moves files from source to target. It can also be used to rename a file.

* `ls` lists the contents of the current directory.

---

### 5. Instructor Do: Uploading Files to GitHub (20 min)

In this activity, students will learn how to upload files to GitHub, which will be used to submit their future homework assignments in the course.

Briefly explain the following:

* GitHub offers a centralized location where developers can push and pull (upload and download) their code; GitHub always holds the most up-to-date code and files and handles everyone's updates appropriately.

* For now, students will only be introduced to the GitHub GUI; however, in the next lesson, students will learn to work with GitHub via the command line using git, which allows for more advanced git operations.

Then, have the students follow along with the following steps:

* Visit <https://github.com> and ask students to log in to their personal accounts.

* From the main page, create a new repository with an initialized `README.md` file.

  * Note that the convention in the software world is for each repository to have a README file that explains what the repository contains.

  ![git repo](Images/GitDemo_1.png)

* Create a new Excel file and save it to your desktop. This file will be used to demonstrate how to upload new files.

* Navigate back to GitHub and click the "Upload files" button.

  ![upload file](Images/GitDemo_upload.png)

* Choose your Excel file in the dialog box.

  * Note that you can also drag and drop the file rather than use the "Upload files" button.

* Add a commit message and commit the changes.

* Refresh the webpage to show that the new file is now safely saved to the repository.

  ![drag file](Images/GitDemo_filedrag.gif)

Encourage students to practice using GitHub before the next class and attend office hours if they run into any problems.

---

### 6. BREAK (15 min)

---

### 7. Instructor Do: FinTech's Past, Present, Future (5 min)

In this activity, instructors transition students from the technical demos of the 1st half of the day (command line and git GUI) into a more interactive discussion for the remainder of class regarding the concepts and background information of the FinTech realm, specifically focusing on the history of FinTech, the current state of its ecosystem, and the possibilities to its future.  

Perform the following:

* Explain to students that the remainder of class will now focus on a deeper dive into FinTech's past, present, and future; namely, the factors leading to the recent explosion of technological investment in the FinTech realm, the current breakdown of the FinTech ecosystem, and the potential outcomes of the FinTech realm given its current trajectory.

Then, set up the prompt for the following thought exercise by asking the students the following questions:

* What did the finance world look like in 1999?

* What were some financial processes that are becoming obsolete or no longer exist today?

* How has technology accelerated the change in the finance world over the last 20+ years?

### 8. Student Do: Rip Van Winkle Thought Exercise (10 min)

In this activity, students think about how the current state of the FinTech world may differ from that of someone from the year 1999.

Quickly explain to the class the following:

* The story of Rip Van Winkle represents a short story by the American author Washington Irving, first published in 1819, that follows a Dutch-American villager in colonial America named Rip Van Winkle who falls asleep in the Catskill Mountains and wakes up 20 years later, completely missing the events of the American Revolution.

* Adapting the Rip Van Winkle story to FinTech, imagine if a financial analyst fell asleep in the year 1999 and woke up today, what would be most surprising about the finance world?

* Students should define areas of finance that have been deeply affected by technology, naming specific companies, products, or innovations that would be surprising to a sleeper from 1999.

* Students should form groups of 3-4 individuals and will be expected to quickly present their thoughts in the following review activity.

---

### 9. Instructor Do: Review Rip Van Winkle Though Exercise (5 mins)

In this activity, students present their opinions regarding the FinTech Rip Van Winkle thought experiment.

Perform the following:

* Ask for a few volunteers that would be willing to share their group's thoughts on what they felt would be the most surprising to a sleeper from 1999 witnessing the current state of the finance world.

* Take note of each group's findings and emphasize some of the overarching themes regarding the state of the current FinTech ecosystem. For example, some themes that are likely to present themselves are:

  * Automation
  * Big Data
  * Mobile Infrastructure
  * Cloud Infrastructure

### 10. Instructor Do: Evolution of FinTech (10 min)

In this section, give students a brief summary of some of the key factors leading to the growth of the FinTech space. Understanding the historical background of FinTech as well as its current trajectory will give students knowledge that will help them both in employer interviews and their FinTech career.

**File:** [Slides](https://docs.google.com/presentation/d/1_7OIXTJY_Yli-E9KO7n4ZlGcylu9IMEsvJuFkhYivpc/edit?usp=sharing)

Open the slideshow and use the slides to review the key historical factors leading to the present-day FinTech boom:

* Mobile Infrastructure and Shifting Consumer Preferences

  * With the advancement in mobile network infrastructure (2G, 3G, 4G LTE), consumers have become more connected to the internet (as well as each other) than ever before. As a result, consumers not only have a greater resource pool to cross-check and validate information (e.g., checking prices) but also have become a resource pool themselves in which companies look to target for business.

  * Consumers today demand quick, reliable, and quality channels of engagement. Modern-day consumers often place their trust in a company that boasts a dynamic and beautiful website, a well-designed and efficient mobile application, and––ideally––a social user platform that allows customers to connect with others using the same product or service.

  * Therefore, companies have been forced to make large investments in technology in order to stay competitive with their industry peers. Consumers have more product choices and are loyal to companies they trust. Therefore, the technological channels affecting consumer engagement have a direct impact on a company's ability to market themselves and, ultimately, capitalize on demand.

* Big Data

  * Over the years, computer processing units (CPUs), random access memory (RAM), and hard drive storage devices have become both more powerful and less expensive. Therefore, more companies were able to purchase and utilize large clusters of computers working in parallel.

  * Parallel processing paradigms have also shifted to become more efficient. Traditionally, to enable machines to work in parallel, the concept of MapReduce was born. With MapReduce, data workloads were split among multiple machines for disk-based processing, and then re-aggregated at the end to produce the result. However, with the advent of Spark, that same process has been refined for in-memory processing, in which data workloads utilize RAM that is much faster (though more costly) at processing data.

  * Because big data processing has become more efficient, the time needed to curate and analyze data has also decreased. Therefore, modern-day companies are able to employ tactics like machine learning to drive business decision-making in real time.

  * Companies have placed enormous emphasis on technological investment due to the growing feasibility and allure of housing large clusters of machines to drive real-time, data-driven analysis.

* Cloud Infrastructure

  * Traditionally, server farms, or large clusters of machines, required large upfront costs and overhead related to server maintenance. With the inception of cloud computing, however, companies no longer had to purchase their own servers for their data-processing needs, but instead could "rent" servers from another vendor on an as-needed (and, therefore, much cheaper) basis. This allowed smaller companies to compete with larger, more established companies in regard to utilizing big data.

  * In addition, because cloud vendors like Amazon Web Services (AWS) manage hosting and deployment of servers in the cloud, the time-to-market for companies to reap the benefits of investing in technology has decreased, as they are able to push their applications and features quicker.

  * The business landscape has become increasingly competitive, as smaller companies now have the capabilities to disrupt markets with their fully fledged, productionalized applications and services––which previously would have required large upfront costs, a barrier to entry of the industry.

Answer any questions before moving on.

---

### 11. Instructor Do: Facilitated Discussion About Finance and Technology (10 min)

This section will be a brief discussion on the positive impacts that technology has had on the finance world, which will then transition to the topic of specific FinTech domains whose traditional financial activities have replaced with more efficient means via the benefits of technological innovation.

Ask the students the following questions:

* What are some areas in the financial industry where technology has disrupted traditional finance activities?

  **Sample Answer:** Blockchain and financial transactions; robo advisors and investment management; and payment applications and money transfers.

* How did these technologies allow for the disruption of traditional finance?

  **Sample Answer:** Blockchain allows for cheaper and more secure transactional validation. Robo advisors utilize machine learning algorithms for portfolio management, thereby reducing overhead costs.  Payment applications utilize modern infrastructure such as mobile and cloud-based networking.

* How might cloud-based networking contribute to the advent of start-ups and technological innovators?

  **Sample Answer:** Traditionally, hosting servers meant purchasing on-premises server farms with large upfront costs and regular maintenance, which was a barrier for entry for small startups. However, with cloud-based networking such as AWS, small start-ups and even individuals can quickly spin up servers faster and on an as-needed basis, thereby minimizing time to deployment and reducing up-front costs. This allows small startups to compete more efficiently with larger firms with existing infrastructures.

* Where else might technology disrupt traditional finance?

  **Sample Answer:** Machine learning can be used in lending to more efficiently target customers who have a higher likelihood of paying back their loans, while avoiding those who have a higher likelihood of *not* paying back their loans.

Then, end the discussion with the following points:

* The field of FinTech is so vast and rapidly changing due to technological innovation that even entire domains of the FinTech ecosystem have begun to change the way in which companies operate and compete with their peers.

* In order to complete the unit 1 homework assignment (FinTech case study), students will need to comprehend the nature of the FinTech domains as well as the competitive factors affecting the underlying companies within. Therefore, we will need to take a closer look at the FinTech landscape.

---

### 12. Student Do: FinTech Domains Part I (25 min)

In this activity, students will form groups of 2-3 individuals to research and produce summaries of the various FinTech domains.

**File:** [README.md](Activities/03-Stu_FinTech_Domains_Part_I/README.md)

### 13. Instructor Do: Review FinTech Domains Part I (10 min)

**File:** [Slideshow](https://docs.google.com/presentation/d/1_7OIXTJY_Yli-E9KO7n4ZlGcylu9IMEsvJuFkhYivpc/edit#slide=id.g5ecf7ad488_5_360)

Open the slideshow and review the following FinTech domains:

* Payments and Remittances
* Robo Advisors and Personal Finance
* RegTech
* Digital Banking
* InsurTech
* Alternative Finance

Then, provide a brief question and answer by asking students the following questions, thereby making sure the class is on the same page before moving on:

* Was there anything confusing regarding the FinTech domains, companies, or technologies used?

* Was there anything you felt was notable or interesting when researching the FinTech domains?

---

### 14. Student Do: FinTech Domains Part II (15 min)

The previous activity should have laid the foundation for students to not only assess the current state of their FinTech domain, but now also devise a hypothetical news headline for that particular FinTech domain that could potentially occur within the next 2-3 years. Students will continue in their groups of 3-4 individuals to complete the activity.

**File:** [README.md](Activities/04-Stu_FinTech_Domains_Part_II/README.md)

### 15. Instructor Do: Review FinTech Domains Part II (20 min)

Now that students have had an opportunity to perform their own research on their respective FinTech domains and produce hypothetical news headlines, it's now time to facilitate a class discussion based on each group's findings and thoughts.

Have each group do a turn-and-teach and present their FinTech domain and news headline to the group next to them:

* Walk around the class with your TAs to support any discussions if necessary.

After students' peer presentations are complete, ask for any volunteers who are willing to share why they chose their particular FinTech news headline. Then, ex0plain the following:

* The intent of this activity was to provide students with not only the breadth but also the depth of knowledge for each FinTech domain. This may prove to be valuable when applying for roles within the FinTech industry.

* It is not enough to simply restate the past, but also to analyze and predict the future. Therefore, after this activity students should have a general idea as to the trends affecting each FinTech domain as well as the potential outcomes that may result for each domain within the near future.

Ask students if they have any questions before moving on.

---

### 16. Instructor Do: Review and Reflect (5 min)

This activity provides a moment to allow the class to digest and decompress from the fast pace of the day.

### End Class

---

© 2019 Trilogy Education Services
