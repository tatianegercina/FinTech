## 1.2 Lesson Plan: Deep Dive into FinTech

---

### Overview

Today's class will focus on command line basics and git, using a graphical user interface, or GUI. It will then further investigate the key factors leading to the exponential growth of the FinTech industry.

Specifically, students will be introduced to basic command line and git download/upload skills, which will help them use the more advanced git CLI in the next lesson; learn more about the history of FinTech and the areas it has disrupted; and collaborate to create their own case studies for a FinTech company.

### Class Objectives

By the end of class, students will be able to:

* Use the command line to execute basic file system operations.

* Download and upload files to GitHub using the git GUI.

* Describe the factors that led to the evolution of the FinTech industry.

* Map out the disrupted domains of the FinTech industry.

* Create a case study based on a FinTech company.

### Instructor Notes

* Students may have trouble grasping the notion of the command line. You can explain it like this: when students double-click on a folder to change directories, they are essentially executing a backend `cd` command. The GUI that a student sees is merely a visual overlay of the backend operations of the computer.

* Emphasize that understanding the history of FinTech is just as important as knowing what FinTech is. Employers will measure candidates not only by their technical skills, but also by their contextual knowledge of what is happening in the financial services industry.

* Be thorough when explaining case study requirements and showcasing a completed case study for students to use as a model. Case studies can vary widely in length depending on the audience for which it was written. Therefore, for the sake of the time, case studies should be comprehensive but not overly long.  

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome (10 min)

Take some time to welcome students back to class and introduce the topics that will be covered in this lesson: command line and git GUI fundamentals, and a brief history of FinTech. This lesson will give students both the skills and knowledge required to gain a deeper understanding of the changing landscape within the FinTech ecosystem.

Cover the following points:

* Students will begin working with common developer tools such as the command line, a text-based utility for performing file system operations and executing programs. They will also learn git, which is a managed remote file repository with built-in version control. By the end of the day, students will join the ranks of millions of developers who also use git to store their files/code.

* Today's lesson will be a (brief) deep dive into FinTech's historical background, in which we'll cover why FinTech is so prevalent today, the financial sectors it has helped to disrupt. We'll also delve into a FinTech case study.

* Understanding and being able to discuss FinTech's history is useful, particularly when applying to jobs; it will show employers that you care enough to familiarize yourself with the industry, as well as showcase an understanding of potential opportunities and pitfalls within the industry.

Encourage the students and get them excited for the lesson. Tell them that today will be a crash course in both hard and soft skills; students will learn technical skills and contextual knowledge to aid them in their future careers in FinTech.

---

### 2. Instructor Do: Introduction to the Command Line (10 min)

In this section, students will learn the basics of using the command line to perform basic file system operations on their machines.

**File:** [slideshow-placeholder]()

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

### 5. Instructor Do: Anaconda Virtual Environments (20 min)

In this activity, instructors guide students on how to use the command line to execute third-party commands such as the `conda` command line interface (CLI), representing the popular Anaconda Distribution. Students will use the `conda` CLI to make sure Anaconda is properly installed on their machines as well as create and initialize a Python virtual environment in preparation for Unit 2 and beyond.

Complete a quick check to ensure students have Anaconda installed and that `conda` is added to their PATH environment variable.

* Open up the console and have students follow along.

  * Enter `conda --version` which will display the version of Anaconda install.

    ![Anaconda Version](Images/conda_version.png)

* Have TAs help any students with issues. The most common problem will be students with Windows that don't have the Anaconda PATH variable set.

  * This can be fixed by manually adding the PATH to Windows' environment variables, but can be more easily solved by uninstalling/reinstalling Anaconda and making sure to check the "Install to Path" box that comes up in a menu.

