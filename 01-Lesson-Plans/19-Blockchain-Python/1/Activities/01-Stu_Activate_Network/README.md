# Activate your local blockchain

Follow this checklist to get your local Ethereum-based blockchain running.

Using this, you can build a cheatsheet to get your `geth` nodes up and running anytime.

## Instructions

* Run the first node and enable the mining/sealing:

  ```bash
  ./geth --datadir node1 --unlock "SEALER_ONE_ADDRESS" --mine --rpc
  ```

  Substitute the "SEALER_ONE_ADDRESS" with the the public address of the first node that was created in the previous session (do **not** include the leading `0x`). We enable the `--rpc` flag on the first node to talk to it later. This defaults to port `8545`.
  We need to unlock the node's account to enable it to sign blocks.

  **NOTE**: If you receive the error - _Fatal: Account unlock with HTTP access is forbidden!_ - complete the following additional steps:
  * Add the flag `--allow-insecure-unlock`.
  * Enter your password if prompted.

* Copy the enode address from this node.

  For example:
  `enode://b044f481e52f03950ed88ad18f550ace268ad4e4e1647f80c5808d6ea2c4e7f550d8ed25a14608afa6e5828f1b69fdfcf5d7775394f7c38d8592f600e4a37e90@127.0.0.1:30303`

* Use the first node's enode address as the bootnode for the second node and run on a separate port. The command to do this will vary from OS X to Windows:

    * Running in OS X:
      ```bash
      ./geth --datadir node2 --unlock "SEALER_TWO_ADDRESS" --port 30304 --bootnodes enode://SEALER_ONE_ENODE_ADDRESS@127.0.0.1:30303
      ```

      The command will look something like this:

      ```bash
      ./geth --datadir node2 --unlock "7a4f862ab163fc62dce2cfbb734ddac153c5e8cc" --port 30304 --bootnodes "enode://b044f481e52f03950ed88ad18f550ace268ad4e4e1647f80c5808d6ea2c4e7f550d8ed25a14608afa6e5828f1b69fdfcf5d7775394f7c38d8592f600e4a37e90@127.0.0.1:30303"
      ```
    * Running in Windows:
      ```bash
      ./geth --datadir node2 --unlock "SEALER_TWO_ADDRESS" --port 30304 --bootnodes enode://SEALER_ONE_ENODE_ADDRESS@127.0.0.1:30303 --ipcdisable
      ```

      The command will look something like this:

      ```bash
      ./geth --datadir node2 --unlock "7a4f862ab163fc62dce2cfbb734ddac153c5e8cc" --port 30304 --bootnodes "enode://b044f481e52f03950ed88ad18f550ace268ad4e4e1647f80c5808d6ea2c4e7f550d8ed25a14608afa6e5828f1b69fdfcf5d7775394f7c38d8592f600e4a37e90@127.0.0.1:30303" --ipcdisable
      ```
  Substitute the "SEALER_TWO_ADDRESS" with the the public address of the second node that was created in the previous session. (do **not** include the leading `0x`)

  Using the first node as a bootnode will enable the nodes to communicate with each other, and discover new nodes later.

  The chain should be up and running after you start the second node.

  **NOTE**: If you receive the error - _Fatal: Error starting protocol stack: Access is denied._ - complete the following additional steps:
  * Add the flags `--allow-insecure-unlock` and `--ipcdisable`
  * Enter your password if prompted. 
  * It may be difficult to see the password prompt (as seen in the image below), however you must still input the password and hit enter for the chain to begin mining.

  ![Password prompt](../../Images/password-prompt.png) 

## Hints

* If you aren't seeing any movement in the wallet amounts in MyCrypto after sending/receiving transactions, make sure you are sending a large enough sum of ETH to see actual movement in the digits. You may have to click on the amount itself to see the full value down to the WEI.
    ![before_after_click_mycrypto](../../Images/before_after_click_mycrypto.png)
* If increasing the transaction value and clicking on the wallet amount doesn't help, try the following:
    * Terminate both nodes using `control+C` in the Node1 and Node2 terminal windows.
    * Change networks in MyCrypto to a Testnet such as Kovan.
    * Restart Node1 and Node2 in their terminal windows.
    * Reconnect to your network in MyCrypto.
    * Log into your wallet and refresh the amount.
* Once you get the chain running, copy and paste the commands you used for each node into a README.md inside your network's folder. This will allow you to get your chain started anytime.
