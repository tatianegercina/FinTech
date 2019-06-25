PLACEHOLDER

## 1.3 Lesson Plan - FinTech Collaboration

---

### Overview

In today's class, students will learn how to utilize the Git Command Line Interface (CLI) and create markdown files to generate FinTech case studies that can be collaboratively stored, accessed/modified, and previewed on an online git or file repository such as Github. A solid understanding of the git CLI as well as knowing how to create markdown files will serve students in helping them properly manage git repositories and construct visually enhanced README description files. 

### Class Objectives

By the end of class, students will be able to:

* Configure the git CLI user credentials from the terminal
* Comprehend the notion of git clone and local/remote branches
* Modify git repositories by adding, committing, and pushing files
* Create markdown files and implement its additional visual capabilities: text formatting, images, links
* Collaboratively write a FinTech case study in markdown, hosted on an online git repository 

### Instructor Notes

* Students may feel uneasy as today's lesson will continue their journey of using the terminal to interact with not just files on their local file system, but also files that are actively tracked via an online repository. Ease students' nerves by telling them that git is merely a command line tool -- a program that exists on the local file system that executes from the command line/terminal.

* Make sure that by the end of class students have the tools to create well-presented markdown README files to host on their git repositories. They'll need these to showcase their git repositories (and the coding assets within) to potential employers in the future.

* Students will need to have a good understanding of git branches and merges in order to effectively collaborate with others working in the same git repository. Otherwise, students may face merge conflicts that prevent them from pushing their file changes to the git repository.

* Be mindful of students working in groups during the case study activity; some students may be less vocal than others. Walk around the room with the other TAs and try to make sure every student is actively engaged and has a voice in their respective groups.

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

---

### 1. Instructor Do: Welcome Class (5 mins)

**Files:**

* [Slideshow](placeholder)

Welcome students to the third day of FinTech! Cover the following points:

* The previous lessons focused on introducing students to the FinTech course structure and discussed the history and current landscape of the FinTech ecosystem, as well as notable case studies of technological disruptors. Today students will combine what they've learned so far on the FinTech industry to collaboratively create their own FinTech case studies that can be hosted on online git repositories and previewed as visually enhanced markdown files.

* Mention to the class that today's goal is two-fold: one, to teach students how to manage their own git repositories as well as develop in shared ones, and two, to develop text-based assets (such as a FinTech case study) in markdown to provide visually appealing README files that can be previewed on the GitHub website (and showcased to potential employers). 

* Students will be put into groups and given a selection of FinTech case study proposals to choose from. Therefore, students will need to work collaboratively and generate a visually appealing document that can be hosted online -- that's where git CLI and markdown comes in! 

* Energize your students! Today they'll be learning the same collaborative tools (git) that real developers and industry professionals use to share and build upon code.

---

### 2. Instructor Do: Refresher (10 mins)

This activity gives students a quick re-cap on how to create and download a git repository (from the web app), use the terminal to navigate and edit a text file in the local repository folder, and upload the file back to the git repository (from the web app). This activity serves as a pre-cursor to the later git CLI activities as it showcases the limitations of merely downloading a repository as a local folder rather than performing a git clone in which git can track and compare changes.

First, quickly present the following questions and answers:

* What is git?

  **Answer:** Git is a version-control system for tracking changes in files -- often from a coding and software development standpoint. Git is designed for coordinating work among programmers, but it can be used to track changes in any set of files.

* What is a git repository?

  **Answer:** A git repository is a remote or online file repository in which git tracks files and conducts version control as changes are made.

* What is a terminal/command prompt?

  **Answer:** A terminal/command prompt is a command line interpreter application in which users can execute commands to perform specific file system operations or run other existing programs residing on the file system.

* What is GitHub?

  **Answer:** GitHub is a web-based file hosting service that is one of the many vendors that use Git for file version control.

Then, perform a live demo while highlighting the following:

* Git repositories can be created via the GitHub website. The option `Initialize this repository with a README` should be checked off to automatically deploy the repository once created.

  ![github-website](Images/github-website.png)

  ![github-create-repository](Images/github-create-repository.png)

* A git repository can then be downloaded locally as a compressed .zip file from the GitHub website.

  ![github-download](Images/github-download.png)

* After unzipping or de-compressing the .zip file, the extracted git repository folder can be accessed through the terminal by performing a `cd` command to change directory inside the folder. The `ls` command with the `-l` parameter displays its contents in list format.

  ![terminal-git-repository](Images/terminal-git-repository.png)

