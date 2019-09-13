# Bringing your blockchain to life

In this activity, you will be starting both nodes that you've created.

* One will be a full node that is also mining.

* One will be a full node that exposes an RPC port, allowing you to talk to it with other apps like MyCrypto.

## Instructions

Time to start your blockchain network!

* Launch the first node into mining mode with the following command:

  ```bash
  geth --datadir node1 --mine --minerthreads 1
  ```

  * The `--mine` flag tells the node to mine new blocks.

  * The `--minerthreads` flag tells `geth` how many CPU threads, or "workers" to use during mining.
    Since our difficulty is low, we can set it to 1.

You should see the node `Committing new mining work`:

![node mining](Images/mining.png)

* Launch the second node and configure it to let us talk to the chain via RPC

  * Copy the entire `enode://` address (including the last `@address:port` segment)
    of the first node located in the `Started P2P Networking` line:

![enodeid](Images/enodeid.png)

* We will need this address to tell the second node where to find the first node.

Open another terminal window and navigate to the same directory as before.
This should be the parent directory of the `node1` and `node2` folders.

Launch the second node, enabling RPC, changing the default port, and passing the `enodeid` of the first node in quotes:

```bash
geth --datadir node2 --port 30304 --rpc --bootnodes "enode://<replace with node1 enode address>@127.0.0.1:30303"
```

The `--rpc` flag enables us to talk to our node, which will allow us to use MyCrypto or Metamask to transact on our chain.

Since the first node's sync port already took up `30303`, we need to change this one to `30304` using `--port`.

The `--bootnodes` flag allows you to pass the network info needed to find other nodes in the blockchain. This will allow us to connect both of our nodes to each other.

The output of the second node should show information about `Importing block segments` and synchronization:

![node sync](Images/node-sync.png)

## Hints

* If you ever encounter strange errors, or need to start over without destroying the accounts,
  run the following command to clear the chain data (this will reset the enode addresses as well):

```bash
rm -Rf node1/geth node2/geth
```
