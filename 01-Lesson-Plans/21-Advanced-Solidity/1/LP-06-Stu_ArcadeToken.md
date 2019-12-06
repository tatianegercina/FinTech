### 6. Students Do: Building an Arcade Token with Mappings (20 min)

In this activity, students will practice using the `mapping` data structure by building an ArcadeToken.

Send out the instructions and the starter code below, and have the TAs circulate the class.

**Instructions:**

* [README.md](Activities/06-Stu_ArcadeToken/README.md)

**Files:**

* [ArcadeToken.sol](Activities/06-Stu_ArcadeToken/Unsolved/ArcadeToken.sol)

Ensure that students are using the mapping to map `address` to `uint` specifically.

If students are confused about how the `exchange_rate` works, remind them:

* By multiplying the `exchange_rate` with the `msg.value`, you are effectively multiplying the amount of `wei`, the smallest denomination of Ether, which is stored in a `uint`. We will learn how to calculate Ether values later this week, but operating on `wei` gives absolute precision.

For students that are confused about `mapping`:

* Mapping simply associates one data type to another. By pairing `address` to `uint`, we can track balances.

  * For example, `0xc3879B456DAA348a16B6524CBC558d2CC984722c => 333` is what the data might look like in contract storage.

---

### 7. Instructor Do: ArcadeToken Review (10 min)

**Files:**

* [ArcadeToken.sol](Activities/06-Stu_ArcadeToken/Solved/ArcadeToken.sol)

Open the solution and explain the following:

* By setting our mapping to `mapping(address => uint) balances` we are able to track address balances by setting the `uint` that is paired to any address.

* Since all types are set to `0` by default, we don't need to worry about initializing any balances. We can simply set them as people use the token.

* We can access our balance from the `balances` function by returning `balances[msg.sender]`. This is a very similar format to how we would access a dictionary in Python.

* In our `transfer` function, we simply subtract the value from the sender's balance in the `balances mapping` and add it to the recipient's.

* By setting an `exchange_rate`, we can reward/create tokens based on how much `wei` is sent to the `purchase` function, and then collect the Ether for ourselves, automatically!

* In our `mint` function, we restrict the function to only allow ourselves (the `owner`) to create new tokens when we need to.

Ask for any remaining questions before moving on.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to the class. Allow them to settle in while asking a few recall questions:

* What is a `mapping`?

  * **Answer:** A pair of types.

* Why do we use it in our token?

  * **Answer:** It allows us to map `address` to `uint`, so we can set balances associated with addresses.

* What is the limit for how much we can store in a `mapping`?

  * **Answer:** There is no set cap, but we are limited by gas prices and gas limits of the current state of the blockchain network.

Get the students excited about the next activity by explaining how we are now going to secure our tokens from a vulnerability that allows users to spend tokens they don't have!
