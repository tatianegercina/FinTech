# GitHub Reorganized

In this activity, you will clone your GitHub repo, create a folder structure, and then push those changes to the `master` branch.

## Instructions

Complete the following steps.

1. Navigate to the GitHub website.  Click on the "Clone or download" button, and then copy the repo link.

2. Open the command line and run the command `git clone <repository link>` to clone the repository to your local file system.

3. Create the following folders in the local repo: `code`, `data`, `references`, and `images`.

4. Create a `.gitkeep` file within each subfolder so that git knows to retain the empty folder. (Remember, empty folders are not added to git repos by default.)

5. Run the `git add .` command to add all changed files to the tracked files queue.

6. Run the `git commit -m "message"` command to group tracked/changed files as a checkpoint prior to uploading to the remote git repo.

7. Execute `git push` to push the commit to the remote git repo.

8. Navigate to the GitHub website and confirm that the changes have been made.

## Hint

GitLab has a pretty good tutorial on how to use the git CLI. Check it out [here](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html).

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
