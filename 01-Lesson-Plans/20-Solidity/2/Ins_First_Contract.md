### X. Instructor Do: First Contract (10 min)

In this demonstration, students will learn how to construct a basic contract in solidity, compile the contract, and interact with the contract.

**Files:**

* [first_contract.sol](Activities/01-Ins_First_Contract/Solved/first_contract.sol)

Open the starter file and live code a basic contract example. Be sure to highlight the following:

```solidity
pragma solidity ^0.5.11;

contract MessageContract {
    string public message = "Hello World";
}
```

* Solidity is a compiled language, so the pragma is used to define the version of the solidity compiler to use.

  ```
  pragma solidity ^0.5.11;
  ```

* Contracts are specified using a keyword `contract` and a set of curly braces.

  ```
  contract ContractName {}
  ```

* Variables in solidity require a data type to be specified. In this example, the variable type is a string.

  ```
  string public message = "Hello World";
  ```

* The `public` keyword just says that anyone can access this variable.

Take a moment to discuss data types with the class. Use the following questions to engage the class:

* What advantages would a language have for specifying the type?

  * **Sample Answer** Specifying the data types allows the language to use the most optimal storage container for the data thus saving space. This is especially important for smart contracts because it costs money to store data.

  * **Sample Answer** When the language is dealing with finance, you want the code to be very precise and accurate.

  * **Sample Answer** Types can be used by the compiler for error-checking.

Demonstrate how to compile the contract using Remix and highlight the following:

* Step 1 - open remix and navigate to...

  ![compiling-1.png](Images/compiling-1.png)

* Step 2 - ...

  ![compiling-1.png](Images/compiling-1.png)

Explain that we will continue to iterate on this example throughout the lesson to add more functionality.

---
