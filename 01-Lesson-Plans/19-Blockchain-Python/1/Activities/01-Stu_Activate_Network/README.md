# Activate your local blockchain

Follow this checklist to get your local Ethereum-based blockchain running.

Using this, you can build a cheatsheet to get your `geth` nodes up and running anytime.

## Instructions

* Run the first node and enable the mining/sealing:

  ```bash
  geth --datadir node1 --unlock "SEALER_ONE_ADDRESS" --mine --rpc
  ```

  We enable the `--rpc` flag on the first node to talk to it later. This defaults to port `8545`.
  We need to unlock the node's account to enable it to sign blocks.

* Copy the enode address from this node.

  For example:
  `enode://b044f481e52f03950ed88ad18f550ace268ad4e4e1647f80c5808d6ea2c4e7f550d8ed25a14608afa6e5828f1b69fdfcf5d7775394f7c38d8592f600e4a37e90@127.0.0.1:30303`

* Use the first node's enode address as the bootnode for the second node and run on a separate port:

  ```bash
  geth --datadir node2 --unlock "SEALER_ONE_ADDRESS" --mine --port 30304 --bootnodes enode://SEALER_ONE_ENODE_ADDRESS@127.0.0.1:30303
  ```

  The command will look something like this:

  ```bash
  geth --datadir node2 --unlock "7a4f862ab163fc62dce2cfbb734ddac153c5e8cc" --mine --port 30304 --bootnodes enode://b044f481e52f03950ed88ad18f550ace268ad4e4e1647f80c5808d6ea2c4e7f550d8ed25a14608afa6e5828f1b69fdfcf5d7775394f7c38d8592f600e4a37e90@127.0.0.1:30303
  ```

  Using the first node as a bootnode will enable the nodes to communicate with each other, and discover new nodes later.

  The chain should be up and running after you start the second node.

## Hints

* Once you get the chain running, copy and paste the commands you used for each node into a README.md inside your network's folder. This will allow you to get your chain started anytime.
