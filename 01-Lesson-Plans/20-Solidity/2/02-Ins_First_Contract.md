### 2. Instructor Do: First Contract (10 min)

In this activity, you will demonstrate how to construct a basic contract in Solidity that sets an arbitrary `string` and an `address`.

**Files:**

* [first_contract.sol](Activities/02-Ins_First_Contract/Solved/first_contract.sol)

Open your web browser and navigate to the [Remix IDE website](http://remix.ethereum.org):

 ![remix_1.png](Images/remix_1.png)

Click on the create new file button in the file explorer:

 ![remix_2.png](Images/remix_2.png)

Enter the name of the new Solidity file "message_contract.sol" and click `OK`:

 ![remix_3.png](Images/remix_3.png)

You should now see the following empty editor window:

![Images/remix_4.png](Images/remix_4.png)

Type the following contract into the editor window:

```solidity
pragma solidity ^0.5.0;

contract MessageContract {
    address my_address = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
    string message = "Send me money!";
}
```

Break down the contract to the students:

* Since the Solidity language is always being updated, we have to define what version we are writing our smart contract in.
  In this class, we're writing version `0.5.0` and up.

```solidity
pragma solidity ^0.5.0;
```

* Contracts are specified using a keyword `contract` and a set of curly braces.

```solidity
contract ContractName {}
```

* Variables in Solidity require a data type to be specified. In this example, the variable type is a `string`:

```solidity
string message = "Hello World";
```

* The `address` variable is a native type that recognizes an Ethereum address and stores it in a way that is cheaper than a string.

```solidity
address my_address = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;
```

Take a moment to discuss data types with the class.

Explain to the class:

* In contrast to Python, Solidity is very strict in the way that variables and functions are defined.

* There are several reasons for this:

  * Much like how a legal contract does not leave room for ambiguity, we also remove the same ambiguity from our code
    by being very specific about how we are storing data, like strings, numbers, arrays, or booleans (true/false values).

  * When we define the data types up front, the Solidity compiler does not have to expend the resources figuring out what type the data is.
    In Python, the interpreter runs the code and figures out the types on the fly. While this makes writing the code easier, it is more
    expensive to run since Python has to calculate the type again every time.

  * Different data types have a different gas cost associated with it. Therefore, if you have to store an `address`, you should use the native
    `address` type instead of a `string`, since it's cheaper that way.

Use the following questions to engage the class:

* What advantages would a language have for specifying the type?

  **Answer:** Specifying the data types allows the language to use the most optimal storage container for the data thus saving space.
  This is especially important for smart contracts because it costs money to store data.

  **Answer:** When the language is dealing with finance, you want the code to be very precise and accurate.

  **Answer:** Types can be used by the compiler for error-checking.

Demonstrate how to compile the contract using Remix and highlight the following:

Click the "Solidity Compiler" button on the remix sidebar.

![remix_compiler_button.png](Images/remix_compiler_button.png)


Click `Compile`:

![remix_compile_contract.png](Images/remix_compile_contract.png)

Explain that we will continue to iterate on this example throughout the lesson to add more functionality.
