# Sending and Receiving ArcadeTokens on a Testnet

In this activity, you will partner up with a neighbor, and transact your tokens with each other.

## Instructions

* Get with a partner near you. Send your partner your main Ethereum wallet address you used to deploy the contract (you can copy this from MetaMask or Remix), as well your token's deployed address (copy from Remix). Make sure to specify in your message which address is which.

* Copy your ArcadeToken contract's address from the sidebar in Remix under `Deployed Contracts`. You'll need this to tell MetaMask where your token is deployed, as it won't auto-detect on a testnet.

* In MetaMask, click on the side menu to bring up a popup from the left. This should contain a link called `Add Token`. From there, click `Custom Token`, then paste your contract address. MetaMask will fill in the rest for you.

  ![MetaMask ARCD Tokens](Images/metamask-erc20.gif)

* Now, you'll be able to send your ARCD tokens directly from MetaMask using the side menu:

  ![ARCD Balance](Images/arcd-balance.png)

* If you are not satisfied with your balance, go back to Remix and `mint` yourself some tokens by setting your address as the `recipient` and setting an `amount`:

  ![Mint tokens](Images/mint.png)

* Send tokens to your neighbor by selecting the token in MetaMask, clicking `Send`, and pasting your partner's address.

![ARCD Send](Images/arcd-send.gif)

* Your partner will be sending their ARCD tokens to you. Make sure to add your partner's token contract address into MetaMask the same way you added yours to get it to recognize the balance you have of their tokens.

* Explore the transactions in the Etherscan block explorer by clicking `View Transaction Details`:

* Notice in the transaction that Etherscan will recognize the contract. Click on your contract's name and dive deeper to check out the activity happening with your tokens!

![View on Etherscan](Images/arcd-etherscan.png)

## Challenge

* If time remains, try to close Remix, then reopen your contract file, navigate to the `Deploy` tab and load the contract from its address (make sure to set `Injected Web3` as the environment). Then, mint more tokens to yourself or your partner.
