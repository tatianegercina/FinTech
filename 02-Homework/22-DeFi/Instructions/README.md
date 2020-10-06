# Unit 22: We're going to Mars!

![mars](https://image.shutterstock.com/image-photo/silhouette-astronaut-standing-on-rocky-600w-1049625047.jpg)

The Martian Development Foundation has asked you to develop a system to raise funds for Martian land development.
The system will be a combination of an ERC721 contract and an Auction contract combined to form the MartianMarket contract.

The foundation will be able to register new landmarks with their account, minting and creating a new auction for the landmark.
When the `endAuction` function is called, the auction will complete and the token will be transferred to the highest bidder.

The functions of the contract can be designed to have the foundation pay for the most expensive functions like`safeTransferFrom`.
This can be done by putting the token transfer in the `endAuction` function that only the foundation can call.

Each landmark will be a unique ERC721 token, with its own metadata including the landmark `name` and `image` URL.

Your frontend developer has already provided you the UI necessary for getting the job done, all you need to do is
implement the contracts. Good luck! Remember, you're building something few people have explored, so don't be afraid!

# Instructions

## Files

- [Starter Code](Starter-Code/martian-market)

## Before you begin

1. An infura account and endpoint is necessary for this assignment.

2. Go to [infura.io](https://infura.io/) and sign up for an account.
![infura_sign-up](Images/infura_sign-up.png)

3. Once you've signed up, create a project and record the end point:
![infura_create_project](Images/infura_create_project.png)
![infura_endpoint](Images/infura_endpoint.png)

## Setting up your project

1. Create a new Github repository named `martian_market` and clone it to your machine. 
2. From your terminal, `cd` into the repo directory and copy the contents of the [starter code] file into it.
3. Remaining inside the repo directory, run the following commands in your terminal:

    * `npm install`
    * `npm install -g truffle`
    * `npm install @truffle/hdwallet-provider`
    * `npm install @openzeppelin/contracts`

4. These commands will install various dependencies that will allow for more streamlined deployment of your app.
5. Navigate to the `truffle-config.js` file and make the following changes:
    * On line 22, insert your mnemonic phrase.
    * On line 61, insert your infura endpoint.
    * Save the file. 

## Designing the contracts

### MartianAuction

The included `MartianAuction.sol` contract is a direct copy of the `SimpleAuction` contract from the
[Solidity documentation](https://solidity.readthedocs.io/en/v0.5.10/solidity-by-example.html?highlight=auction#id2).
You will need to modify this contract in the following ways:

- Remove the biddingTime functionality, ensuring the foundation can call end the auction any time

- Set `ended` as a `public` variable so the `MartianMarket` contract can access it with an automatic getter

- Change `msg.sender` in the `bid` function to a payable address parameter instead, to make it easier for the `MartianMarket`
  contract to call and to allow bidding on behalf of another address

- Add a `require` in `auctionEnd` that only allows the beneficiary to end the auction

### MartianMarket

This contract will store an array of MartianAuctions in a mapping of tokenIds to MartianAuctions.
When the auction ends, the token ownership will be transferred to the highest bidder of the auction.

You will need to complete the functions provided in the starter code. Here are some tips for the main functions:

- In `endAuction`, you will need to end the auction, then perform a `safeTransferFrom`, transferring the token to the
  `auction.highestBidder()` from the `owner()`

- In the bid function, you will need to pass the `msg.value` to the function call to pass the ether to the auction.
  You can do this by adding `value(msg.value)` immediately before the parameter.
  It will look something like `auction.bid.value(msg.value)(msg.sender);`

- The rest of the functions are mostly just exposing the internal `MartianAuction` functions by fetching the auction by
  tokenId and calling the functions from that instance. The `getAuction` function is very useful and should be completed
  early.

- Make sure to include `require(_exists(tokenId), "error message here")` when possible, and other `requires` that will
  prevent lost ether or enforce security.

## Deploying to a Testnet

1. After the contracts are properly implemented, use your terminal to run the command `truffle deploy` and pass your desired network using the `--network` flag. Example:

```python
truffle deploy --network ropsten
```
2. This will initiate a process of deployment that will take some time, so don't worry if it looks like things are stalling. You should see output to your screen similar to the following:

![deployment_output](Images/deployment_output.png)

3. Once this process is complete, your contract will full deployed on the Testnet of your choice.  

4. **Important!:** 
    * Make sure you copy the contract address from the output!
    * Make sure you copy the deployer address from the output!

    ![deployment_addresses](Images/deployment_addresses.png)

## Modifying the frontend code

* Navigate to the file titled `dapp.js`.  At the very top of the file, you will need to insert your newly revealed contract address. This will ensure the frontend can communicate with the smart contract backend. 

## Testing the Market

* To test your dApp:
    
    * cd into `martian_market` and run `npm run dev`.

    * This command will launch the front end via a local server that will allow you test your app locally in your browser.

    * Once you run the command, you can type `localhost:1234` in your browser and the app should be visible and available for testing.

    * You should import at least 2 accounts into MetaMask, the first being the deployer of the contracts (the one we notated in the deployment process) and one other address of your choosing to test non-admin features.

* After launching with the above steps, you should see something like this:

![market](Images/market.png)

* You should be able to bid on a token:

![bid](Images/bid.png)

* When you are out-bid, you should be able to withdraw your pending balance in escrow:

![withdraw](Images/withdraw.png)

* When you are using the foundation account in MetaMask, you should be able to end auctions as well. This will then transfer the token to the highest bidder of the auction. You will see this as such:

![ended](Images/ended.png)

* You can also register new land using the foundation address:

![register](Images/register.png)


## Github Deployment

1. With the contracts and front end fully functioning, you can now deploy to github pages for a live, interactive dApp experience to add to your portfolio!

2. Deploy to Github Pages by running the command `npm run deploy` in your terminal. This will run the provided convenience package `gh-pages` will automatically publish the bundle to the `martian_market` repo you initialized in the beginning of the homework. 

3. After running `npm run deploy` continue the normal process of pushing to your remote repository.

## Submission

Once the dapp is live on Github Pages and accessible to the world, utilize the `README.md`to explain how the dapp works and how it is built. Remember: the more details, the better.

Ensure that you have changed the `contractAddress` in the frontend code to be the address deployed on a live network.

## Celebrate

You have just created a system that few people in the world have ever even imagined! Just imagine all of the things you
can build now. By building this, you have flexed every Solidity muscle you can. You have proved to the world and to yourself
that you can build next generation financial technology!
