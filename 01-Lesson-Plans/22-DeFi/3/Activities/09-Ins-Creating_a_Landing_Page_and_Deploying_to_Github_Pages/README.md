# Creating a Landing Page and Deploying to Github Pages

In this activity, you will create a landing page and deploy the Martian Market dApp to your Github Pages account.

## Instructions

* Create a fresh directory in your workspace called `martian_market`:

  ```bash
  mkdir martian_market
  cd martian_market
  ```

* Move the frontend code from the previous folder you were working in that contained the `dapp.js`, `index.html`, and `martian_market` into a subfolder called `frontend`.

* Create a `README.md` inside the top-level `martian_market` folder.

  * You can model the structure from the [Resources/martian_market](Resources/martian_market) folder.

* Within this `README.md` file, add some information explaining the application.
  You **must** include a link to the dApp's `frontend` directory by linking to `frontend/index.html` at least once, otherwise, the point of the landing page is lost!

  The syntax for a link in Markdown is `[Link Text Here](https://url_here)`. You can directly link to the `frontend/index.html` file with something like

  ```markdown
  [Frontend Code Link Text](frontend/index.html)
  ```

  For example:

  ```markdown
  # Martian Market

  ## Summary

  This application is an online auction system for the Martian Land Foundation to auction available resources on Mars.

  ### Demo App

  Click [here](frontend/index.html) to launch the Martian Market application.
  ```

* Take the time to explain how the application was built. Explain things like how the contracts work, what the purpose of the application is, and how to use it.

* Include codeblocks and even explain your raw code if you would like to present this to a future employer. Get creative!

* Use this [Markdown Syntax Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for quick reference on how to style various aspects of your text.

* Once you've got a good summary going, create a new Github repository by navigating to [Github](https://github.com), clicking the `+` at the top right, and selecting `New Repository`:

* Give it a title and short description. Set it to public, and do not initialize with a `README`, since you have one already. Create the repository.

* Run the first set of commands that Github provides for uploading existing code to the repo, minus the first line of code that `echo`s to the `README.md` file (since there is already content in there):

* Once you run this set of commands, you will need to upload the rest of the frontend code, since this set only uploads the `README.md`:

  ```bash
  git add -A
  git commit -m "add frontend code"
  git push
  ```

  * After running this, all of the code should be uploaded to the repository.


* Navigate to the repo settings on Github by clicking the `Settings` tab, and scroll down to the `Github Pages` section, and set the `Source` to `master`:

* Click the theme chooser, pick a theme, then navigate to the URL that Github Pages provides. You should see your website generated! **(This may take a few moments to reflect and may need a refresh.)**

* Once on the landing page, check our your beautiful work, then on the link that you generated to take you to your dApp. Ensure MetaMask is pointed at the same network that you've deployed the contract to. The dApp should request permissions to connect, and once on the same network the contract is deployed to, the contract data should populate.

## Challenge

* This landing page faces the world. Try to make this site as compelling as possible by capturing the exciting elements of your hard work!

## Hints

* In case you need some help with Markdown, use this [Markdown Syntax Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for quick reference on how to style various aspects of your text.

* Github also provides a [Markdown Reference](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).
