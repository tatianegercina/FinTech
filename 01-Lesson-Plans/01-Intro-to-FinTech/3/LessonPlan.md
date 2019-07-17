## 1.3 Lesson Plan: FinTech Collaboration

---

### Overview

In today's class, students will learn how to utilize the git command line interface (CLI) and create markdown files to generate FinTech case studies that can be collaboratively stored, accessed, modified, and previewed in an online git or file repository such as GitHub. A solid understanding of the git CLI and knowing how to create markdown files will help students properly manage git repositories and construct visually enhanced README files.

### Class Objectives

By the end of class, students will be able to:

* Configure the git CLI user credentials from the terminal.

* Clone a repository using `git clone`.

* Modify git repositories by adding, committing, and pushing files.

* Create markdown files and implement its additional visual capabilities: text formatting, images, links.

* Collaboratively write a FinTech case study in markdown and host it in an online git repository.

### Instructor Notes

* Today's lesson may make students feel uneasy as they continue to use the command line to interact with both files on their local file system as well as files that are actively tracked via an online repository. Calm students' nerves by telling them that git is merely a command line tool––a program that exists on the local file system that executes from the command line, or terminal.

* Make sure that by the end of class students have the tools to create well-presented markdown README files to host in their git repositories. They'll need these to showcase their git repositories (and the coding assets within them) to potential future employers.

* More advanced git operations such as git branches, merges, and checkouts will not be introduced in this lesson. Therefore, be aware that students may face merge conflicts that prevent them from pushing their file changes to the git repository when collaborating with others working in the same git repository.

* Be mindful of students working in groups during the case study activity; some students may be less vocal than others. Circulate the classroom with the TAs and make sure that every student is actively engaged and has a voice in their respective groups.

