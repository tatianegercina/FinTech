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

    * `git checkout`: Checks out a specific git branch and updates the files in the local git repository to match the contents of the git branch.

    * `git merge`: Merges two branches together, consolidating any changes amongst the two.

* What is a git commit?

  > Before changed files are pushed from a local git repository to the remote git repository, a git commit saves a queue of tracked changed files as a **save** or **checkpoint** for a git repository. This way, should it be necessary, a git repository can be restored to a previous checkpoint in time, thereby undoing any existing changes from that point.

* What is a git branch?

  > A git branch is a derived version of another branch (often `master`). In other words, a branch is just a copy of another branch.

* What is Git's "Snapshot model":

  > Git thinks of its data more like a set of snapshots of a miniature filesystem. Every time you commit, or save the state of your project in Git, it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a stream of snapshots."

  ![Git Snapshot Model](https://git-scm.com/book/en/v2/images/snapshots.png)

### 17. Instructor Do: Adding Files from the Command Line (10 min)

Tell students that so far they have only added files using the GitHub website, which works well when just dealing with one or two files. What happens when multiple files need to be quickly added?

* The command line comes to the rescue!

Have students follow along with creating a repo and adding files with Terminal/git-bash.

* Create a new repo.

* From repo page, click the green box in the top right "Clone or download", select "Use SSH" and copy the link to the clipboard.

  ![clone repo](Images/GitClone.gif)

* Open terminal (or git-bash for Windows users) and navigate to the home folder using `cd ~`.

* Type in `git clone <repository link>` in the terminal to clone the repo to the current directory. Once this has run, everyone should now see a folder with the same name as the repo.

    ![terminal clone](Images/GitClone_command.png)

* Open the folder in VS Code and create two python script files named `script01.py` and `script02.py`.

* Once the files have been created, open up Terminal/git-bash and navigate to the repo folder. Run the following lines and explain each as you go through them.

  ```bash
  # Displays that status of files in the folder
  git status

  # Adds all the files into a staging area
  git add .

  # Check that thr files were added correctly
  git status

  # Commits all the files to your repo and adds a message
  git commit -m <add commit message here>

  # Pushes the changes up to GitHub
  git push origin master
  ```

* Finally navigate to the repo on [Github.com](https://github.com/) to see that the changes have been pushed up.

Make sure every student was able to successfully clone a repo, add file to the repo, commit the changes, and then push the changes to Github all from the command line.
