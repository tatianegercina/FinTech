### 10. Instructor Do: Storing, Catching, Withdrawing Ether (10 min)

In this activity the we will demonstrate how to add functions for depositing ether, withdrawing ether, and a default "fallback" function that can be used to catch Ether sent from outside a function call. The `payable` modifier will be introduced and added to payable functions as well as to payable addresses in the contract.

Open [Remix](http://remix.ethereum.org) and create a new file called `JointSavings.sol`.

* Earlier in the day we built a simple contract that stored variables representing a rewards/bank account balance.
  Let's take that a step further, and build a JointSavings account smart contract that allows two addresses to manage a savings account.

Type the following contract boilerplate:

```solidity
pragma solidity ^0.5.0;

contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;
}
```

* Once again we are defining what version of the compiler we want to use by setting the `pragma`.

* Then, we define the contract and call it `JointSavings`.

* Next, we set two `address`es to represent the owners of the JointSavings account.

* Pay special attention to the new modifier that we are using called `payable`.
  By setting an `address` or function as `payable`, we unlock special functions that allow us to capture and manage Ether.

For example, if we wanted to withdraw Ether from the contract, we can add a withdraw function like so:

```solidity
pragma solidity ^0.5.0;

contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

  function withdraw(uint amount, address payable recipient) public {
    return recipient.transfer(amount);
  }
}
```

* Our withdrawal function accepts the following parameters:

  * A `uint` amount representing the amount of Ether (in its smallest denomination, wei) we would like to withdraw.

  * The `address` recipient that we would like to withdraw to.

* All smart contracts on Ethereum have their own address when deployed, and can store and send Ether like a wallet.

* Address types have built in functions, like `address.balance`.
  If we set the address to `payable`, the `.transfer` function is enabled, which allows us to transfer
  Ether from the contract's wallet to that address.

* Notice that we have the recipient parameter set as a `payable address` in this withdraw function.
  We still have to be explicit like this in the parameters as well, so that we can call the `.transfer` function on the
  recipient address later in the function.

Now that we have the ability to withdraw let's add the ability to deposit:

```solidity
pragma solidity ^0.5.0;

contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

  function withdraw(uint amount, address payable recipient) public {
    return recipient.transfer(amount);
  }

  function deposit() public payable {}
}
```

* Remember, all smart contracts on Ethereum have their own address when deployed, and can store and send Ether like a wallet.
  It is up to us to create functions that manage this Ether properly, like we did with the withdraw function.

* When we create a deposit function and set it to `payable`, we are telling the contract to accept the Ether that is sent to this function.

* As you can see our `deposit` function body is blank; our function does not contain anything.
  The reason for this is that we only register this function to accept and hold the Ether that we send it,
  and this can be done by just adding the `payable` modifier. We can add more to this function later, like event logging,
  but for now, we'll just do a bare-bones deposit function.

* We now have a complete contract where any account can send our contract Ether through the `deposit` function.
  It can also send any amount of Ether to any address that we specify in the `withdraw` function (as long as we have enough balance, of course!).

Ask the students the following question:

* As you know, moving Ether around on the blockchain costs money. What if we don't have enough `gas` to complete the transaction?
  Do we loose all of the gas that was sent?

  **Answer:** We do lose the gas that was used up already, but the transaction will be reversed and we would get our Ether back,
  since it was never successfully spent.

We are going to add one final line to make sure that if Ether is sent to the contract without using the `deposit` function,
(i.e., sending Ether directly to the contract's address) we can still capture the Ether into the contract's wallet.

* If we don't add this `payable` fallback function, and Ether is sent to our contract address, it will return the Ether instead,
  forcing other users to send via the `deposit` function. In our case, we just want to capture any and all Ether sent to the contract.

```solidity
pragma solidity ^0.5.0;

contract JointSavings {
  address payable account_one = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
  address payable account_two = 0xA29f7E79ECEA4cE30DD78cfeb9605D9aFf5143a5;

  function withdraw(uint amount, address payable recipient) public {
    return recipient.transfer(amount);
  }

  function deposit() public payable {}

  function() external payable {}
}
```

Great! Now we have a fully functioning Savings account contract. We can use this smart contract to store Ether, and withdraw
it to any address we choose!
