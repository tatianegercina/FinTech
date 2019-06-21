### 6. Instructor Do: Git CLI (10 min)

In this activity, students will revisit their newly created GitHub repositories to add folder structures and make a `backup` branch of their `master` branch.  

Live demo the following walkthrough:

* Re-visit the GitHub website and click on the "Clone or Download" button. This time, copy the URL as it represents the GitHub repository link (which will be used for the `git clone` command).

  ![github-url](Images/github-url.png)

* Run a `git clone` of the GitHub repository using the copied link.

  ![git-clone](Images/git-clone.png)

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

