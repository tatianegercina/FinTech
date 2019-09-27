# Creating two nodes with accounts

In this activity, you will create two accounts for nodes to use for mining rewards.

Then, you will be initializing the nodes using the genesis block configuration you created earlier to prep
them for bringing the chain to life!

## Instructions

First, export your genesis configuration into a `networkname.json` file:

* In `puppeth`, navigate to the `Manage existing genesis` by typing `2` and enter. You may have to type your network name again first if you're launching `puppeth` fresh.

* Then, type `2` again to `Export genesis configurations`, then continue with the default (current) directory:

![export genesis puppeth](Images/puppeth-export.png)

* This will export several `networkname.json` files -- you only need the first one without `aleth`, `parity`, or `harmony` suffixes.

Now, we need to create at least two nodes to build the chain from the genesis block onward:

* Exit `puppeth` by using `Ctrl+C`.

* Create the first node's data directory using `geth` and a couple command line flags:

```bash
geth account new --datadir node1
```

You should see a success message similar to this one:

![geth new account](Images/geth-account-new.png)

* Do the same for node 2 by replacing the `datadir` parameter with the `node2` folder.

Time to initialize and tell the nodes to use your genesis block!

* Initialize the first node, replacing `networkname.json` with your own:

```bash
geth init networkname.json --datadir node1
```

You should see this success message:

![geth init](Images/geth-init.png)

* Do the same for node 2.

Get excited, because your blockchain is only a couple steps away from being brought to life!

Your directory structure should look something like:

![directory tree](Images/geth-tree.png)