* The `vi` command is a utility for editing text files directly from the command line. Once in the editor, press `I` to insert text and then press the sequence `ESC`, `:wq!`, `ENTER` to save the file when finished. Conversely, the sequence `ESC`, `:q!`, `ENTER` would quit the file without saving.

  ![terminal-vi](Images/terminal-vi.png)

  ![terminal-vi-editor](Images/terminal-vi-editor.png)

* Here, the file `README.md` is edited and saved within the local git repository; however, changes are still local and will need to be pushed to the remote repository.

  ![git-local-change](Images/git-local-change.png)

* Files can be committed and changed on the git repository via the GitHub website.

  ![github-upload-files](Images/github-upload-files.png)

  ![github-remote-change](Images/github-remote-change.png)

* The `README.md` preview via the Github website confirms the change.

  ![github-remote-change-confirmation](Images/github-remote-change-confirmation.png)

  ---

### 3. Students Do: GitHub README (15 mins)

In this activity, students will emulate the preceding instructor activity by creating their own git repositories and modifying their README.md files to personalize their GitHub repositories.

**Instructions:**

* [README.md](Activities/01-Stu_Refresher/README.md)

### 4. Instructor Do: GitHub README (5 mins)

Highlight the following points when it comes to setting up a git repository and modifying the README:

* Make sure to intialize the new GitHub repository with a `README.md` file. Otherwise, deployment of the repository will be halted until further setup is completed.

  ![github-create-repo-uninitialized](Images/github-create-repo-uninitialized.png)

* When downloading the GitHub repository as a `.zip` file, contents will have to first be extracted in order to edit any of the files.

  ![github-repo-unzipped](Images/github-repo-unzipped.png)

* Navigating through the terminal and performing edits via the command-line may seem unfamiliar and inefficient at first; however, most veteran developers will agree that familiarity with the terminal is critical as it demonstrates a developer's understanding of low-level functions and provides an interactive shell when no graphical user interface (GUI) exists. For example, when connecting remotely to another machine via the SSH or Secure Shell Protocol.

  ![terminal-familiarity](Images/terminal-familiarity.png)

* After modifying the `README.md` file on the local file system, changed files will have to be pushed or re-uploaded to the online repository.

  ![github-file-upload-update](Images/github-file-upload-update.png)

* GitHub should automatically be able to preview `.md` or *markdown* files, as they contain style formatting elements, and therefore should immediately reflect the changes of the updated `README.md` file. If not, manually refresh the page.

  ![github-readme-update](Images/github-readme-update.png)

---

### 5. Instructor Do: Git CLI (10 min)

In this activity, students will be introduced to the git CLI, which will allow them to more efficiently track changes to a git repository by providing additional git operations.  

**Files:**

* [Slideshow](Resources/Intro_to_Git.pptx)

Open the slideshow and go over slides 1-22. Highlight the following about git:

* How does the GitHub web app and Git CLI differ?

  > The GitHub web app provides a convenient user interface for performing common git operations. The Git CLI, however, is a command line utility that provides all git operations and is generally more robust than a git-based graphical user interface (GUI). This is because more often then not, a GUI interacts with the underlying CLI to perform its functionality (ex. click a button that executes a command in the backend) and therefore is often a simplified version of the underlying functionality.

* What other features does the Git CLI provide?

  > The Git CLI can perform many different kinds of git operations; however, popular commands are:

    * `git clone`: Clones a git repository onto the local file system.

    * `git add`: Adds changed files to the queue of tracked files ready to be committed.

    * `git commit`: Adds tracked files as a bulk checkpoint ready to be pushed to the remote git repository.

    * `git push`: Uploads changed files from the local git repository to the remote git repository and updates the remote files.

    * `git pull`: Downloads changed files from the remote git repository to the local git repository and updates the local files.

    * `git branch`: Lists the available branches of the git repository.

    * `git checkout`: Checks out a specific git branch and updates the files in the local git repository to match the contents of the git branch.

    * `git merge`: Merges two branches together, consolidating any changes amongst the two.

* What is a git commit?

  > Before changed files are pushed from a local git repository to the remote git repository, a git commit saves a queue of tracked changed files as a **save** or **checkpoint** for a git repository. This way, should it be necessary, a git repository can be restored to a previous checkpoint in time, thereby undoing any existing changes from that point.

* What is a git branch?

  > A git branch is a derived version of another branch (often `master`). In other words, a branch is just a copy of another branch.

