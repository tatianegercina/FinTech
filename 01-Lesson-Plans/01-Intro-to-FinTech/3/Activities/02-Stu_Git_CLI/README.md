# GitHub Re-Organized

Clone your Github repo, create a folder structure, and create a `backup` branch from the `master` branch.

## Instructions

* Walk through the following steps.

  1. Navigate to the GitHub website and click on the "Clone or download" button. Copy the git repo link.

  2. Open up your terminal and clone the repository to your local file system by running the command `git clone <repository link>`.

  3. Create the following folders in the local git repo:

    * `code`

    * `data`

    * `references`

    * `images`

  4. Create a `.gitkeep` file within each sub-folder so that git knows to retain the empty folder (empty folders are not added to git repos by default)

  5. Use the `git add .` command to add all changed files to the tracked files queue.

  6. Run the `git commit -m "<message"` command to group tracked/changed files as a checkpoint prior to uploading to the remote git repo.

  7. Execute `git push` to push the commit to the remote git repo.

  8. Navigate to the GitHub website and confirm that the changes have been made.

## Hints

* GitLab has a pretty good tutorial on how to use the git CLI. Check it out [here!](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html)