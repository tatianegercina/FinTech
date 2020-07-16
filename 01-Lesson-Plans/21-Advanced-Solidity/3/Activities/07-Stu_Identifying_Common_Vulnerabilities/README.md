# Identifying Common Vulnerabilities

In this activity, you will apply your knowledge of smart contract best practices to analyze a vulnerable contract and identify various vulnerabilities.

![Computer Bug](../../Images/computer-bug.webp)

## Instructions

1. Open the [ArcadeTokenVulnerable.sol](Unsolved/ArcadeTokenVulnerable.sol) smart contract in [Remix](https://remix.ethereum.org):

2. Identify the three major vulnerabilities within the `ArcadeTokenVulnerable` contract, and make note of each one and where it is present.

   * Integer Overflow

   * Reentrancy Attack

   * Logical errors/lack of propper checks

3. Next go back and fix any issues that the you are able to uncover. Remember that you've learned everything you need to know to fix these common problems.

4. Once you have fixed all of the vulnerabilities present in your smart contract; compile and deploy the new contract onto your local `ganache` network.

### Challenge:

There is another logical bug in the smart contrat that is much harder to spot. Can you find it?