* What is Git's "Snapshot model":

  > Git thinks of its data more like a set of snapshots of a miniature filesystem. Every time you commit, or save the state of your project in Git, it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a stream of snapshots."

  ![Git Snapshot Model](https://git-scm.com/book/en/v2/images/snapshots.png)

---

### 6. Instructor Do: Git CLI (10 min)

In this activity, students will revisit their newly created GitHub repositories to add folder structures and make a `backup` branch of their `master` branch.  

Live demo the following walkthrough:

* Re-visit the GitHub website and click on the "Clone or Download" button. This time, copy the URL as it represents the GitHub repository link (which will be used for the `git clone` command).

  ![github-url](Images/github-url.png)

* Run a `git clone <repository link>` in the terminal to clone the repo to the current directory. Copying a repository via the `git clone` command differs from just downloading a `.zip` file of the repository as the `git clone` command downloads a tracked git repository onto the local filesystem while the `.zip` file merely download the contents without any kind of tracking or version control involved.

  ![git-clone](Images/git-clone.png)

* Create three folders in the local git repository via the `mkdir` command: `Homework`, `CourseWork` and `Projects`. Add a `.gitkeep` file to each folder so that git knows to retain the folders as it refrains from keeping empty folders unless explicitly told.

  ![git-repository-mkdir](Images/git-repository-mkdir.png)

  ![git-repository-gitkeep](Images/git-repository-gitkeep.png)

* Once the folders and files have been created, open up the terminal/git-bash and navigate to the root of the git repo folder. Run the following lines to push the changes to the remote git repository and explain each as you go through them.

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

* Navigate to the repo on [Github.com](https://github.com/) to see that the changes have been pushed up.

  ![git-push-results](Images/git-push-results.png)

* Once the changes have been pushed up, open up the terminal/git-bash again and navigate to the root of the git repo folder. Run the following lines to create a new branch with a modified `README` and explain each as you go through them.

  ```bash
  # Make sure the current branch is `master`
  git checkout master

  # Create a branch `backup` from the current branch `master`
  git checkout -b backup

  # Verify that the `backup` branch was created
  git branch

  # Add a quick note in the README file "This is a backup branch."
  vi README.md

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

* Navigate to the repo on [Github.com](https://github.com/) and see that the new branch and `README` changes have been pushed up.

  ![git-branch-results](Images/git-branch-results.png)

Make sure every student was able to successfully clone a repo, add files to the repo, commit the changes, and then push the changes to Github all from the command line.

---

### 7. Students Do: GitHub Re-Organized (15 min)

In this activity, students use the Git CLI to clone their git repositories to their local file systems and add directories to their GitHub repositories. 

**Instructions:**

* [README.md](Activities/02-Stu_Git_CLI/README.md)

### 8. Instructor Do: Review GitHub Re-Organized (10 min)

* Ask students for any questions they may have and take a few minutes to review any commands which weren't clear. Offer to help students with this throughout the day and during office hours.

* Explain to students that this will be the new, primary way of submitting homework to GitHub (no more manual uploads!).

* Reassure them that it's ok if this takes some time to figure out. By the end of the course, they will be git ninjas!

* Encourage students to continue to add and commit their activities today into a repo for additional practice.

---

### 8. Instructor Do: Markdown (10 mins)

In this activity, students are introduced to markdown files and their style formatting, which can be used to create visually appealing README files. 

**Files:** [slideshow-placeholder]()

Open the slideshow and present the following questions and answers:

* What is Markdown?

  > Markdown is a lightweight markup language that contains syntax for adding formatting elements to plain text documents.

* Why use Markdown?

  > Markdown provides features for created visually enhanced documents that are rendered on the web, most commonly used for documents such as README files or online forum discussion posts. 

* What are some common Markdown features?

  * Header Formatting

  * Text Formatting

  * Line Breaks

  * Text/Code snippets

  * Block quotes

  * Links

  * Images

Then, live demo the following while explaining the following points:

* Go to your local git repository and modify the `README` file. Notice there was already a `#` in front of the `README` title! That's why the font looked larger in the GitHub webpage. Markdown can create text headers with `#`, `##`, `###...`, where `#` represents size header 1 and `###...` repesents size header 3 and so on. 

  ![markdown-header](Images/markdown-header.png)

  ![markdown-header-results](Images/markdown-header-results.png)

* Use the `*` and `**` syntax to put the repository name in **italics** and the repository description in *bold*. Alternatively, the `*` syntax can represent a bullet point if used at the beginning of a new line.

  ![markdown-text](Images/markdown-text.png)

  ![markdwon-text-results](Images/markdown-text-results.png)

* Use the `---` syntax to put a line break underneath the repository name. A line break is a good idea when trying to separate areas of the document.

  ![markdown-line-break](Images/markdown-line-break.png)

  ![markdown-line-break-results](Images/markdown-line-break-results.png)

* Use the \` backtick syntax to wrap text as snippets or (code) if applied. Wrapping text as snippet or blocks can add emphasis to a specific item or code.

  ![markdown-text-code-snippet](Images/markdown-text-code-snippet.png)

  ![markdown-text-code-snippet-results](Images/markdown-text-code-snippet-results.png)

* Use the `>` syntax to create a block quote with the following text `"...to boldly go where no one has gone before".` Block quote formatting can be used when there is a large text excerpt or quote.

  ![markdown-blockquotes](Images/markdown-blockquotes.png)

  ![markdown-blockquotes-results](Images/markdown-blockquotes-results.png)

* Use the `[]()` syntax to create a directory for each folder in the repository. Links are useful in directing a reader to different webpages.

  ![markdown-links](Images/markdown-links.png)

  ![markdown-links-result](Images/markdown-links-result.png)

* Use the `![]()` syntax to add an image. Images are useful in providing pictures and visuals to the markdown document.

  ![markdown-image-link](Images/markdown-image-link.png)

  ![markdown-image-link-results](Images/markdown-image-link-results.png)

* As can be seen, the original markdown compared to the style formatted markdown looks as different as day and night! 

Ask your students if they have any further questions before moving on.

---

### 10. Students Do: Git Welcome (15 mins)

In this activity, students visually enhance their `README` files for their GitHub repositories by adding additional markdown features.

**Instructions:**

* [README.md](Activities/03-Stu_Markdown/README.md)

### 11. Instructor Do: Git Welcome (5 mins)

Perform the following:

* Explain to the students that having a well formatted `README` file helps to better showcase the contents of a GitHub repository; markdown syntax provides additional features for text formatting, links, images, and code snippets among other things. 

* Remind students that markdown is a common `README` format and renders on a webpage via specific syntax.

* Reassure students that using markdown syntax is as easy as using the correct syntactical key word or term. For example, the `![]()` syntax is used specifically for linking images to the markdown file. 

* Encourage students to continue building their GitHub `README` files as they progress through the course, particularly when they begin generating coding assets. Ideally, their GitHub repository `README` should look like that of a professional's by the end of this course.

---

### 12. BREAK (40 mins)

---

### 13. Instructor Do: Group Case Study (5 min)

In this activity, students will combine their knowledge of the git CLI and markdown syntax to collaboratively create a group FinTech case study on a shared GitHub repository. 

**Files:** [slideshow-placeholder]()

Open the slideshow and go over slides 1-22 while explaining the following:

* Now that students know how to manage their own GitHub repositories and create text formatted markdown files, they can move on to creating shared repositories in which multiple people collaborate to create a group case study report.

* Git repositories are often shared and have multiple collaborators; the group case study mini-project will showcase this scenario.

* Remind students that in the class GitHub repository, there will be a list of potential FinTech case studies from which they can choose. 

* Students should pair off into `4-5` groups and choose one of the available FinTech companies to present. Students will be given `30` minutes to develop their case studies and will then have `5` minutes to present their reports.

* Energize your students! This will be a good time for students to interact with each other and build upon what they've learned to perform their own independent case study analyses (without teacher help).

---

### 14. Students Do: FinTech Groups (30 mins)

In this activity, students will be divided up into groups of `4-5` individuals with each group representing a FinTech case study of a particular company. Each group will have to create their own shared GitHub repository and collaboratively create a case study report written in markdown.

**Instructions:**

* [README.md](Activities/04-Stu_Group_Case_Study/README.md)

### 15. Instructor Do: Review FinTech Groups (20 mins)

Perform the following:

* Explain to students that now that they've worked together to create their FinTech case studies, they should finish off with a presentation of their findings. Have each group present their findings to the class and give each group approximately `4-5` minutes per presentation.

* Have students log into their shared GitHub repository and present off of the FinTech case study content written in the `README` markdown file.

* Make sure that all students have a say in the group presentations. Most likely, there will be some students who are shy when it comes to presenting -- try to bring them out of their comfort zones?

* When presentations are finished, check the pulse of the class. Ask the students if they have any questions regarding the FinTech case studies and if they enjoyed their group activity.

* Lastly, remind students that the homework for Unit 1 will be a FinTech case study. Therefore, students can leverage what they already have as a group to complete the more comprehensive requirements of the Unit 1 homework.

### 16. Instructor Do: Career Services (35 mins)

Take the time to go over any career services related questions and talk about students and their future goals.

### End Class

---

Trilogy Education Services © 2019. All Rights Reserved.