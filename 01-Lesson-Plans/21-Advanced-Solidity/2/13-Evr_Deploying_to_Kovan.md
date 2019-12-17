### 13. Everyone Do: Deploying the token to a Testnet (10 min)

In this activity, you will lead a code along, where the entire class will deploy their tokens to the Kovan testnet.

**Files:**

* [ArcadeTokenERC20.sol](Activities/13-Evr_Deploying_ERC20/Resources/ArcadeTokenERC20.sol)

First, assign a number to every student in the class. This will be the number that they will append to their `symbol` as a way of quickly identifying which `ArcadeToken` was deployed by each student.

Have each student modify their token's `symbol` to append their number, for example, student 33 would modify their token symbol to be `ARCD33`, student 42 would use `ARCD42`, and so on.

Once each student has set their `symbol` properly, have everyone **save their contract** before moving forward. We will be switching to the Kovan network in MetaMask, and this will trigger a refresh in Remix.

Now, switch MetaMask's network to the Kovan network, like so:

![MetaMask Kovan](Images/metamask-kovan.png)

Allow Remix to refresh and navigate back to the `ArcadeTokenERC20.sol` contract.

Have students switch over to the Kovan network and pause until everyone has switched, refreshed Remix, and reopened their contract.

Navigate to the `Deploy` tab, and switch the `Environment` from `JavaScript VM` to `Injected Web3` to connect it to MetaMask. The environment should show `Kovan (42) Network`.

Next, type in an arbitrary amount, like `333333333333333333333` into the `initial_supply` constructor parameter, then click the orange `Deploy` button:

![ERC20 Deployment](Images/arcade-token-erc20-deploy.png)

Confirm the contract deployment in MetaMask:

![Deployment Confirmation](Images/deploy-confirm.png)

Point out the following before confirming the transaction:

* The estimated price can be used to check how much deploying this token to the mainnet would cost. In this case, deploying our ERC20-compliant ArcadeToken would cost about $0.34 total.

Confirm the transaction, and have all of the students follow along and deploy their tokens to Kovan. It may take a couple minutes for everyone's transactions to confirm, but Kovan's blocktime is 5 seconds and should manage quickly.

Once everyone has deployed, point out that Remix will allow you to interact with this contract in the sidebar as usual:

![Deployed contract](Images/arcade-token-deployed.png)

Explain to the class:

* We should copy the contract's address and store it where convenient. We can always look it up on the blockchain by looking at our transaction history, but we want to have it handy.

Copy the contract's address, then refresh the page, clearing out the Remix session. Navigate back to the contract's code.

Switch the environment to `Injected Web3` again, then paste the contract's address in the `At Address` field below the orange `Deploy` button:

![Fetch contract at address](Images/arcade-token-at-address.png)

Click the `At Address` button to fetch the contract from the Kovan testnet. This will have the contract's interactive menu re-appear:

![The Arcade Token Returns](Images/arcade-token-reappear.png)

Explain to the students:

* As long as we have our contract's code, and the address, we can generate the information we need to interact with the contract.

* In fact, we don't need the code itself, just something called the ABI (Application Binary Interface), which is a compiled interface that is like an API, but in binary format. Since we have the code, we can generate the ABI. But, don't worry about that, Remix will handle that stuff behind the scenes.

* We can come back to this interactive menu at any time by pointing Remix in the right direction by setting the network and contract's address.

Now time for the exciting part, actually using our tokens!
