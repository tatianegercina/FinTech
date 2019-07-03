## 8.1 Lesson Plan - Projects & Collaboration with Git

### Overview

Today's lesson plan introduces students to the requirements for Project 1, as well as the basics of collaboration with Git.

### Instructor Priorities

* Students will be able to articulate the requirements for Project 1.
* Students will be able to draw and interpret diagrams of Git branching workflows.
* Students will be able to create new branches with Git.
* Students will be able to push local branches to GitHub.

#### Instructor Notes

It is highly recommended to request project proposals from students and then approve their proposals. Students will often struggle with finding data sources and in setting realistic goals, so use this as an opportunity to guide them to unique, interesting, and achievable projects.

Install the appropriate text editor plugin to help visualize Git histories: [Git History](https://github.com/DonJayamanne/gitHistoryVSCode) in VS Code, [Git Time Machine](https://github.com/pidu/git-timemachine) for Sublime Text, and [git-time-machine](https://atom.io/packages/git-time-machine) for Atom.

Be sure to refer to the [TimeTracker](TimeTracker.xlsx) to remain on time.

Be sure to slack out the [Git Branching Workflow](http://nvie.com/posts/a-successful-git-branching-model/) before the end of class.

Be sure to slack out the [Visual Introduction to Git](https://medium.com/@ashk3l/a-visual-introduction-to-git-9fdca5d3b43a).

* If possible, share the above links both _before_ today's class, and again at the end of it.

Lastly, as a reminder these slideshows are for instructor use only - when distributing slides to students, please first export the slides to a PDF file. You may then distribute the PDF file through Slack.

- - -

### Class Objectives

* Students must be able to articulate the requirements for Project 1.
* Students must be able to draw and interpret diagrams of Git branching workflows.
* Students must be able to create new branches with Git.
* Students must be able to push local branches to GitHub.

- - -

### 1. Instructor Do: Welcome Students (5 min)

Greet the class, and explain that today is the first day of Project one!

Congratulate the class on having made it this far!

Explain that, over the next two class weeks, students will work in groups to complete a FinTech Python Project.

Point out that this provides students an opportunity to practice both programming and collaborative workflows.

Explain that the first half of today's class will focus on using Git for collaboration, and that students will have the second half to convene with their groups and start thinking about projects.

Break students into their project groups, and give them a few minutes to rearrange their seating before moving on.

### 2. Groups Do: Create a Repository (10 min)

In this activity, each project group will create a project repo and invite all group member as collaborators.

Refer to `08-project-1/01-Stu_Create-Repository`, which contains the following instructions:

**Instructions**

```
* Once group member should create a new Github repository. Don't worry about the project name now, this can be changed later.

* From the repo's main page, click the "Settings" tab.

* Once in the repo's settings, select the "Collaborators" menu item on the left.

* From the "Collaborators" page invite your group members to be project collaborators by entering their Github usernames one at a time.

* Each invited group member should receive an email they must open to accept the invitation.

* **Hints**:

* Ask an instructor or TA if you get stuck!
```

### 3. Instructor Do: Pull Requests and Code Review (5 min)

Explain that when working with others on the same repo, it's important to make sure that all of the new code gets reviewed by at least one other team member before getting merged into the master branch.

Assure the class that we'll go into further detail about how this is done, but ask the class: "Why would we want to get code reviewed before merging it into master?"

> Reviewing new code decreases the chances that a breaking change will accidentally be introduced into the master branch.

> Code review helps group members who didn't write the code understand how it works.

Explain that the next step of setting up our project repos for group collaboration is to protect the master branch.

* Protecting the master branch means we will configure the repo to prohibit any team members from pushing code up into master directly or merging it in without another team member's review.

### 4. Groups Do: Protect Master Branch (5 min)

In this activity groups will protect their master branches.

Refer to `08-project-1/02-Stu_Protect-Master`, which contains the following instructions:

**Instructions**

```
* Only one member per project group needs to complete this activity.

* Navigate back to the repo's "Settings" page and then select "Branches" from the left sidebar.

* Under "Branch Protection Rules" select "master" from the dropdown.

* You should be presented with some options, check off the following:

  * "Protect this branch"

  * "Require pull request reviews before merging"

  * "Include administrators"

* If completed successfully, no one should be able to push directly to the master branch. Instead, all changes must be made in the form of pull requests that are to be reviewed by another group member.

* **Hints**:

* Ask an instructor or TA for assistance if you get stuck!
```

### 5. Instructor Do: Branching (10 min)

Note: For now we just want to give students a high level conceptual understanding of branching.

Explain the following points about branching:

* Every Git repo starts off with a master branch. This is there to hold the production version of the repo's code. But when we want to work on the code, we start by creating a new feature branch off of master.

* If we create a new branch from master, it essentially creates a self-contained copy of all of the master branch's code for us to work in.

* When we're satisfied with our work in the new feature branch, we submit a pull request from the feature branch to the master branch.

* A pull request is a request to merge the diffs or changes from the source branch (the feature branch) to the target branch (master).

* With the way our repos are set up now, another group member must look at and approve the pull request before its changes can be merged into master.

* Once a feature branch has been merged into master, we delete it and then check back out to the master branch. From there, we'd check back out to a new feature branch and repeat the process for each feature we add.

Slack out the following image for students to have as a visual aid:

  ![Git Branching](Images/01-Git-Branching.png)

Take a moment to answer any questions, but avoid going too in depth. Students will utilize branches in the next activity.

### 6. Student Do: Git Branching/Pushing (15 mins)

In this activity students will create branches, submit pull requests, and perform code reviews before merging.

Instructional staff should be walking around the class making themselves available for assistance and making sure students understand the instructions.

Refer to [03-Stu_Branching-Pushing](Activities/03-Stu_Branching-Pushing/README.md), which contains the following instructions:

**Instructions**
```
**Part I**: Branching and Submitting a Pull Request

* In this section we will create a branch, add a feature, and submit a pull request. **Only one group member should complete this section, everyone else should observe.**

* Clone the project repo onto your computer and cd into it.

* Run the following command in your terminal to create and checkout to a new branch:

  `git checkout -b add-new-python-script`

* You should now be on a new branch named "add-new-python-script". In order to verify this worked, run the following command in your terminal:

  `git branch`

* You should see two branches listed: `master` and `add-new-python-script`. The `add-new-python-script` branch should have an asterisk to the left of it. This indicates that this is the branch you're currently on.

* At the root of the repo, create a new file named `data_collection.py`. Inside this file, add code to import the `requests` library and save.

* In your terminal, add and commit the changes. Then push up your code by running following in your terminal:

  `git push origin add-new-python-script`

* This should push up your code to to GitHub on a branch with the same name (`add-new-python-script`).

* Go to the main repo page at github.com and you should see an button that says "Compare & pull request" -- click this.

* On the next screen, add a description of the work that was done in the textarea and click the "Pull Request" button.

* If completed successfully, you should see the pull request listed under the repo's "Pull request" tab.
```

- - -

```
**Part II**: Reviewing a Pull Request

* In this section we will review the pull request from Part I and merge it into master. **A different project member should complete this section while others observe**.

* Clone the repo to your computer if you haven't already done so and cd into it.

* First you will want to test the changes introduced by the `add-new-python-script` branch locally. In order to examine the new branch on your local machine, run the following commands in your terminal:

  `git fetch`

  `git checkout -b add-new-python-script origin/add-new-python-script`

* This code should bring the copy of the `add-new-python-script` branch that's on GitHub onto your computer.

  * Make sure this worked by verifying that there's an `data_collection.py` file in your local repo.

  * Normally you'd run the code here to make sure everything works properly.

* Check back out to your local `master` branch by running the following in your terminal:

  `git checkout master`

* Now go to your GitHub repo's main page and go to the "Pull request" section. Select the `add-new-python-script` pull request from the list.

* At the next page select the option to see the "Files changed".

* You should be presented with all of the files that were changed in this PR along with line numbers for any code added/removed.

* If there are any changes you would like made, you can click the line number to leave a comment the PR author will see and should address before approval. Otherwise click "Review changes" and approve the PR. You should be taken to a screen with an option to "Merge pull request" -- click this button.

* Once complete you can delete the feature branch from your machine by running the following in your terminal:

  `git branch -D add-new-python-script`

* **Hints**:

* Ask an instructor or TA if you get stuck or have any questions!
```

### 7. Instructor Do: Introduce Projects (0:10)

Point out that students will need a project to work on if they're to be able to practice Git!

Step through the [slideshow](), and explain the requirements for Project 1.

* Be sure to slack out the Project's [Technical Requirements](ProjectGuidelines/TechnicalRequirements.md); the [Presentation Requirements](ProjectGuidelines/PresentationRequirements.md); and the [Projects Overview](ProjectGuidelines/README.md) after going through the slides.

Take a moment to address any remaining student questions before dismissing the class for break.

- - -

### 8. BREAK (15 min)

- - -

### 9. Everyone Do: Project Work (1:45)

Students should spend the remainder of class working with their groups to develop a project proposal.

Be sure to walk around and offer advice on project scope; finding data sources; and what kinds of questions would be interesting, and realistic, for students to investigate.

- - -

### End Class

- - -

© 2019 Trilogy Education Services
