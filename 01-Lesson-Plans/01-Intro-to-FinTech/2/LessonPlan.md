## 1.2 Lesson Plan - Deep Dive into FinTech

---

### Overview

Today's class will focus on command line basics and git (using a graphical user interface (GUI)) and then proceed to further investigating the key stimuli and impacts that have lead to the exponential growth of the FinTech industry. Specifically, students will develop the basic command line and git download/upload skills that will aid them in using the more advanced git CLI in the next lesson as well as learn more about the history of FinTech, the particular domains it has helped disrupt, and collaborate to create their own case studies on a particular FinTech (Payments) company.

### Class Objectives

By the end of class, students will be able to:

* Use the terminal/command line to execute basic file system operations.
* Download/upload files to GitHub using the git GUI.
* Deconstruct the factors that lead to the evolution of the FinTech industry.
* Map out the disrupted domains of the FinTech industry.
* Perform a case study on a FinTech (Payments) company.

### Instructor Notes

* Students may have trouble grasping the notion of the command line. Think of it like this, when students double-click into a folder to change directories, they are essentially executing a backend `cd` command that initiates upon the signal of a double-click into a folder. In other words, the GUI that a student sees is merely a visual overlay of the backend operations of the computer.

* Knowing a brief history of FinTech is just as important as knowing what FinTech is. Employers will want to know that students not only have the technical skills to perform their jobs, but also the contextual knowledge of what is happening in the financial services industry.

* Be thorough when explaining case study requirements and showcasing a completed case study for students to model off of. Case studies can vary widely in length depending on the audience for which it was written. Therefore, for the sake of the time, case studies should be comprehensive but shouldn't be overly long.  

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome (10 mins)

In this activity, instructors should take the time to welcome students back and exemplify the fact that in today's lesson, students will learn basic technical fundamentals (terminal and git GUI) that will be integral to their success as future developers. In addition, students will receive a more detailed overview into the background of FinTech, which will give them the contextual knowledge required for comprehending the changing landscape within the FinTech ecosystem. 

Perform the following:

* Explain that students will begin working with common developer tools such as the terminal/command line, a text-based utility for performing file system operations and executing programs, and git, a managed remote file repository with in-built versioning control. By the end of the day, students will look like hackers with their terminals open and join the ranks of millions of developers who also use git to store their files/code.

* Remind students that today's lesson will perform a technical deep dive into a brief historical background of FinTech, explain the reasoning for its current prevalence, focus in on the traditional domains or sectors within finance that FinTech has helped to disrupt, and delve into a single case study of an individual FinTech company. 

* Being aware of the background behind FinTech can be really useful, especially when applying to jobs because it shows that students not only care enough to familiarize themselves with the industry in which they'd like to work, but also showcases competence in understanding where potential opportunities (and pitfalls) within the FinTech industry may be.

* Encourage your students and get their energy levels up! Today will be a crash course on both hard and soft skills; students will learn technical skills and contextual knowledge to aid them in their future careers in FinTech.

---

### 2. Instructor Do: Terminal (10 mins)

In this activity, students will learn the basics of using the terminal/command line to perform basic file system operations on their machines.

Open up the terminal (Mac) or git-bash (Windows) and walk through the following commands:

  * `cd` (Changes the directory).

  * `cd ~` (Changes to the home directory).

  * `cd ..` (Moves up one directory).

  * `ls` (Lists files in the folder).

  * `pwd` (Shows the current directory).

  * `mkdir <FOLDERNAME>` (Creates a new directory with the folder name as <FOLDERNAME>).

  * `touch <FILENAME>` (Creates a new empty file with the file name as <FILENAME>).

  * `cat <FILENAME>` (Reads a file and outputs to the terminal)

  * `rm <FILENAME>` (Deletes a file).

  * `rm -r <FOLDERNAME>` (Deletes a folder recursively, make sure to note the -r).

  * `open .` (Opens the current folder on Macs).

  * `explorer .` (Opens the current folder on GitBash).

  * `open <FILENAME>` (Opens a specific file on Macs).

  * `explorer <FILENAME>` (Opens a specific file on GitBash).

  ![terminal-example](Images/terminal-example.png)

Slack out [CommonCommands.txt](Activities/03-Ins_Terminal/Solved/CommonCommands.md) for students to use as a reference. Answer any questions up until this point.

---

### 3. Students Do: File System Operations (15 mins)

In this activity, students will perform their own file system operations via the terminal/command line. 

