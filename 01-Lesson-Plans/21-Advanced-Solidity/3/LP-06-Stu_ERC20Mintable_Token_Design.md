### 6. Students Do: ERC20 Mintable Token Design (10 min)

In this activity, students will build a mintable ERC20 token and prepare it for a crowdsale.

**Instructions:**

* [README.md](Activities/06-Stu_ERC20Mintable_Token_Design/README.md)

### 7. Instructor Do: ERC20Mintable Review (10 min)

Review the previous activity with the class by discussing the following recall questions.

* What are some benefits of using the OpenZeppelin libraries?

* **Answer** OpenZeppelin follows the community standards defined for various ERCS.

* **Answer** Saves development time by providing a boilerplate for common tasks.

* **Answer** OpenZeppelin smart contracts are secure.

* Why might we restrict who can mint tokens?

* **Answer** If anyone could mint tokens using our contract, it would essentially make them worthless.

* What are we doing when we say `ArcadeToken is ERC20` in our contract definition.

* **Answer** We are inheriting the functions and properties from ERC20 to ArcadeToken.

* What are some things a function modifier may be used for in solidity?

* **Answer** To restrict access to a function.

* **Answer** To expose a function.

* **Answer** To add dependencies to a function.
