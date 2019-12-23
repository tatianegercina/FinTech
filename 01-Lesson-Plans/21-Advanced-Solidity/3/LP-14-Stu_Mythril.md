### 14. Students Do: Scanning Contracts with MythX (15 min)

In this activity, students will spend the time scanning the contracts they have built so far in class, starting with the `ArcadeTokenSale` they just built.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/14-Stu_Scanning_with_MythX/README.md)

**Files:**

* [ArcadeTokenVulnerable.sol](Activities/14-Stu_Scanning_with_MythX/Solved/ArcadeTokenVulnerable.sol)

Ensure that students are scanning their contracts with MythX properly.

If the students are having difficulties, try the following:

* Remove and re-add the MythX plugin in Remix. Hard refresh or clear cookies to reset any cobbled state.

* If the trial does not work properly, register an account at [MythX.io](https://mythx.io) while MetaMask is pointing to the mainnet, then save the credentials in the MythX plugin while in mainnet. Then, MetaMask can be switched back over. This process should take about 2-3 minutes.

### 15. Instructor Do: Review MythX (5 min)

Now that students have scanned their contracts, ask them the following questions:

* What was the most common vulnerability that kept popping up?

  **Answer:** Floating pragma version, state variable visibility not being set, etc.

* After fixing our vulnerabilities, are our contracts "hack-proof?"

  **Answer:** We cannot guarantee that they are hack proof, but we still performed due diligence.

  **Answer:** There may be a bug in our logic that the tool cannot pick up, so we should still have a 3rd party security team test and audit these contracts before deploying to production/mainnet.

Now that students have scanned and fixed their contracts, it's time for them to dive a bit deeper into some common vulnerabilities.
