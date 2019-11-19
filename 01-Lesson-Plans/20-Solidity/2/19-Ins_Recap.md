### 19. Instructor Do: End of Day Recap (5 min)

Ask the following review questions.

* What are some aspects of Solidity?

  **Answer** Solidity is:
  * A high level object oriented programing language.

  * It is the language used to write smart contracts on the Ethereum blockchain.

  * Is strictly typed.

* What advantages would a language have for specifying the type?

  **Answer:** Specifying the data types allows the language to use the most optimal storage container for the data thus saving space.
  This is especially important for smart contracts because it costs money to store data.

  **Answer:** When the language is dealing with finance, you want the code to be very precise and accurate.

  **Answer:** Types can be used by the compiler for error-checking.

* If I pass a parameter into a function, where will I have to temporarily store that variable?

  **Answer** `In memory`

* As you know, moving Ether around on the blockchain costs money. What if we don't have enough `gas` to complete the transaction?
  Do we loose all of the gas that was sent?

  **Answer:** We do lose the gas that was used up already, but the transaction will be reversed and we would get our Ether back,
  since it was never successfully spent.

* Why do we use a testnet to test our code?

  **Answer** Ether costs real money on mainnet, we don't want to waste real money testing code.

  **Answer** Until our code is fully tested we might not uncover certain bugs or potential security vulnerabilities; testnet gives us a way to run our code as if it's in production without it actually being in production.
