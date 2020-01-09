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

* Create a new text file for notes, and copy the node's address into the file and label it `Node 1 Key`.

* Repeat the same process for the second node by replacing the `datadir` parameter with the `node2` folder.

 ```bash
 ./geth account new --datadir node2
 ```

* Make sure to keep track of the node's addresses and which belongs to which. You can always fetch the address later by printing the keystore file in the node's folder like so:

  ```bash
  cat node1/keystore/UTC--2019-10-08T20-14-04.346928000Z--959a2bd5da6097bab0c2d98e14ebfa65bed06b1b
  ```

  This will output something like:

  ```bash
  {"address":"959a2bd5da6097bab0c2d98e14ebfa65bed06b1b","crypto":{"cipher":"aes-128-ctr","ciphertext":"07d7df14c082d8d4d14c7d2877c968a9bb624f398c4b820127dcd8d0dfe62bc1","cipherparams":{"iv":"494ce9a4fb08101a52eb3f60b1b80a2f"},"kdf":"scrypt","kdfparams":{"dklen":32,"n":262144,"p":1,"r":8,"salt":"c6a8ce0ed96bada27cd8e82906a78c795953901e90736170180db97196644052"},"mac":"440e051dd3c0333966a403e8a037c50fa80355ea0a911aa323c0f9ef01214f28"},"id":"0de99a24-763b-4c98-8ed7-115954e6d420","version":3}
  ```

Now, it's time to initialize and tell the nodes to use your genesis block!

* Initialize the first node, replacing `yournetworkname.json` with your own:

 ```bash
 ./geth init yournetworkname.json --datadir node1
 ```

You should see this success message:

![geth init](Images/geth-init.png)

* Since you only initialize your nodes once, you don't need to copy anything into your notes here.

* Run the same command for `node2`.

 ```bash
 ./geth init yournetworkname.json --datadir node2
 ```

Get excited, because your blockchain is only a couple steps away from being brought to life!

Your final directory structure should look something like:

![directory tree](Images/geth-tree.png)

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
