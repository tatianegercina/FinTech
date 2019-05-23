# Proof of Authority Development Chain

## Background

Remember `puppeth`? Great!

You have been tasked by your manager to create a new testnet for the company, so that developers can deploy their
applications in-house without paying fees, and without relying on a public testnet. However, she mentioned that she
doesn't want to waste any energy mining! She wants you to create nodes for the two DevOps engineers that will
take over management of the chain. You will need to use the Clique Proof of Authority consensus mechanism.

This is a much more effective algorithm for development or private networks, since it does not require any mining,
but rather assigns "Authority" of producing or "sealing" new blocks to specific addresses on the network.
This is more like a role based access control system in non-blockchain or centralized environments or applications,
so your DevOps engineers will be able to maintain the chain without worry of users changing any rules.

In this assignment, you will be creating an out-of-the-box development blockchain that anyone can use as a playground
for blockchain applications without having to deploy to the mainnet and pay fees to do so, and without mining.
This also allows for offline development, as there is no need to rely on a live testnet such as Ropsten or Kovan.

You should be able to forge the commands necessary to run both nodes in conjunction, and to hand each DevOps engineer
their designated command. You should be able to run both nodes locally and test the chain as well.

Tokens inherently have no value here, so we will provide pre-configured accounts and nodes for easy setup.

After creating the custom development chain, create documentation for others on how to start it using the pre-configured
nodes and accounts. You can name the network anything you want, have fun with it!

Be sure to include any preliminary setup information, such as installing dependencies and environment configuration.

## Instructions

### Setup the custom out-of-the-box blockchain

- Create a new project directory for your new network. Call it whatever you want!

- Create a "Screenshots" folder inside of the project directory.

- Create accounts for two (or more) nodes for the network with a separate `datadir` for each using `geth`.

- Run `puppeth`, name your network and select the option to configure a new genesis block.

- Choose the `Clique (Proof of Authority)` consensus algorithm.

- Paste both account addresses from the first step one at a time into the list of accounts to seal.

- Paste them again in the list of accounts to pre-fund. There are no block rewards in PoA, so you'll need to pre-fund.

- You can choose `no` for pre-funding the pre-compiled accounts (0x1 .. 0xff) with wei. This keeps the genesis cleaner.

- Complete the rest of the prompts, and when you are back at the main menu, choose the "Manage existing genesis" option.

- Export genesis configurations. This will fail to create two of the files, but you only need `networkname.json`.

- You can delete the `networkname-harmony.json` file.

- Screenshot the `puppeth` configuration once complete and save it to the Screenshots folder.

- Initialize each node with the new `networkname.json` with `geth`.

- Run the first node, unlock the account, enable mining and the RPC flag. Only one node needs RPC enabled.

- Set a different peer port for the second node and use the first node's `enode` address as the `bootnode` flag.

- Be sure to unlock the account and enable mining on the second node!

- You should now see both nodes producing new blocks, congratulations!

### Send a test transaction

- Use the MyCrypto GUI wallet to connect to the node with the exposed RPC port.

- You will need to use a custom network, and include the chain ID, and use ETH as the currency.

![custom-node](Images/custom-node.png)

- Import the keystore file from the `node1/keystore` directory into MyCrypto. This will import the private key.

- Send a transaction from the `node1` account to the `node2` account.

- Copy the transaction hash and paste it into the "TX Status" section of the app, or click "TX Status" in the popup.

- Screenshot the transaction metadata (status, tx hash, block number, etc) and save it to your Screenshots folder.

- Celebrate, you just created a blockchain and sent a transaction!

![transaction-success](Images/transaction-success.png)

### Create a repository, and instructions for launching the chain

- Create a `README.md` in your project directory and create documentation that explains how to start the network.

- Remember to include any environment setup instructions and dependencies.

- Be sure to include all of the `geth` flags required to get both nodes to mine and explain what they mean.

- Explain the configuration of the network, such as it's blocktime, chain ID, account passwords, ports, etc.

- Explain how to connect MyCrypto to your network and demonstrate (via screenshots and steps) and send a transaction.

- Upload the code including the `networkname.json` and node folders.

### Remember, *never* share your mainnet private keys! This is a testnet, so coins have no value here!

### Challenge mode

- Create a separate `bootnode` dedicated to connecting peers together

- There will be a new DevOps engineer joining the team, add an additional sealer address to the network on the fly!