**File:** [README.md](Activities/04-Stu_Terminal/README.md)

### 4. Instructor Do: Review File System Operations (5 mins)

Open [file_system_operations.sh](Activities/04-Stu_Terminal/Solved/file_system_operations.sh) and cover the following points:

  * `mkdir` creates folder directories.

  * `cd` navigates into specified folder directories.

  * `touch` will create an empty file.

  * `cat` reads files and outputs the results to the console.

  * `cd ..` will navigate up one level.

  * `cp` copies files from source to target.

  * `rm -r` recursively deletes all files in a folder (that may have sub-folders).

  * `mv` moves files from source to target. Can also be used to rename a file.

  * `ls` lists the contents of the current directory.

---

### 5. Instructor Do: Uploading files to Github (15 mins)

In this activity, students will learn how to upload files to GitHub, which will be used to submit their future homework assignments in the course. 

Briefly explain the following:

* GitHub offers a centralized location where developers can push and pull (upload and download) their code; GitHub always holds the most up-to-date code and files and handles everyone's updates appropriately. 

* For now, students will only be introduced to the GitHub GUI; however, in the next lesson, students will learn to work with Github through the terminal using git -- allowing for more advanced git operations.

Then, have the students follow along with the following steps:

* Visit <https://github.com> and ask students to login to their personal accounts. From the main page, create a new repository with an initialized `README.md` file. Explain that the convention in the software world is for each repository to have a "README" file that explains what the repository contains.

  ![git repo](Images/GitDemo_1.png)

* Switch back to the Desktop and create a new empty Excel file and save it. This will be used to demonstrate how to upload new files.

* Navigate back to Github website and click **Upload files**.

  ![upload file](Images/GitDemo_upload.png)

* Choose your Excel file in the dialog box; instead of the "Upload Files" button, you may also drag files from your desktop to the Github web page for a repo. Add a commit message and commit the changes.

* Finally, refresh the web page to show that the new file is now safely saved to the repository.

  ![drag file](Images/GitDemo_filedrag.gif)

Encourage students to practice using Github before the next class and to use office hours if they run into any problems.

---

### 6. BREAK (15 mins)

---

### 7. Instructor Do: Evolution of Fintech (15 mins)

In this activity, students will be given a detailed view into the historical progression of the FinTech space; students will learn from where FinTech has come and the potential reasons for how it came to be.

**File:** [slideshow-placeholder]()

Walk through the slideshow while presenting the potential historical factors leading to today's FinTech boom:

* `The Dot-Com Bubble`: The run-up to the early 2000's dot-com bubble can be characterized as having three main features that are helpful to understanding today's environement:

  * Investors were throwing money around due to a reduction in the capital gains tax (Taxpayer Relief Act of 1997) and therefore had lots of free-flowing capital.

  * There was a rise in tech talent as the bubble in capital also had the effect of freeing up many talented developers when companies went through the process of dissolution.

  * There was a lack of regulation of tech as the rise of services like Napster and LimeWire proved that technology was finally getting to the point that it _far_ outpaced regulatory agencies' ability to understand what they were and how to fairly regulate them.

* `The Great Recession`: In the following years, tech companies - especially web comapnies - began to grow in size as the economy recovered. However, 2007 as you may well know, marked the beginnings of the Great Recession due to the collapsing real estate bubble. 

* `The Rise of Mobile Phones`: 2007 also marked the launching of what is unequivocally one of the most influential advancements in recent history: the modern smartphone. Specifically the iPhone in 2007, with the first Android later the following year. Smartphones severely incerased the demand for talented programmers in both mobile and web development. They also changed our ability to _access_ information in quickly. Companies found themselves needing apps not because they wanted to be trendy, but because their clients would not interface with their products and services without the ability to do so while not at a computer. In some foreign markets, there are more people with smartphones than laptops, tablets, and desktops; meaning that if a service isn't available on an app, the service doesn't exist in the user's world.

* `Millenials`: The aughts and early teens additionally saw the generation known as millenials coming of age as income-earners and investors. Millenials already outnumber any other population group, and that proportion relative to baby boomers and generation x over time. In fact, they are projected to outnumber any other population group for quite a few decades to come. This means that understanding the needs and feelings of this highly diverse market sector will be important to companies that want to stay relevant. A few very important things characterize this generational group:

  * They have grown up with technology and thus demand internet-connected, user-friendly experiences

  * They are more likely to take on loans to pay for educational certifications

  * Their finances are somewhat shaped by a the combined economic effects of the Dot-Com bubble, the Great Recession, and student loans

  * They are less likely to own homes than previous generations, and tend to marry later in life

