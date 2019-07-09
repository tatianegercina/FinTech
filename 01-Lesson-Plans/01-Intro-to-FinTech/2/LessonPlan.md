placeholder

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

**File:** [slideshow-placeholder]()

Open the slideshow and present the following questions and answers:

  * What is a Terminal?

    * **Answer:** A terminal/commandline is an interface in which a user can type and execute text based commands.

  * When should one use a Terminal?

    * **Answer:** A terminal can be used at any time over a Graphical User Interface (GUI) as the GUI is merely a visual overlay to the programs executed via the terminal. In addition, when remotely connecting to a server, such as via the Secure Shell Protocol (SSH), a GUI wil not be provided. 

  * Why use a Terminal?

    * **Answer:** Using a terminal is efficient as it does not need to expend the additional processing to produce the visuals associated with a Graphical User Interface (GUI).

Then, open up the terminal (Mac) or git-bash (Windows) and walk through the following commands:

  * `cd` (Changes the directory).

  * `cd ~` (Changes to the home directory).

  * `cd ..` (Moves up one directory).

  * `ls` (Lists files in the folder).

  * `pwd` (Shows the current directory).

  * `mkdir <FOLDERNAME>` (Creates a new directory with the folder name as <FOLDERNAME>).

  * `touch <FILENAME>` (Creates a new empty file with the file name as <FILENAME>).

  * `code <FILENAME>` (Opens up a file in the VS Code editor).

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

  * `code` open files in the VS Code editor.

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

In this activity, students will be given a brief summary on some of the key components of the past that have lead to the current exponential growth of the FinTech space. Knowing the factors leading to FinTech's prevalence as well as its future trajectory should give students the contextual knowledge to succeed in future employer interviews and eventually careers in the FinTech industry.

**File:** [slideshow-placeholder]()

Walk through the slideshow while presenting the potential historical factors leading to today's FinTech boom:

* `Mobile Infrastructure & Shifting Consumer Preferences`

  * With the advancement in mobile network infrastructure (2G, 3G, 4G LTE), consumers have become more connected to the Internet (as well as each other) than ever. As a result, consumers not only now have a greater resource pool to cross-check and validate information (ex. checking prices) but also have become a resource pool themselves in which companies look to target for business.

  * Consumers these days now demand quick, reliable, and quality channels of engagement. Modern-day consumers will often place their trust in a company that boasts a dynamic and beautiful website, a well-designed and efficient mobile application, and (if possible) a social user platform for connecting with others using the similar product.

  * Therefore, companies have been forced to make large investments in technology in order to stay competitive amongst their industry peers. Consumers more than ever have more product choices to pick from and are loyal to those companies they trust. Thus, the technological channels affecting consumer engagement have a direct impact to a companies ability to market themselves and ultimately capitalize on demand.  

* `Big Data`

  * Throughout the years Computer Processing Units (CPUs), Random Access Memory (RAM), and hard drive storage devices have become more powerful while also becoming much cheaper. Therefore, as time progressed, more companies were able to purchase and utilize large clusters of computers working in parallel.

  * Parallel processing paradigms have also shifted to become more efficient. Traditionally, to enable machines to work in parallel, the concept of MapReduce was born in which data workloads were split amongst multiple machines for disk-based processing and re-aggregated at the end to produce the result. However, with the advent of Spark, that same process has been refined for in-memory processing, in which data workloads utilize RAM that is much faster (ableit costlier) at processing data.

  * Because Big Data processing has become much more efficient, the time to curation of data and subsequent analysis has also decreased. Therefore, modern-day companies are able to employ tactics like machine learning to drive business decision-making in real time.

  * Thus, companies have placed an enormous emphasis on technological investment due to the growing feasibility and allure of housing large clusters of machines to drive real-time data-driven analysis.

* `Cloud Infrastructure`

  * Traditionally server farms, or large clusters of machines, required large up-front costs and overhead related to server maintenance. With the inception of cloud computing however, companies no longer had to purchase their own servers for their data processing needs, but instead could "rent" servers from another vendor on an as needed and therefore much cheaper basis. This lead to the ability for smaller companies to compete with larger more established companies in regards to utilizing Big Data.

  * In addition, because cloud vendors like Amazon Web Services (AWS) managed hosting and deployment of servers in the cloud, the time-to-market for companies to reap the benefits of investing in technology decreased as they were able to push their applications and features quicker.

  * As a result, the landscape for business has become increasingly more competitive as smaller companies now have the capabilities to disrupt markets with their fully-fledged productionalized applications and services that previously would have required large up-front costs that acted as barriers to entry of the industry. 

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

* `Payments & Remittances`

  * Currently representing the largest segment of the FinTech space, digital payments have become increasingly widespread with the growth of e-Commerce and mobile device infrastructure.

  * Distributing credit card numbers over the Internet proved to be insecure (and costly) in the past. Thus, digital payment technologies were designed for not only security, but overall speed and convenience as well.

  * Examples: Venmo, Stripe, PayPal, Square, Apple Pay, Android Pay, Zelle, Cryptocurrencies

* `Robo Advisors & Personal Finance`

  * Robo advisors and personal finance companies provide wealth management, investment, or budgetary services that seek to help customers with their overall capital management and investments. 

  * Often, wealth management solutions are driven by machine learning with automated trading and portfolio re-balancing, while budgetary services utilize machine learning to scan through a customer's purchase history and identify buying habits to suggest areas in which they can save.

  * Betterment, Acorns, Robinhood, Personal Capital

* `RegTechs`

  * RegTech companies manage the regulatory/compliance processes within the financial industry through technology.

  * These types of companies use machine learning to identify and prevent instances of fraud, money laundering, or breaches in data.

  * Examples: Apiax, Finform, Trulioo, ClauseMatch.

* `Digital Banking`

  * Digital Banking consists of online banks that seek to provide higher account interest rates by reducing the capital overhead associated with physical branches/bank locations.

  * Examples: Ally Bank, ING Direct

* `InsurTechs`

  * InsurTechs utilize the benefits of machine learning to more efficiently group customers into respective risk profiles and provide the right type of insurance product. 

  * Fine-tuning the determination of customer risk profiles minimizes costs to those who would have been lumped together in a more broad customer risk profile.  
    
  * Examples: Lemonade, Slice, Ladder
    
* `Alternative Finance`

  * Alternative Finance refers to the financial channels outside of the realm of traditional finance, such as regulated banks and capital markets, that facilitate capital borrowing and lending.

  * Popular *crowdfunding* and *peer-to-peer* lending channels have emerged in this domain.

  * Example: Indiegogo, Kiva, LendingClub

![fintech-ecosystem](Images/fintech-ecosystem.png)

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

Open the slideshow and walk through the following:

* `Background`

  * This case study studies the payment processing company known as Stripe. Stripe is an examplar Digital Payments company that provides the technical, fraud prevention, and banking infrastructure required to operate online payment systems.

* `Use Case`
  
  * Behind the scenes of digital payments, there is a payment processor that walks through the entire ACH (Automated clearing house) submittal process with an operator, and verifies the payment info, transaction, and communication between the bank and the credit card issuer for approval/denial and subsequent notification of payment success or failure. Therefore, the system needs to verify the handshakes between all processes and institutions, and make sure that every step along the way is secure.

* `Advantages`

  * Stripe provides a tiny 8-line set of code that offloads the deployment of a digital payments system for most Android, iOS, and web applications. For this service, Stripe charges a relatively small fee on every processed payment.

* `Competitors`

  * Similar companies such as PayPal, Apple, Google, Square, and many others have developed similar solutions.

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