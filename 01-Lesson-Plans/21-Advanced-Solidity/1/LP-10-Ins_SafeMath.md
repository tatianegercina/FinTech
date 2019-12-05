### 10. Instructor Do: 3rd Parties Libraries in Solidity (SafeMath) (15 min) (Critical)

Now that we've built tokens, our code is not secure.
In this activity, we're going to make our contracts secure by using a library called SafeMath from OpenZeppelin.

But first, let's demonstrate how our contract is vulnerable to rewarding infinite tokens via an "integer underflow" exploit.

Continue with the `ArcadeToken.sol` contract. It should match the unsolved file below at this point.

**Files:**

* [ArcadeTokenSafeMath.sol](Activities/10-Ins_SafeMath/Unsolved/ArcadeTokenSafeMath.sol)

In the `Deploy` tab in Remix, expand the `transfer` function of the `ArcadeToken` contract deployed in the previous activity.

Deploy a new version of the contract to ensure that your account has an `ARCD` balance of `0`.

Fill in any address that is **different** from the current account in the `recipient` field, and a value of `1` in the `value` field:

![Vulnerable Transfer](Images/arcade_token_vulnerable_transfer.png)

Hit `Transact`, confirm the transaction in MetaMask, then click on the `balance` function in the contract.

You will notice that you have an extremely high balance of tokens, in fact, the maximum balance you could possibly have!

![Hacked Balance](Images/hacked_balance.png)

Ask the class:

* Can anyone spot the vulnerability in our code that allows this to happen?

Allow the students to give their answers, then confirm:

* We are subtracting the balance from the `msg.sender` without checking if there is enough first!

* When we subtract `1` from a `uint` that is set to `0`, we actually perform something called an "integer underflow."

* Imagine if you took a car's odometer (mileage tracker) and cranked it to the maximum value it could support.
  What would happen when you reached mile `999999999...`? It would reset back to `0`. That's an integer overflow.

* An underflow is the opposite, when we subtract `1` from `0`, we roll it back to the maximum value that can fit inside a `uint`.
  By default, most programming languages behave this way. It's up to us to make sure that does not happen.

Ensure the students understand the concept of an underflow/overflow and how it allows us to hack an insecure contract, then move on.

* Thankfully, there are libraries out there that allow us to write more secure smart contracts.

Introduce the OpenZeppelin project, and the SafeMath library:

* The OpenZeppelin project contains many standardized smart contracts and templates to help the community build off of.
  This allows developers to write more secure and efficient Solidity code.

* To fix our contract, we can leverage the SafeMath library provided by OpenZeppelin.

* The SafeMath library provides the guardrails we need to prevent integer underflows and overflows and similar vulnerabilities.

Navigate back to Remix and edit the `ArcadeToken` contract.

Import the SafeMath library at above the contract definition like so:

```solidity
pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/math/SafeMath.sol";

contract ArcadeToken {
    // ...
}
```

* Remix supports importing libraries straight from Github. It will automatically resolve the dependencies for us.

Next, in the first line of the contract, add `using SafeMath for uint;` to link the library to the `uint` type:

```solidity
pragma solidity ^0.5.0;

import "github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/math/SafeMath.sol";

contract ArcadeToken {
    using SafeMath for uint;

    // ...
}
```

Explain to the class:

* We need to add this line at the beginning of our contract to link the library to the `uint` data type.

* This adds special functions to any object using the `uint` type, like `.add()`, `.sub()`, `.mul()`, and `.div()` that we can use instead of the `+`, `-`, `*`, and `/` operators.

Modify the `transfer` function to use the SafeMath assignments instead of the standard `-` and `+` operators:

```solidity
function transfer(address recipient, uint value) public {
    balances[msg.sender] = balances[msg.sender].sub(value); // prevents integer underflow
    balances[recipient] = balances[recipient].add(value);
}
```

* Notice now we can call `.sub()` and `.add()` on the `uint` values that come from the `balances` mapping.

* By performing math operations this way, we now prevent integer underflows! Let's try to perform the same hack on our contract again and see what happens.

Deploy a fresh version of this newly modified contract and fill in the `transfer` function with the same details as before:

![Secure Transfer](Images/arcade_token_secure_transfer.png)

Now, attempt to make the same transaction. You will need to ignore a `Gas estimation failed` error -- this is because even the EVM knows an error is likely to occur.

Sending the transaction anyway will result in an error like:

![MetaMask Failed](Images/metamask_failed.png)

The log in Remix will show something like:

```shell
transact to ArcadeToken.transfer pending ...
transact to ArcadeToken.transfer errored: Error: [ethjs-rpc] rpc error with payload {"id":559065790857,"jsonrpc":"2.0","params":["0xf8ab1a843b9aca00832dc6c094aa6b6a74aec9a4d05484c9841dd911b35838bb4180b844a9059cbb000000000000000000000000a29f7e79ecea4ce30dd78cfeb9605d9aff5143a50000000000000000000000000000000000000000000000000000000000000001822d45a0dc029786c5cb8efb0c75ed6d6c86db6f75e5e51af57e584f0df168e6d4fffbf0a069cabf26a54d320aaea8d68d98d02d296fbf80335200c6434b021f9324058ef7"],"method":"eth_sendRawTransaction"} [object Object]
```

* Voila! Now are contract is secured against integer under/overflows.

* Note, this will only work with `uint` currently, but we can declare it for `int` as well in the future.

* We'll need to make sure that we replace every instance of a normal operator like `+`, `-`, `*`, `/`, etc, with the SafeMath alternatives.

* It is good practice to leverage this library by default, and the majority of smart contract developers do the same as it has prevented many tokens from being compromised.

Now it's time for students to secure their tokens!
