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