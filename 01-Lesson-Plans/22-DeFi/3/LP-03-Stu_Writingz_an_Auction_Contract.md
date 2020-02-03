### 3. Students Do: Writing an Auction Contract (15 min)

In this activity, students will take a SimpleAuction contract from the Solidity documentation, modify it for their own needs (remove the time-related features), and prepare it for use within another contract.

**Instructions:**

* [README.md](Activities/02-Stu_Practice/README.md)

**Files:**

* [Solved - MartianAuction](Activities/03-Stu_Writing_an_Auction_Contract/Solved/MartianAuction.sol)

* [Unsolved - MartianAuction](Activities/03-Stu_Writing_an_Auction_Contract/Unsolved/MartianAuction.sol)


### 4. Instructor Do: MartianAuction Review (15 min)

Review the code from the previous activity with the class.

Now discuss the following recall questions:

* What are some additional features that you believe could add useful functionality to this contract.

  **Potential Answer** The ability to re-open bids.

  **Potential Answer** The ability to rebid at a higher price without additional transactions.

  **Potential Answer** The ability to set a minimum bid price.

  **Potential Answer** The ability to set a max bid price.

  **Potential Answer** A buy now at market price feature.

* Are there any other events that you think this contract could benefit from having?

  **Answer** An event that is emitted when the auction opens.

  **Answer** An event that is emitted when funds are withdrawn.
