### 09. Instructor Do: Contextualizing Solidity (15 min)

In this exercise, the instructor will explain to the students that Solidity is a statically typed language and that it runs inside the EVM in a sandbox.

**Files**

[EVM Diagram](Images/EVM.png)

* Solidity is the language of smart contracts used by Ethereum, as well as Ethereum-compatible blockchains like IBM's Hyperledger Fabric and Burrow, JPMorgan Chase's Quorum, Ethereum Classic, and last, but not least, Counterparty which extends Bitcoin to support the EVM.

* We're going to learn Solidity this week! It's a statically typed language, so it will also help you understand other statically typed languages like C++.

Present the following diagram to the class and give them a few minutes to think about what is being illustrated.

* Try to conceptualize what is happening in the graphic.

![Diagram](Images/EVM.png)

* The Ethereum Virtual Machine is a sandboxed environment backed by a virtual stack and capable of performing calculations. There's an EVM embedded within every Ethereum full node on the Ethereum network. Since code executes inside the sandboxed processes of the Ethereum node, machine code remains isolated from the host machine. Let's break down the levels of the following graphic.

* Higher Level language

  * Solidity is the `Higher Level Language` of the EVM.

  * A higher level language allows code to be written that is independent of a particular computer's hardware.

  * A higher level language is a language that is more easily understandable for humans than machine code.

  * A higher level language cannot be understood by a computer; it has to be compiled to machine code by the compiler before it can be understood.

* Machine Code

  * EVM machine code consists of a list of instructions that the EVM will perform.

  * A user pays a certain amount of `gas` for each instruction that gets executed by the EVM.

  * Instead of just a transaction fee like `bitcoin`, you have a fee for running programs.

Show the class the example machine code.

```bytecode
 "opcodes": "PUSH1 0x80 PUSH1 0x40 MSTORE CALLVALUE DUP1 ISZERO PUSH2 0x10 JUMPI PUSH1 0x0 DUP1 REVERT JUMPDEST POP PUSH1 0x40 MLOAD PUSH2 0x872 CODESIZE SUB DUP1 PUSH2 0x872 DUP4 CODECOPY DUP2 DUP2 ADD PUSH1 0x40 MSTORE PUSH1 0x20 DUP2 LT ISZERO PUSH2 "
```

* Virtual Machine

  * The EVM contains a memory, storage, and all of the essential parts of a physical computer, just virtual, and sandboxed inside of your Ethereum node.
  
  * Every Ethereum node runs the EVM, which is how all Ethereum nodes are able to process and validate transactions and smart contracts.

* Process/Runtime

  * The process/runtime is the actual process that runs on the host machine.

  * The Ethereum node spawns a process for the EVM.

  * It takes multiple full nodes running multiple EVM's to verify calculations.

  * `Geth` is one implementation of an Ethereum full node written in GO.

* Hardware

  * Since blockchains are written in software, the hardware can be any machine that is capable of running the node software and connecting to the internet.
