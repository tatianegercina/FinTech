# Setting Up Remix and Ganache

In this activity, you will be configuring your development environment for writing and deploying smart contracts on your local development blockchain.

## Instructions

* Install Ganache following the Unit 20 Installation Guide.

* If the link is not working or your correct `operating system` is not appearing on the page. Downloads of the latest ganache releases can be found on their Github page at [Ganache releases](https://github.com/trufflesuite/ganache/releases).

![Ganache releases](Images/ganache_github_releases.png)

* Once you have downloaded the Ganache executable for your desired operating system, install and launch Ganache.

![Ganache releases](../../Images/ganache_create_workspace.png)

* Create a `New Workspace` and navigate through the various configuration pages. Apply the following settings on the following pages.

  * WORKSPACE
      * WORKSPACE NAME = `fintech`

  * SERVER
      * HOSTNAME = `127.0.0.1`
      * PORT NUMBER = `8545`
      * AUTOMINE = `ON`

  * ACCOUNTS & KEYS
    * ACCOUNT DEFAULT BALANCE = `100`
    * TOTAL ACCOUNTS TO GENERATE = `10`
    * AUTOGENERATE HD MNEMONIC = `YOUR MNEMONIC PHRASE`

* Once you've saved your workspace, take a few minutes to explore Ganache. Then open the Remix IDE at [remix.ethereum.org](https://remix.ethereum.org) and use your remaining time exploring Remix.