Next move on to explaining [virtual environments](https://conda.io/docs/user-guide/tasks/manage-environments.html).

* Virtual environments create an isolated environment for Python projects.

* Explain how different projects can have different dependencies.

* Explain how different projects might also use different types and versions of libraries.

* This virtual environment will make sure the class has all the right dependencies for future class activities.

Create a virtual environment that will run Python 3.7. This will help solve issues where students have multiple versions of Python installed.

* First run `conda create -n PythonData python=3.7 anaconda` in the terminal. Warn students that this may take a few minutes to install.

* Now enter `source activate PythonData` to activate the environment. When `(PythonData)$` appears, this means you are in the environment.

* Now make sure everyone is using the correct version of Python by entering `python --version`.

  ![Python version](Images/python_version.png)

* Lastly, show that you can exit the environment by entering `source deactivate`. If `source deactivate` does not work, try using `conda deactivate` instead.

Remind students that they will need to activate their environment each time that they open a new terminal. Windows users should always use `git-bash` for their terminal.

---

### 6. BREAK (15 min)

---

### 7. Student Do: Rip Van Winkle Thought Exercise (5 min)

In this activity, students think about how the current state of the FinTech world may differ from that of someone from the year 1999.

Quickly explain to the class the following:

* The story of Rip Van Winkle represents a short story by the American author Washington Irving, first published in 1819, that follows a Dutch-American villager in colonial America named Rip Van Winkle who falls asleep in the Catskill Mountains and wakes up 20 years later, completely missing the events of the American Revolution.

* Adapting the Rip Van Winkle story to FinTech, imagine if a financial analyst fell asleep in the year 1999 and woke up today, what would be most surprising about the finance world?

* Students should define areas of finance that have been deeply affected by technology, naming specific companies, products, or innovations that would be surprising to a sleeper from 1999.

* Students should form groups of 3-4 individuals and will be expected to quickly present their thoughts in the following review activity.

---

### 8. Instructor Do: Review Rip Van Winkle Though Exercise (15 mins)

In this activity, students present their opinions regarding the FinTech Rip Van Winkle thought experiment.

Perform the following:

* Give each group approximately 1-2 minutes to present their opinions on what would be most surprising to a sleeper from 1999 witnessing the current state of the finance world.

* Take note of each group's findings and emphasize some of the overarching themes regarding the state of the current FinTech ecosystem. For example, some themes that are likely to present themselves are:

  * Automation
  * Big Data
  * Mobile Infrastructure
  * Cloud Infrastructure

### 9. Instructor Do: Evolution of FinTech (15 min)

In this section, give students a brief summary of some of the key factors leading to the growth of the FinTech space. Understanding the historical background of FinTech as well as its current trajectory will give students knowledge that will help them both in employer interviews and their FinTech career.

**File:** [slideshow-placeholder]()

Open the slideshow and use the slides to review the key historical factors leading to the present-day FinTech boom:

* Mobile Infrastructure and Shifting Consumer Preferences

  * With the advancement in mobile network infrastructure (2G, 3G, 4G LTE), consumers have become more connected to the internet (as well as each other) than ever before. As a result, consumers not only have a greater resource pool to cross-check and validate information (e.g., checking prices) but also have become a resource pool themselves in which companies look to target for business.

  * Consumers today demand quick, reliable, and quality channels of engagement. Modern-day consumers often place their trust in a company that boasts a dynamic and beautiful website, a well-designed and efficient mobile application, and––ideally––a social user platform that allows customers to connect with others using the same product or service.

  * Therefore, companies have been forced to make large investments in technology in order to stay competitive with their industry peers. Consumers have more product choices and are loyal to companies they trust. Therefore, the technological channels affecting consumer engagement have a direct impact on a company's ability to market themselves and, ultimately, capitalize on demand.  

* Big Data

  * Over the years, computer processing units (CPUs), random access memory (RAM), and hard drive storage devices have become both more powerful and less expensive. Therefore, more companies were able to purchase and utilize large clusters of computers working in parallel.

  * Parallel processing paradigms have also shifted to become more efficient. Traditionally, to enable machines to work in parallel, the concept of MapReduce was born. With MapReduce, data workloads were split among multiple machines for disk-based processing, and then reaggregated at the end to produce the result. However, with the advent of Spark, that same process has been refined for in-memory processing, in which data workloads utilize RAM that is much faster (though more costly) at processing data.

  * Because big data processing has become more efficient, the time needed to curate and analyze data has also decreased. Therefore, modern-day companies are able to employ tactics like machine learning to drive business decision-making in real time.

  * Companies have placed enormous emphasis on technological investment due to the growing feasibility and allure of housing large clusters of machines to drive real-time, data-driven analysis.

* Cloud Infrastructure

  * Traditionally, server farms, or large clusters of machines, required large upfront costs and overhead related to server maintenance. With the inception of cloud computing, however, companies no longer had to purchase their own servers for their data-processing needs, but instead could "rent" servers from another vendor on an as-needed (and, therefore, much cheaper) basis. This allowed smaller companies to compete with larger, more established companies in regard to utilizing big data.

  * In addition, because cloud vendors like Amazon Web Services (AWS) manage hosting and deployment of servers in the cloud, the time-to-market for companies to reap the benefits of investing in technology has decreased, as they are able to push their applications and features quicker.

  * The business landscape has become increasingly competitive, as smaller companies now have the capabilities to disrupt markets with their fully fledged, productionalized applications and services––which previously would have required large upfront costs, a barrier to entry of the industry.  

Answer any questions before moving on.

---

### 10. Instructor Do: Facilitated Discussion About FinTech Domains (10 min)

This section will be a discussion of the current state of the FinTech industry and which financial sectors have been positively impacted by technological innovation.

Ask the students the following questions:

* What are some areas in the financial industry where technology has disrupted traditional finance activities?

  **Sample Answer:** Blockchain and financial transactions; robo advisors and investment management; and payment applications and money transfers.

* How did these technologies allow for the disruption of traditional finance?

  **Sample Answer:** Blockchain allows for cheaper and more secure transactional validation. Robo advisors utilize machine learning algorithms for portfolio management, thereby reducing overhead costs.  Payment applications utilize modern infrastructure such as mobile and cloud-based networking.

* How might cloud-based networking contribute to the advent of start-ups and technological innovators?

  **Sample Answer:** Traditionally, hosting servers meant purchasing on-premises server farms with large upfront costs and regular maintenance, which was a barrier for entry for small startups. However, with cloud-based networking such as AWS, small start-ups and even individuals can quickly spin up servers faster and on an as-needed basis, thereby minimizing time to deployment and reducing up-front costs. This allows small startups to compete more efficiently with larger firms with existing infrastructures.

* Where else might technology disrupt traditional finance?

  **Sample Answer:** Machine learning can be used in lending to more efficiently target customers who have a higher likelihood of paying back their loans, while avoiding those who have a higher likelihood of *not* paying back their loans.

---

### 11. Instructor Do: FinTech Domains and Trends (10 min)

This section is a deep dive into the various domains of the FinTech ecosystem that have been bolstered by technological innovation.

**File:** [slideshow-placeholder]()

Open the slideshow and review the following FinTech domains:

* Payments and Remittances

  * Currently representing the largest segment of the FinTech space, digital payments have become increasingly widespread with the growth of e-commerce and mobile device infrastructure.

  * Distributing credit card numbers over the internet proved to be insecure (and costly) in the past. Thus, digital payment technologies were designed for not only security, but overall speed and convenience as well.

  * Examples: Venmo, Stripe, PayPal, Square, Apple Pay, Android Pay, Zelle, cryptocurrencies

* Robo Advisors and Personal Finance

  * Robo advisors and personal finance companies provide wealth management, investment, and budgetary services that seek to help customers with their overall capital management and investments.

  * Often, wealth management solutions are driven by machine learning with automated trading and portfolio re-balancing, while budgetary services utilize machine learning to scan a customer's purchase history and identify buying habits to suggest areas in which they can save.

  * Examples: Betterment, Acorns, Robinhood, Personal Capital

* RegTech

  * RegTech companies manage the regulatory and compliance processes within the financial industry through technology.

  * These types of companies use machine learning to identify and prevent instances of fraud, money laundering, or breaches in data.

  * Examples: Apiax, Finform, Trulioo, ClauseMatch.

* Digital Banking

  * Digital banking consists of online banks that seek to provide higher account interest rates by reducing the capital overhead associated with physical branches/bank locations.

  * Examples: Ally Bank, ING Direct

* InsurTech

  * InsurTech utilizes the benefits of machine learning to more efficiently group customers into risk profiles in order to provide the right type of insurance product.

  * Fine-tuning the determination of customer risk profiles minimizes costs to those who would have been lumped together in a broader customer risk profile.  

  * Examples: Lemonade, Slice, Ladder

* Alternative Finance

  * Alternative finance refers to the financial channels outside of the realm of traditional finance, such as regulated banks and capital markets, that facilitate capital borrowing and lending.

  * Popular **crowdfunding** and **peer-to-peer** lending channels have emerged in this domain.

  * Examples: Indiegogo, Kiva, LendingClub

![fintech-ecosystem](Images/fintech-ecosystem.png)

Answer any questions before moving on.

---

### 12. Student Do: Investigating FinTech Domains Part I (15 min)

By this point, students have been given examples of the major domains within FinTech as well as the overarching trends across the industry. Now, students will work together in groups of 3-4 individuals to research and produce a broad summary overview of one of the FinTech domains.

**File:** [README.md](Activities/03-Stu_FinTech_Domains_Part_I/README.md)

---

### 13. Student Do: Investigating FinTech Domains Part II (20 min)

 Now, students will work together in groups of 3-4 individuals to research and produce hypothetical headlines for each FinTech domain that one could expect to witness within the next 2-3 years.

**File:** [README.md](Activities/04-Stu_FinTech_Domains_Part_II/README.md)

### 14. Instructor Do: Review FinTech Headlines (20 min)

Now that students have had an opportunity to perform their own research on the various domains in FinTech and produce hypothetical news headlines for each FinTech domain, it's now time to facilitate a class discussion based on each group's findings.

Open up [GroupMap](https://www.groupmap.com/), a collaborative brainstorming service, and perform the following:

* Create sections within the mapping document for each FinTech domain:

  * Payments and Remittances
  * Robo Advisors and Personal Finance
  * RegTech
  * Digital Banking
  * InsurTech
  * Alternative Finance

* Once the GroupMap document is created and set up, slack out the link to the class and have each group list their headlines for each FinTech domain.

* Then, have each student in the class vote on the best headlines for each FinTech domain, with an emphasis on feasibility. When finished, tally up the votes and showcase the most popular headlines for each FinTech domain. Ask for any volunteers who are willing to share why they chose the particular news headline that was voted the most popular.

After the GroupMap review is complete, explain the following:

* The intent of this activity was to provide students with not only the breadth but also the depth of knowledge for each FinTech domain. This may prove to be valuable when applying for roles within the FinTech industry.

* It is not enough to simply restate the past, but also to analyze and predict the future. Therefore, after this activity students should have a general idea as to the trends affecting each FinTech domain as well as the potential outcomes that may result for each domain within the near future.

Ask students if they have any questions before moving on.

### End Class

---

© 2019 Trilogy Education Services
