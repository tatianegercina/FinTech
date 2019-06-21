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