* Have your TAs keep track of time with the [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome Class (5 min)

**Files:**

* [Slideshow](placeholder)

Welcome students to the third day of class and the final lesson of Unit 1.  Cover the following points:

* The previous lessons focused on introducing students to the FinTech course structure as well as FinTech more broadly. We have discussed the history and current landscape of the FinTech ecosystem, as well as notable case studies of technological disruptors in this space. Today, students will combine what they've learned so far about the FinTech industry to create their own case studies that can be hosted in online git repositories and previewed as visually enhanced markdown files.

* Mention to the class that today's goal is twofold: (1) to manage their own git repositories and develop in shared repositories, and (2) to develop text-based assets, such as a FinTech case study, in markdown to provide visually appealing README files that can be previewed in GitHub (and, therefore, showcased to potential employers).

* In this lesson, students will be divided into groups and given a selection of FinTech case study proposals to choose from. Students will need to work collaboratively and generate a visually appealing document that can be hosted online––which is where git CLI and markdown comes in!

* Energize your students! Remind them that they'll be using collaborative tools (git) that real developers and industry professionals use to share and build upon code.

---

### 2. Instructor Do: Git GUI (10 min)

In this activity, students will learn how to create and download a git repository, use the command line to navigate to and edit a text file in the local repository folder, and then upload the file to the git repository. This section serves as a precursor to the following git CLI activities, as it showcases the limitations of downloading a repository as a local folder versus performing a git clone in which git can track and compare changes.

First, quickly present the following questions and answers:

* What is git?

  **Answer:** Git is a version-control system for tracking changes in files––often from a coding and software development standpoint. Git is designed for coordinating work among programmers, but it can be used to track changes in any set of files.

* What is a git repository?

  **Answer:** A git repository is a remote or online file repository in which git tracks files and conducts version control as changes are made.

* How is git used?

  **Answer:** Git is often used via the command line, but vendors such as GitHub or GitLab provide web/desktop apps that allow users to use git via a GUI.

* What is GitHub?

  **Answer:** GitHub is a web-based file-hosting service that is one of the many vendors that uses Git for file version control.

* Why is git important?

  **Answer:** Git is an extremely powerful tool for software development. It has become the standard for versioning software and data science tools across all industries, and is even used to version data and enhance data reproducibility. For these reasons, GitHub proficiency has become a critical job skill. In fact, it will be one of the most essential job skills in students' careers in FinTech.

Then, perform a live demo while highlighting the following:

* Git repositories can be created via the GitHub website. Check the option to "Initialize this repository with a README" to automatically deploy the repository once created.

  ![github-website](Images/github-website.png)

  ![github-create-repository](Images/github-create-repository.png)

* A git repository can then be downloaded locally as a compressed ZIP file from GitHub.

  ![github-download](Images/github-download.png)

* After unzipping, or decompressing, the ZIP file, the extracted git repository folder can be accessed via the terminal by performing a `cd` command to change directory inside the folder. The `ls` command with the `-l` parameter displays its contents in list format.

  ![terminal-git-repository](Images/terminal-git-repository.png)

* The `code` utility opens text files from the command line in VS Code for editing.

  ![terminal-vscode](Images/terminal-vscode.png)

  ![vscode-editor](Images/vscode-editor.png)

* Here, the file `README.md` is edited and saved in the local git repository. However, changes are still local and will need to be pushed to the remote repository.

  ![git-local-change](Images/git-local-change.png)

* Files can be committed and changed in the git repository via GitHub by clicking on the `Upload files` tab and navigating to the file upload webpage.

  ![github-upload-files](Images/github-upload-files.png)

  ![github-remote-change](Images/github-remote-change.png)

* The `README.md` preview in GitHub confirms the change.

  ![github-remote-change-confirmation](Images/github-remote-change-confirmation.png)

Answer any questions before moving on.

---

### 3. Student Do: Create and Personalize a GitHub Repo (15 min)

In this activity, students will follow the steps in the preceding instructor demo to create their own git repository and modify their README files to personalize their GitHub repository.

**Instructions:** [README.md](Activities/01-Stu_Refresher/README.md)

### 4. Instructor Do: Review Create and Personalize a GitHub Repo (5 min)

Review the previous activity with students, highlighting the following points:

* Make sure to initialize the new GitHub repository with a `README.md` file. Otherwise, deployment of the repository will be halted until further setup is completed.

  ![github-create-repo-uninitialized](Images/github-create-repo-uninitialized.png)

* When downloading the GitHub repository as a ZIP file, contents must first be extracted in order to edit any of the files.

  ![github-repo-unzipped](Images/github-repo-unzipped.png)

* The `code` command line utility is often used as a quick shortcut to jump from the terminal to editing files directly in VS Code.

  ![vscode-familiarity](Images/vscode-familiarity.png)

* After modifying the `README.md` file on the local file system, changed files will have to be pushed or re-uploaded to the online repository.

  ![github-file-upload-update](Images/github-file-upload-update.png)

* GitHub should automatically be able to preview `.md`, or markdown, files, as they contain style formatting elements and therefore should immediately reflect the changes of the updated `README.md` file. If not, manually refresh the page.

  ![github-readme-update](Images/github-readme-update.png)

---

### 5. Instructor Do: Git CLI (10 min)

In this section, students will be introduced to the git CLI, which will allow them to more efficiently track changes to a git repository by providing additional git operations.  

**Files:**

* [Slideshow](https://docs.google.com/presentation/d/1OAbxqe1yZKGMN2IxRPfNXnXT6Bem1oD7gFr47inJMos/edit#slide=id.g473a132ac1_0_7)

Open the slideshow and use slides 1–22 to review the following points about git:

* How does the GitHub web app differ from the git CLI?

  * The GitHub web app provides a convenient user interface for performing common git operations. The git CLI, however, is a command line utility that provides all git operations and is generally more robust than a git-based graphical user interface (GUI).
  
  * This is due to the fact that, more often than not, a GUI interacts with the underlying CLI to perform its functionality (e.g., click a button that executes a command on the back-end) and, therefore, is often a simplified version of the underlying functionality.

* What are the popular commands of the git CLI?

    * `git clone`: Clones a git repository to the local file system.

    * `git add`: Adds changed files to the queue of tracked files ready to be committed.

    * `git commit`: Adds tracked files as a bulk checkpoint ready to be pushed to the remote git repository.

    * `git push`: Uploads changed files from the local git repository to the remote git repository and updates the remote files.

    * `git pull`: Downloads changed files from the remote git repository to the local git repository and updates the local files.

* What is a git commit?

  * Before changed files are pushed from a local git repository to the remote git repository, a git commit saves a queue of tracked changed files as a **save** or **checkpoint** for a git repository.
  
  * This way, should it be necessary, a git repository can be restored to a previous checkpoint in time, thereby undoing any existing changes from that point.

* What is git's "snapshot" model?

  * Git thinks of its data more like a series of snapshots of a miniature file system. Every time you commit, or save the state of your project in git, it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot.
  
  * To be efficient, if files have not changed, git doesn’t store the file again; rather, it stores a link to the previous identical file it has already stored.

  ![Git Snapshot Model](https://git-scm.com/book/en/v2/images/snapshots.png)

Answer any questions before moving on.

---

### 6. Instructor Do: Git CLI (10 min)

In this section, you will demo how to add folder structures to their newly created GitHub repositories.

Demo the following with your students:

* Revisit the GitHub website and click on the "Clone or download" button.

* This time, copy the URL, as it represents the GitHub repository link (which will be used for the `git clone` command).

  ![github-url](Images/github-url.png)

* Open the command line and run `pwd` to determine the current work directory. Then, perform the `cd` operation to navigate to the desktop.

  ![terminal-pwd-cd](Images/terminal-pwd-cd.png)

* Run `git clone <repository link>` to clone the repo to the current directory. Copying a repository via the `git clone` command differs from just downloading a ZIP file of the repository. `git clone` downloads a tracked git repository to the local file system, while the ZIP file merely downloads the contents without any kind of tracking or version control involved.

  ![git-clone](Images/git-clone.png)

* Create three folders in the local git repository via the `mkdir` command: `data`, `references`, and `code`. Add a `.gitkeep` file to each folder so that git knows to retain the folders. (Git refrains from keeping empty folders unless explicitly told to do so.)

  ![git-repository-mkdir](Images/git-repository-mkdir.png)

  ![git-repository-gitkeep](Images/git-repository-gitkeep.png)

* Once the folders and files have been created, go to the command line and navigate to the root of the git repo folder. Run the following lines to push the changes to the remote git repository:

**Note:** Be sure to explain each piece of code as you run it.

  ```bash
  # Displays git untracked/tracked status of files in the folder
  git status

  # Adds all files and sub-folder files into a staging area
  git add .

  # Performed again to check that the files were added correctly
  git status

  # Commits all the files to your repo and adds a message
  git commit -m <add commit message here>

  # Pushes the changes up to GitHub
  git push
  ```

* Navigate to the GitHub repository to confirm that the changes have been pushed up.

  ![git-push-results](Images/git-push-results.png)

Make sure all students were able to successfully clone a repository, add files to the repo, commit the changes, and then push the changes to GitHub all from the command line. Ask your TAs to assist students if needed.

---

### 7. Student Do: GitHub Reorganized (15 min)

In this activity, students will use the git CLI to clone their git repositories to their local file systems, and then add directories to their GitHub repositories.

**Instructions:** [README.md](Activities/02-Stu_Git_CLI/README.md)

### 8. Instructor Do: Review GitHub Reorganized (10 min)

In this section, review the previous activity and take some time to answer students' questions.

First, ask students if they have any questions, and review commands they are having trouble with. Encourage students to attend office hours if they need additional review.

Then, tell students the following:

* The process completed in this activity will be the primary way of submitting homework assignments to GitHub. (No more manual uploads!)

* If it takes some time to figure out, that's okay. By the end of the course, everyone will be git ninjas!

Encourage students to continue adding and committing to GitHub for extra practice.

---

### 9. Instructor Do: Markdown (10 min)

In this part of the lesson, students will be introduced to markdown files and their style formatting, which can be used to create visually appealing README files.

**Files:** [slideshow-placeholder]()

Open the slideshow and present students with the following questions and answers:

* What is markdown?

  **Answer:** Markdown is a lightweight markup language that contains syntax for adding formatting elements to plain text documents.

* Why use markdown?

  **Answer:** Markdown provides features for creating visually enhanced documents that are rendered on the web. It is commonly used for documents such as README files or online forum discussion posts.

* What are some common markdown features?

  * Header formatting

  * Text formatting

  * Line breaks

  * Text/code snippets

  * Block quotes

  * Links

  * Images

* Why is markdown important?

  **Answer:** Markdown allows us to create visually enhanced documents such as README files (for GitHub repos, for example), which are valuable not only to potential employers, but also to potential collaborators (colleagues or teammates). A good README file helps people understand the purpose of the repository at a glance, and it shows developers how to navigate, install, and run a project.

Next, demo the following while explaining each step:

* Go to your local git repository and modify the README file. Notice that there is a `#` in front of the README title; this is why the font appears larger in the GitHub webpage. In markdown, the `#` sign represents a level 1 heading, `##` represents a level 2 heading, and so on.  

  ![markdown-header](Images/markdown-header.png)

  ![markdown-header-results](Images/markdown-header-results.png)

* Use the `*` syntax to put the repository name in italics, and use `**` syntax to put the repository description in bold. Alternatively, the `*` syntax can represent a bullet point if used at the beginning of a new line.

  ![markdown-text](Images/markdown-text.png)

  ![markdwon-text-results](Images/markdown-text-results.png)

* Use the `---` syntax to put a line break below the repository name. Line breaks help to separate areas of the document.

  ![markdown-line-break](Images/markdown-line-break.png)

  ![markdown-line-break-results](Images/markdown-line-break-results.png)

* Use the backtick (`\`) syntax to wrap text as snippets or code. Wrapping text as snippet or code blocks adds emphasis to a specific item or piece of code.

  ![markdown-text-code-snippet](Images/markdown-text-code-snippet.png)

  ![markdown-text-code-snippet-results](Images/markdown-text-code-snippet-results.png)

* Use the `>` syntax to create a block quote with the following text: `"...to boldly go where no one has gone before".` Block quote formatting can be used when there is a large text excerpt or quote.

  ![markdown-blockquotes](Images/markdown-blockquotes.png)

  ![markdown-blockquotes-results](Images/markdown-blockquotes-results.png)

* Use the `[]()` syntax to create a directory for each folder in the repository. Links are useful in directing a reader to different webpages.

  ![markdown-links](Images/markdown-links.png)

  ![markdown-links-result](Images/markdown-links-result.png)

* Use the `![]()` syntax to add an image. Images help to visually enhance a markdown document.

  ![markdown-image-link](Images/markdown-image-link.png)

  ![markdown-image-link-results](Images/markdown-image-link-results.png)

* Notice how the newly formatted markdown file appears in comparison to the original.

Ask students if they have any questions before moving on.

---

### 10. Student Do: Git Welcome (15 min)

In this activity, students will visually enhance their README files for their GitHub repositories by adding additional markdown features.

**Instructions:** [README.md](Activities/03-Stu_Markdown/README.md)

### 11. Instructor Do: Review Git Welcome (5 min)

Take some time to review the previous activity with students, highlighting the following points:

* A well-formatted README file showcases the contents of a GitHub repository. Markdown syntax provides additional features for text formatting, links, images, and code snippets, among other things.

* Markdown is a common README format and renders on a webpage via specific syntax.

* Using markdown syntax is as easy as using the correct syntactical keyword or term. For example, the `![]()` syntax is used specifically for linking images to the markdown file.

Encourage students to continue building their GitHub README files as they progress through the course, particularly when they begin generating coding assets. The goal is to have professional-looking README files for their GitHub repo by the end of this course.

---

### 12. BREAK (40 min)

---

### 13. Instructor Do: Introduce Case Studies (5 min)

In this part of the lesson, you will prepare students to work in pairs to create a FinTech case study in a shared GitHub repo. This activity will combine students' knowledge of the git CLI and markdown syntax.

**Files:** [slideshow-placeholder]()

Open the slideshow and go through the slides while explaining the following:

* Now that students know how to manage their own GitHub repositories and create text-formatted markdown files, they can move on to creating shared repositories in which multiple people collaborate to create a case study report.

* Git repositories are often shared and have multiple collaborators; therefore, this activity will give students practice in this kind of scenario.

Next, provide an overview of the activity.

* In the class GitHub repository, there will be a list of potential FinTech case studies that they can choose from.

* Students should pair off and choose one of the FinTech companies on the list to present.

* Students will have 30 minutes to develop their case studies, and 2 to 3 minutes to present their reports.

Get students excited for this work. This activity is a great opportunity for students to interact and build on what they've learned to independently produce an analysis.

In this activity, students will be instructed on how to create a FinTech case study -- a compilation of holistic research performed on a FinTech company or technology. This activity is particularly important as it will serve as the knowledge foundation for students completing their FinTech case studies for the unit `1` homework.

**File:** [slideshow-placeholder]()

Open the slideshow and walk through the following:

* `Background`

  * This case study researches the online financial advisory or "robo-advisory" company known as Betterment. Betterment is an examplar robo-advisory company that provides optimized and self-managed portfolios that customers can invest in based on their varying risk tolerances. In addition, Betterment provides financial advice based on specific customer goals and timelines, and offloads the work of things like portfolio re-balancing, dividend re-investments, auto-depositing, and much more.

* `Use Case`
  
  * Traditionally, investment management services would first gauge a customer's investment risk level (conservative, neutral, aggressive) based on factors such as overall risk tolerance, financial goals, and duration of investment, and then proceed to manage a portfolio specifically tailored to that customer for a nominal overhead/maintenance fee. However, as overall technology advanced (as did machine learning/algorithmic trading), automated investment management services started becoming increasingly prevalent -- allowing investment management services to become more data-driven (and therefore intelligent) as well as cheaper due to automation.

* `Advantages`

  * Betterment provides a relatively cheap and easy-to-use service that makes investing simple, intuitive, and intelligent; Customers are given the benefits of investing in computer-optimized and self-managed portfolios based on their specific investment needs (risk tolerance, financial goals, and duration of investment) all the while paying a cheaper overhead/maintenance fee due to the efficiencies of automation. In addition, Betterment has additional features such as monthly auto-deposits to make saving even easier for its customers.

* `Competitors`

  * Similar companies such as WealthFront, Acorns, Stash, and many others have developed similar solutions.

Advise students that they should generally seek to answer the following questions for their case studies:

* `Company Sector`

  * Which financial industry it is in?

  * What are the trends and competitors in this industry?

* `Company Business Activities`

  * What **problem** does this company solve?

  * Who is their intended customer?

  * What solution does this company offer that their competitor does not or cannot? (What is the advantage they utilize?)

  * Which technologies are they currently using and how are they implementing them?

  * What are they doing right? What could be improved?

* `Recommendations:`

  * What products or services would you suggest they add to their catalog? Why do you think it would benefit them?

  * What technologies would your proposed ideas incorporate? Why are those technologies appropriate for your solution?

---

### 14. Student Do: FinTech Case Study (30 min)

In this activity, students will work in pairs to create a case study report on a particular FinTech company, which will be chosen from a list. Each team will create their a shared GitHub repository and write their report in markdown.

**Instructions:** [README.md](Activities/04-Stu_Group_Case_Study/README.md)

### 15. Instructor Do: Review FinTech Case Study (20 min)

Students will now present their findings to the class.

Explain that each team should take 2 to 3 minutes to share their reports. They should log into their shared GitHub repo and use the markdown file they created to guide their presentation.

**Note:** Make sure that all students participate in the presentation and are given an opportunity to speak.

After each group has presented, check the pulse of the class. Ask students if they have any questions and if they found the activity to be enjoyable.

Finally, remind students that the Unit 1 homework assignment is a FinTech case study. Students can leverage the content created in this activity to complete the homework requirements.

### 16. Instructor Do: Career Services (35 min)

Take time to go over any questions related to career services, as well as students' professional goals.

### End Class

---

© 2019 Trilogy Education Services
