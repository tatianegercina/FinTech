# GitHub Practice 

In this activity, you will create new project in GitHub and practice common git commands. Git is a great resource for managing your code and is very convenient if you want to change computers. You'll become very familiar with git and GitHub over the course of this class.

Follow these steps: 

1. Navigate to GitHub and create a new respository by clicking on the Respositories tab, and selecting New.

![Making a new repository](images/01.PNG)

2. Create a new project named `git-practice`. Add a short description to the project, like "practicing with git." Then, initialize the repository with a README and create the repository.

![Creating a new respository](images/02.PNG)

3. Clone the repository you just made. Click the "Clone or download" button and then copy the link to your clipboard.

![Copying the clone url](images/03.PNG)

4. Navigate to the directory where you want to save your coding drills (e.g., desktop, root directory, Documents folder). 

5. Open the command line in this folder. Make a local copy of the repository you just created by running the `git clone ` command with the link you copied.

![Cloning down a repository](images/04.PNG)

6. Use `git status` to check the current status of your repository. This should say you're completely up to date.

![Checking the git status](images/05.PNG)

7. Create a new file called `test.md` and then check your `git status` again. Notice that git is now telling you that you have an untracked file.

![Adding a new file](images/06.PNG) 

8. Use `git add` to add the contents of the current folder to be tracked by git. The period by itself references the current directory. Now git is waiting for those files to be committed.

![Tracking a new file](images/07.PNG)

9. Use `git commit -m "add test file"` to commit the changes you've made to the repository, along with a commit message. This creates a new commit with the "add test file" commit message.

![Committing a new file](images/08.PNG)

10. Use the `git push origin master` command to push the changes up to GitHub to sync your machine with GitHub. 

![Pushing up to GitHub](images/09.PNG)

11. If you made changes to your repository on another computer, you can pull down the changes you committed with the `git pull origin master` command. Since you haven't made any changes yet, git will tell you that you're up to date.

![Pulling down from Github](images/10.PNG)

12. If you want to work on your project from another computer or from a different location, you can clone the repository from GitHub like you did in Step 3.

![Cloning to another computer or location](images/11.PNG)

13. From the new location, you can make changes to the project and push those changes up to GitHub.

![Making changes in another location](images/12.PNG)

14. Go back to your first directory and pull down the changes you made elsewhere. Navigate back to the directory you cloned in Step 3 and run `git pull origin master`.

![Pulling down changes from GitHub](images/13.PNG)

 - - - 

 © 2019 Trilogy Education Services