* `The Rise of the Data Overlords`: Beyond the recession, there has been a proliferation in the number of entities utilizing data in increasingly interesting ways. As companies continue to grow and seek additional methods to mitigate risk in pursuit of profit, increasing data sources and analytics tools offer a way forward.

  * As prices for more powerful processors and memory continue to decrease, it has become increasingly feasible to carry out the massive number of calculations required to accomplish machine learning (ML).

  * The use of machine learning and artificial intelligence - although often misunderstood by the general public as well as many investors - promises to find trends and strategies that humans would be otherwise incapable of finding

  * Many of the developers from the two last bust cycles are finding new roles in the new startup climate.

Ask the students if they have any questions before moving on.

---

### 8. Instructor Do: Facilitated Discussions to FinTech Domains (10 mins)

In this activity, the instructor leads students into the discussion of the current state of the FinTech industry, specifically where in the financial industry technological innovation has brought upon a positive impact. 

Ask the students the following questions:

* What are some potential areas in finance where technology has disrupted traditional finance activities?

  * **Answer:** Blockchain and financial transactions; robo advisors and investment management; and payment applications and money transfers are one of many possible answers.

* How did these technologies allow for the disruption of traditional finance?

  * **Answer:** Blockchain allows for cheaper and more secure transactional validation; robo advisors utilize machine learning algorithms for portfolio management, thereby reducing overhead costs; and payment applications utilize modern infrastructure such as mobile and cloud-based networking. 

* How might cloud-based networking, especially, contribute to the advent of start-ups and technological innovators?

  * **Answer:** Traditionally, hosting servers meant purchasing on-premise server farms with large up-front costs and regular maintenance, which was a barrier for entry for small startups. However, with cloud-based networking such as AWS, small startups and even individuals could quickly spin up servers faster and on an as needed basis, thereby minimizing time to deployment and reducing up-front costs -- allowing small startups to compete more efficiently with larger firms with existing infrastructures. 

* Where else might technology disrupt traditional finance?

  * **Answer:** Machine learning can be used in lending to more efficiently target customers who have a higher likelihood of paying back their loans while avoiding those who have a higher likelihood of *not* paying back their loans.

---

### 9. Instructor Do: Fintech Domains and Trends (15 mins)

In this activity, students will deep dive into the various domains of the FinTech ecosystem that have been bolstered by technological innovation. 

**File:** [slideshow-placeholder]()

Open the slideshow and walk through the following FinTech domains:

* Payments

  * By far the largest segment at the moment, mobile and internet payments have been increasingly important with the rise of web companies and monbile devices.

  * In general, these technologies reduce friction of peer-to-peer payments without the need for a bank to be involved. These systems are designed to be more convienent than cash, and significantly faster than checks.

  * Payments, _especially_ credit cards, are largely built on older technologies that could be disrupted in a variety of ways in order to reduce friction and increase payment approval speeds

  * Examples: Venmo, Stripe, PayPal, Square, Apple Pay, Android Pay, Amazon Payments, Plaid, Zelle, most Cryptos

* Investment Management

  * A broad area that promises both individuals and institutions better management of wealth in addition to applications for algorithmic trading.

  * Betterment, Acorns, Robinhood, Quantlab

* Capital Investment

  * growth of alternate modes for financing larger projects

  * IndieGoGo, Kickstarter, Kiva, eREIT's

* Enterprise Solutions

  * companies need better tech for a large variety of different things

  * Equifax NeuroDecision, JPM Coin, BofA Quartz, Analytics, Fraud detection

* Insurance

  * Insurance agencies looking to cut costs can reduce the number of physical locations they have, as well as taking advantage of new data sources in order to better understand their clients

  * Area is slow to adapt new technologies due to heavy regulation, but better use of machine learning and statistics could provide pathway to higher profit margins

  * Examples: Lemondade

* Deposits

  * Similar to insurance agencies, many banks are looking for ways to cut costs while providing more/better services.
    
  * Examples: CapitalOne, Ally
    
