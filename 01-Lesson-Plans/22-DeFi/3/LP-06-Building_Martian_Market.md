### 6. Students Do: Building the MartianMarket (20 min)

In this activity, students will be building the ERC721 + Auction based `MartianMarket`.

Have TAs circulate the room and ensure students are able to complete the activity.

**Instructions:**

* [README.md](Activities/06-Stu_Building_Martian_Market/README.md)

**Files:**

* [MartianMarket.sol](Activities/06-Stu_Building_Martian_Market/Unsolved/MartianMarket.sol)

* [MartianAuction.sol](Activities/06-Stu_Building_Martian_Market/Resources/MartianAuction.sol)

### 7. Instructor Do: Martian Market Review (10 min)

**Files:**

* [MartianMarket.sol](Activities/06-Stu_Building_Martian_Market/Solved/MartianMarket.sol)

* [MartianAuction.sol](Activities/06-Stu_Building_Martian_Market/Resources/MartianAuction.sol)

Open the solution and review the `MartianMarket` code. Make sure to explain the following:

* In the `bid` function, we are using the `.value` syntax.

  * We must be careful about this syntax, as it only forwards `2300` gas. Since that's enough to complete our function, we're okay. Otherwise, we'd have to add `.call` right before `.value()`. That forwards the remaining gas, but that syntax doesn't protect against re-entrancy attacks, so we'd need to be very careful about modifying the state of our contract in that case.

Ask the students:

* If we needed to drop down to the lower level `.call.value` syntax, how could we prevent a re-entrancy attack?

  **Answer:** We'd need to set any state that limits an Ether withdrawal before calling the external function. Like in the `MartianAuction` contract, we set the `pendingReturns` for the address that is calling the `withdraw` function *before* calling `.send`. If were able to get our function to `re-enter`, the check would know they already withdrew and stop the function from sending more Ether.

* What are some ways we can improve the logic of the `MartianMarket`? Can we make it more decentralized? How?

  **Answer:** We could implement a voting system to manage the `Martian Land Foundation` in a decentralized way, like a `DAO`.

  **Answer:** We could use a voting system to decentralize the process of land registration.

  **Answer:** We could re-introduce the time limit factor to the auction and tweak it to our preferences.

Ask for any remaining questions before moving on.
