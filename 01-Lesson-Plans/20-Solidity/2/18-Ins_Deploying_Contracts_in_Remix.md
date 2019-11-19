### 20. Everyone Do: Deploying a Contract in Remix (10 min)

In this activity students will take their `JointSavings` account contract, compile and deploy it on their local testnet.

**Files:**

* [JointSavings.sol](Activities/16-Ins_Restricting_Withdraw_With_Require/Solved/JointSavings.sol)

Let's compile and deploy our contract to test it out!

Start by having everyone open the `Ganache` application.

Instruct everyone to select the workspace we previously configured.

![Ganache Running](Images/ganache_running.png)

Ensure the students all have Ganache running before moving on.

* You should see your servers running on `http://127.0.0.1:8545`

* Navigate to [Remix](http://remix.ethereum.org/) in your browser and open the `JointSavings.sol` contract.

* Now open MetaMask, and enter the password to unlock your account, then make sure
  the network is "Localhost 8545".

![Remix Meta Mask](Images/remix_meta_mask.png)

* You should now see your primary wallet balance in MetaMask.

Click the `Deploy & Run Transaction` button in the Remix sidebar.

![Remix Deploy](Images/remix_deploy.png)

Ensure that all students are on the deploy tab before moving forward.

Now click the environment dropdown menu. By default it will have `Javascript VM` checked, switch this to `Injected Web3`. This will allow Metamask to send our contract `Eth`.

![Remix Deploy](Images/remix_enviroment.png)

* You will be prompted to connect your account in Meta Mask to remix.

![Remix Deploy](Images/remix_web3_prompt.png)

Click the yellow `Deploy` button to deploy the contract, then `Confirm` in MetaMask.

![Remix Confirm Deploy](Images/remix_deploy_confirm.png)

Pause while the students deploy their contracts.

![Remix Deployed Contract](Images/remix_deployed_contract.png)

* If your contract successfully deployed it should now appear as a grey box under deployed contracts at the bottom of the deploy sidebar.

Click the drop-down arrow next to the grey deployed contract to display the contracts functions that can be called.

![Remix Contract Functions](Images/remix_contract_functions.png)

Discuss with the students:

* These are the functions that are publically callable from the contract.

* As you can see all of the function have an input that allows you to send the function parameters.

* Notice that the deposit function does not have an input next to it, this is because it does not have any parameters. Instead you will pass it ether through the value field at the top.

Lead students through passing `10 ether` into the deposit function and then withdrawing it.

![Remix Deposit Ether](Images/remix_deposit_ether.png)

* We are now going to deposit some ether into our `JointSavings` account.

* Locate the value field and enter `10` into the input box. Then chnage the dropdown menu to the denomination `ether`. This is saying that we are going to send `10 ehter`in this transaction.

* Now click the `Deposit` button under the deployed contract.

![Remix transaction Confirm](Images/remix_transaction_confirm.png)

* You will be prompted by meta mask to confirm the amount. Click `Confirm`.

Have students confirm that that the `10 eth` was subtracted from their wallet in MetaMask.

![Remix transaction Confirm](Images/remix_meta_mask_balance.png)

* Reopen your MetaMask wallet and check to make sure that your depositied `eth` is subtracted from your wallet balance.

Lead students through withdrawing the `10 eth` from their `Jointsavings` account back to their wallet. Have students open their MetaMask wallet and copy their address at the top:

![Remix Copy Address](Images/remix_meta_mask_copy_address.png)

* Reopen your meta mask wallet and click your address at the top to copy it to your clipboard.

* Double check to make sure that this address matches one of your two addresses in your `JointSavings` account contract.

Since we defined the `amount` variable as a `uint256` we are actually working with the smallest demonimnation of `ether` called `wei`. Before we can withdraw our `10 ether` we must convert it to an equivalent amount of `wei`.

We can do this in a number of ways, we can either use `Web3.py`, a website like [eth-converter.com](eth-converter.com), or we can remember that `1 ether` is equivalent to 1 * 10^18 `wei`. That's right, we can specify incredibly small amounts of `ether` by using `wei`. In our case `10 ether` is `10000000000000000000 wei` -- aka 1 with 19 zeros after it.

Call the `Withdraw` function and pass it 10 `ether` (in `wei`) and the address to withdraw to.

![Remix Withdraw](Images/remix_withdraw.png)

* Now call the `Withdraw` function and pass it 10 `ether` (in `wei`) and your address that you would like to withdraw the funds to.

* You will have to open `MetaMask` to confirm the transaction if it does not open automatically.

![Remix Withdraw Confrim](Images/remix_withdraw_confirm.png)

Click confirm in the `MetaMask` window.

![Remix Withdraw Confrim](Images/remix_confirm_transactions.png)

* You should now see a confirmed `Deposit` transaction, a confirmed `Withdraw` transaction and your `MetaMask` wallet should now once again contain the additonal `10 ether`.

Congratulations, you have now written, compiled, deployed and executed your first smart contract!

Not only have you written a smart contract but you have learned a strictly typed programming language which will enable you to write super precise and fast code.
