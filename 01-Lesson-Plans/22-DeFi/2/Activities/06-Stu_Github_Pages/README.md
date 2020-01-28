# Creating a Landing Page Website with Github Pages

In this activity, you will leverage the power of Github Pages to convert a `README.md` into a landing page for your dApp. You can use this to point to the frontend code and to explain the context of your application to users, developers, future employers, or any audience you choose!

## Instructions

* Create a fresh directory in your workspace called `cryptoright`:

  ```bash
  mkdir cryptoright
  cd cryptoright
  ```

* Move the frontend code from the previous folder you were working in that contained the `dapp.js`, `index.html`, and `CryptoRight.json` into a subfolder called `frontend`.

* Create a `README.md` inside the top-level `cryptoright` folder.

  Your directory tree should look something like:

  ![Github Pages file tree](Images/github-pages-tree.png)

  You can model the structure from the [Resources/cryporight](Resources/cryptoright/README.md) folder.

* Within this `README.md` file, add some information explaining the application.
  You **must** include a link to the dApp's `frontend` directory by linking to `frontend/index.html` at least once, otherwise, the point of the landing page is lost!

  The syntax for a link in Markdown is `[Link Text Here](https://url_here)`. You can directly link to the `frontend/index.html` file with something like

  ```markdown
  [Frontend Code Link Text](frontend/index.html)
  ```

  For example:

  ```markdown
  # CryptoRight Blockchain Copyright System

  ## Summary

  This application is a copyright management system built on the Ethereum blockchain.

  ### Demo App

  Click [here](frontend/index.html) to launch the CryptoRight application.
  ```

* Take the time to explain how the application was built. Explain things like how the contracts work, what the purpose of the application is, and how to use it.

* You can include codeblocks and even explain your raw code if you would like to present this to a future employer. Get creative!

* Use this [Markdown Syntax Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for quick reference on how to style various aspects of your text.

* Once you've got a good summary going, create a new Github repository by navigating to [Github](https://github.com), clicking the `+` at the top right, and selecting `New Repository`:

![New Github Repo](Images/github-new-repo.png)

* Give it a title and short description. Set it to public, and do not initialize with a `README`, since you have one already. Create the repository.

* Run the first set of commands that Github provides for uploading existing code to the repo, minus the first line of code that `echo`s to the `README.md` file (since there is already content in there):

![Github Upload CLI](Images/github-repo-cli.png)

* Once you run this set of commands, you will need to upload the rest of the frontend code, since this set only uploads the `README.md`:

  ```bash
  git add -A
  git commit -m "add frontend code"
  git push
  ```

  After running this, all of the code should be uploaded to the repository.

![Github Upload Complete](Images/github-upload.png)

* Navigate to the repo settings on Github by clicking the `Settings` tab, and scroll down to the `Github Pages` section, and set the `Source` to `master`:

![Github Pages Setup](Images/github-pages-setup.gif)

* Click the theme chooser, pick a theme, then navigate to the URL that Github Pages provides. You should see your website generated! **(This may take a few moments to reflect and may need a refresh.)**

* Once on the landing page, check our your beautiful work, then on the link that you generated to take you to your dApp. Ensure MetaMask is pointed at the same network that you've deployed the contract to. The dApp should request permissions to connect, and once on the same network the contract is deployed to, the contract data should populate.

![Github Pages Theme](Images/github-pages-theme.gif)

* Congratulate yourself on building your first portfolio-ready landing page!

## Challenge

* If time remains, try to deploy your contract to a live testnet like Kovan or Ropsten. You will need to update the `contract_address` variable in the `dapp.js` frontend to reflect the new contract address. If using the same deployment account, it might end up even being the same contract address, due to the deterministic nature of Ethereum.

* This landing page faces the world. Try to make this site as compelling as possible by capturing the exciting elements of your hard work!

## Hints

* In case you need some help with Markdown, use this [Markdown Syntax Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for quick reference on how to style various aspects of your text.

* Github also provides a [Markdown Reference](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax).
