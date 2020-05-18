# Jupyter Notebook dApp Frontend Demo: Craigslist Style Message Board

### Deployment

1. Set the `WEB3_PROVIDER_URI` in the `.env` file to a public gateway or to your local ganache instance.

2. Open the [smart_contract.sol](smart_contract.sol) in the [Remix IDE](http://remix.ethereum.org) and build the contract. Copy the compiled ABI into the [smart_contract.json](smart_contract.json) file.

3. Now deploy the contract; don't forget to set your environment to `Injected web3`.

4. Copy the associated contracts address into the `.env` and set `SMART_CONTRACT_ADDRESS`.

5. Run the cells of the [message_board.ipynb](message_board.ipynb) jupyter notebook.
