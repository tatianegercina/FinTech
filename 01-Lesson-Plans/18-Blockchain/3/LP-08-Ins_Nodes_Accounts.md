### 8. Instructor Do: Creating two nodes with accounts (10 min)

First, we need to export our genesis configuration into a `json` file.

In `puppeth`, navigate to the `Manage existing genesis` by typing `2` and enter.

Then, type `2` again to `Export genesis configurations`, then continue with the default (current) directory:

![export genesis puppeth](Images/puppeth-export.png)

* This will export several `networkname.json` files -- we only need the first one without `aleth`, `parity`, or `harmony` suffixes.

* We can use the `networkname.json` file to initialize any new nodes in the system automatically to grow the network!

Now, we need to create at least two nodes to build the chain from the genesis block onward.
Exit `puppeth` by using `Ctrl+C`.

Then create the first node's data directory using `geth` and a couple command line flags:

```bash
geth account new --datadir node1
```

* Explain to the class that you are using `geth` here to create a new account in the `node1` folder.
  This is where all data belonging to the first node will belong, and the address that the mining rewards will go.

You will have to enter a password to encrypt the keypair. Ask the students:

* What type of cryptography are we using when we lock the keys with a password?

  **Answer**: Symmetric cryptography!

* In this case, we're actually locking a pair of asymmetric keys with a symmetric password, wild times!

It might be worth mentioning that by doing this, we create a security bottleneck with our password.
All a hacker has to do is brute force the password, which is significantly easier than the long private key.

**Note**: In production, you would use a hardware wallet, but more on the different types of wallets next unit.

Once you successfully create the account you should see this message:

![geth new account](Images/geth-account-new.png)

Next, create another account using a different `datadir`:

```bash
geth account new --datadir node2
```

* Explain to the students that you typically would only have one node per machine, but you need
  at least two to create a blockchain and that's why we're doubling up on the same computer.

* Now we have two folders that each node can use to store its private key and its copy of the blockchain.

Time to initialize and tell the nodes to use our genesis block!

```bash
geth init puppernet.json --datadir node1
```

You should see this success message:

![geth init](Images/geth-init.png)

* Explain to the class that this node is now initialized. This means that it is using our genesis block as a starting
  point.

Repeat this process for the second node:

```bash
geth init puppernet.json --datadir node2
```

Your directory structure should look something like:

![directory tree](Images/geth-tree.png)

The chain is ready to be started. Now it's time to have the students initialize their nodes.
