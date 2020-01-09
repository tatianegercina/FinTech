# Bringing your blockchain to life

In this activity, you will be starting both nodes that you've created before to bring your blockchain to life.

* `node1` will be a full node that is also mining.

* `node2` will be a full node that exposes an RPC port, allowing you to talk to it with other apps like MyCrypto.

## Instructions

Time to start your blockchain network! Open a terminal window (Git Bash in Windows) navigate to your `Blockchain-Tools` folder and follow the next steps.

In your notes text file, make sure to keep track of **every** command you run in this activity for later. You can use these notes as a cheat-sheet later to easily start your chain again.

* Launch the first node into mining mode with the following command:

 ```bash
 ./geth --datadir node1 --mine --minerthreads 1
 ```

 * The `--mine` flag tells the node to mine new blocks.

 * The `--minerthreads` flag tells `geth` how many CPU threads, or "workers" to use during mining. Since our difficulty is low, we can set it to 1.

You should see the node `Committing new mining work`:

![node mining](Images/mining.png)

* Copy this command into your notes and label it `Start Node 1`.

Now you will launch the second node and configure it to let us talk to the chain via RPC.

* Scroll up in the terminal window where `node1` is running, and copy the entire `enode://` address (including the last `@address:port` segment) of the first node located in the `Started P2P Networking` line:

 ![enodeid](Images/enodeid.png)

* We will need this address to tell the second node where to find the first node.

* Open another terminal window and navigate to the same directory as before.

* Launch the second node, enable RPC, change the sync port, and pass the `enode://` address of the first node in quotes by running the following command (it will differ in Windows and OS X):

 * Running in OS X:
 ```bash
 ./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://<replace with node1 enode address>"
 ```

 * Running in Microsoft Windows:
 ```bash
 ./geth --datadir node2 --port 30304 --rpc --bootnodes "enode://<replace with node1 enode address>" --ipcdisable
 ```

* The output of the second node should show information about `Importing block segments` and synchronization:

 ![node sync](Images/node-sync.png)

* Copy this command into your notes and call it `Start Node 2`.

## Hints

* If you ever encounter strange errors, or need to start over without destroying the accounts, run the following command to clear the chain data (this will reset the `enode` addresses as well):

  ```bash
  rm -Rf node1/geth node2/geth
  ```

* The `--rpc` flag enables us to talk to our second node, which will allow us to use MyCrypto or Metamask to transact on our chain.

* Since the first node's sync port already took up `30303`, we need to change this one to `30304` using `--port`.

* The `--bootnodes` flag allows you to pass the network info needed to find other nodes in the blockchain. This will allow us to connect both of our nodes.

* In Microsoft Windows, we need to add the flag `--ipcdisable` due to the way Windows spawns new IPC/Unix sockets doesn't allow for having multiple sockets running from `geth` at once. Since we are only using `RCP` we can safely disable the `IPC` sockets.

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
