# Running the POA Blockchain

* Create accounts for two nodes for the network with a separate `datadir` for each using `geth`.
    * ./geth --datadir node1 account new
    * ./geth --datadir node2 account new

* Run `puppeth`, name your network, and select the option to configure a new genesis block.

* Choose the `Clique (Proof of Authority)` consensus algorithm.

* Paste both account addresses from the first step one at a time into the list of accounts to seal.

* Paste them again in the list of accounts to pre-fund. There are no block rewards in PoA, so you'll need to pre-fund.

* You can choose `no` for pre-funding the pre-compiled accounts (0x1 .. 0xff) with wei. This keeps the genesis cleaner.

* Complete the rest of the prompts, and when you are back at the main menu, choose the "Manage existing genesis" option.

* Export genesis configurations. This will fail to create two of the files, but you only need `networkname.json`.

* Initialize each node with the new `networkname.json` with `geth`.
    * ./geth --datadir node1 init networkname.json
    * ./geth --datadir node2 init networkname.json

* Runs the nodes in separate terminal windows with the commands:
    *  ./geth --datadir node1 --unlock "SEALER_ONE_ADDRESS" --mine --rpc --allow-insecure-unlock
    *  ./geth --datadir node2 --unlock "SEALER_TWO_ADDRESS" --port 30304 --bootnodes "enode://SEALER_ONE_ENODE_ADDRESS@127.0.0.1:30303" --ipcdisable --allow-insecure-unlock
    * type your password and hit enter - even if you can't see it visually!

* The blockchain should hopefully be running now!