Then, overview the following overarching trends that appear across all domains of FinTech:

  * `Mobile accessibility is a must`: The rise of smartphones has made it a requirement that any new technology be accessible through a mobile site or app

  * `Use of machine learning and/or AI`: With the advent of more powerful processors and cheaper memory, the applications of machine learning have enabled even faster calculations and more accurate predictions than ever berfore.  

  * `Fintech as a social good`: A few of the big players such as Kiva and Lemonade are building companies that not only make profit, but also promote or fund nonprofits

  * `Banks have skin in the game`: Although many would like to paint the picture that banks are completely ignorant of the rise of fintech, it couldn't be further than the truth. Many of the largest banks are internally funding a multitude of fintech projects in order to stay ahead of the curve!

---

### 10. Student Do: Investigate FinTech Domains (20 mins)

By this point, students have been given examples of both the major domains within FinTech as well as the overarching trends across the industry. The instructor should now place students into groups of `2-4` individuals to conduct some research of the various FinTech domains on their own.

**File:** [README.md](01-Stu_FinTech_Domains/README.md)

### 11. Instructor Do: Review Investigate FinTech Domains (10 mins)

Now that students have had an opportunity to perform their own research on the various domains in FinTech, it's time to facilitate a discussion amongst the class on each group's findings.

* Have each group present their findings to the class one-by-one until all groups have presented.

* Presentations should be quick, approximately `1-2` minutes.

---

### 12. Instructor Do: Stripe Payments Case Study (10 mins)

In this activity, students will be instructed on how to create a FinTech case study -- a compilation of holistic research performed on a FinTech company or technology. This activity is particularly important as it will serve as the knowledge foundation for students completing their FinTech case studies for the unit `1` homework.   

**File:** [slideshow-placeholder]()

Open the slideshow while walking through the following:

* For this case study, we have decided to cover the payment processing known as Stripe, Inc. Not only does it allow us to discuss the ubiquitous world of online payments, Stripe is also an examplar of how a company can generate significant profits by lowing barriers of entry for other businesses.

* When we go to a website, we often take for granted how easy it is to pay for goods and services. Behind the scenes, there has to be a payment processor that walks through the entire ACH (Automated clearing house) submittal process with an operator, verifies payment info, verifies the transaction, communicate with both the bank and the credit card issuer to greenlight the transaction, and notify the end-user of a success or failure. In addition, that system also needs to verify the handshakes between all of those systems and institutions, make sure that every step along the way is secure, and ensure that it is resistant to errors in transmission.

* Oh, and did we also mention it has to be fast? Users tend to become _exceptionally_ anxious if it takes more than 3 seconds to load a page, and studies show that more than half of your users will leave if you don't meet that bar.

* As a programmer facing all of these technical issues, it would be _super_ awesome if someone were to swoop in and take 90% of the work for this off your hands. Enter Stripe.

* Stripe is a payment processing company founded in 2011 that provides a tiny, 8-line set of code that takes the load off of building a payment system into most android, iOS, and web applications. For this service, Stripe charges a relatively small fee on processed payments.

* By integrating Stripe, a developer can dramatically increase their development speeds, while *trust*ing that Stripe will handle much of the security and performance of payments. Anyone building a modern application will likely lean on Stripe as a go-to solution for the first implementation of their application, which has had great financial benefits for Stripe and their target users (developers).

* Stripe is by no means the only pony in town for this service though! Companies such as Plaid, PayPal (through Braintree), Square, and more have developed their own, similar solutions.

---

### 13. Student Do: FinTech Payments Case Study (20 mins)

In this activity, the instructor should place students into groups of `2-4` individuals once again to create a case study on a particular FinTech payments technology that rivals Stripe.

**File:** [README.md](02-Stu_FinTech_Case_Study/README.md)

### 14. Instructor Do: Review FinTech Payments Case Study (10 mins)

In this activity, students will present their case study findings to the class.

Before proceeding with presentations, mention the following:

* The secondary goal of this activity was to hone students' communication and presentation skills. Point out the importance of these soft skills in the FinTech career space and give specific examples in your own careers where they've applied. 
    
* Make sure to think about the audience in both oral as well as written presentations. Fellow students like themselves who are new to the FinTech space will require language that is communicated in such a way that avoids using too many esoteric terms and instead provides clear easy to understand content.

* Each person in the group is expected to speak during the presentation. Emphasize the importance of public speaking, and let students know that there will be more opportunities throughout the course for them to present on various fintech topics. 

Then, allow groups `1-2` minutes to quickly present their findings.

### End Class

---

Trilogy Education Services © 2019. All Rights Reserved.