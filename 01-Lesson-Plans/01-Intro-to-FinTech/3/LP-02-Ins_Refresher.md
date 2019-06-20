### 2. Instructor Do: Refresher (10 mins)

This activity gives students a quick re-cap on how to create and download a git repository (from the web app), use the terminal to navigate and create a new text file in the local repository folder, and upload the file back to the git repository (from the web app). This activity serves as a pre-cursor to the later git CLI activities as it showcases the limitations of merely downloading a repository as a local folder rather than performing a git clone in which git can track and compare changes.

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