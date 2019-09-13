### 12. Instructor Do: Starting the Blockchain (10 min)

Now it's time to start the chain!

Launch the first node into mining mode with the following command:

```bash
geth --datadir node1 --mine --minerthreads 1
```

Explain each of the new command line flags:

* The `--mine` flag tells the node to mine new blocks.

* The `--minerthreads` flag tells `geth` how many CPU threads to use during mining. Since our difficulty is low, we can set it to 1.

You should see the node `Committing new mining work`:

![node mining](Images/mining.png)

Now this is our miner in the network. Let's launch the second node and configure it to let us talk to the chain!

First, copy the entire `enode://` address (including the last `@address:port` segment)
of the first node located in the `Started P2P Networking` line:

![enodeid](Images/enodeid.png)

* We will need this address to tell the second node where to find the first node.

Open another terminal window and navigate to the same directory as before.

Launch the second node, enabling RPC, changing the default port, and passing the `enodeid` of the first node in quotes:

```bash
geth --datadir node2 --port 30304 --rpc --bootnodes "enode://69994ca26f775569b5cdb4970299c2265f7dcb7714a4ffaf66400f50e5128e79e2ff465731ddf597030f931375aa90f40d6cff7ace0f4afb84ae8de19da047bf@127.0.0.1:30303"
```

Explain each of the new command line flags:

* The `--rpc` flag enables us to talk to our node, which will allow us to use MyCrypto or Metamask to transact on our chain.

* Since the first node's sync port already took up `30303`, we need to change this one to `30304` using `--port`.

* The `--bootnodes` flag allows you to pass the network info needed to find other nodes in the blockchain. This will allow us to connect both of our nodes to each other.

The output of the second node should show information about `Importing block segments` and synchronization:

![node sync](Images/node-sync.png)

Now it's time to have the students bring their own blockchains to life!

**Note**: If you ever encounter strange errors, or need to start over without destroying the accounts,
run the following command to clear the chain data (this will reset the enode addresses as well):

```bash
rm -Rf node1/geth node2/geth
```

This will be a key command for assisting students during the next activity.
