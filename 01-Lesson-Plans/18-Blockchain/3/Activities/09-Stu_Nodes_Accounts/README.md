# Creating two nodes with accounts

In this activity, you will create two accounts for nodes to use for mining rewards.

Then, you will be initializing the nodes using the genesis block configuration you created earlier to prepare them for bringing the chain to life!

## Instructions

First, export your genesis configuration into a `yournetworkname.json` file as follows:

* In the `puppeth` prompt, navigate to the `Manage existing genesis` by typing `2` and hitting enter.

* You may have to type your network name again first if you're launching `puppeth` fresh.

* Then, type `2` again to choose the `Export genesis configurations` option, and continue with the default (current) directory by hitting enter:

 ![export genesis puppeth](Images/puppeth-export.png)

* This will export several `yournetworkname.json` files -- you only need the first one without `aleth`, `parity`, or `harmony` suffixes.

Now, we need to create at least two nodes to build the chain from the genesis block onward:

* Exit `puppeth` by using the `Ctrl+C` keys combination.

* Create the first node's data directory using the `geth` command and a couple of command line flags by running the following line in your terminal window (Git Bash in Windows):

 ```bash
 ./geth account new --datadir node1
 ```

You should see a success message similar to this one:

![geth new account](Images/geth-account-new.png)

* Repeat the same process for the second node by replacing the `datadir` parameter with the `node2` folder.

 ```bash
 ./geth account new --datadir node2
 ```

Now, it's time to initialize and tell the nodes to use your genesis block!

* Initialize the first node, replacing `yournetworkname.json` with your own:

 ```bash
 ./geth init yournetworkname.json --datadir node1
 ```

You should see this success message:

![geth init](Images/geth-init.png)

* Run the same command for `node2`.

 ```bash
 ./geth init yournetworkname.json --datadir node2
 ```

Get excited, because your blockchain is only a couple steps away from being brought to life!

Your final directory structure should look something like:

![directory tree](Images/geth-tree.png)

---
© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
