# Scanning Contracts with MythX

In this activity, you will scan the smart contracts you have developed so far with the MythX security tool.

## Instructions

* Activate the MythX plugin in Remix by navigating to the `Plugins` tab, and enabling `MythX`:

  ![MythX Remix](Images/mythx-remix.gif)

  * You do not need to change the credentials in the plugin settings, proceed with the trial mode until you have scanned your contracts.

* Start with the `ArcadeTokenSale` contract that you just built. You should also give this [ArcadeTokenVulnerable](Solved/ArcadeTokenVulnerable.sol) a scan.

* Fix any issues that the tool uncovers, then move on to the other contracts you have built, repeating the process.

* With the time remaining, you can choose to create a [MythX](https://mythx.io) account, and register your credentials with the Remix plugin. Make sure that MetaMask is pointing at the mainnet before registering, as you will use MetaMask to sign a message to register, and it won't work if MetaMask is pointing to `localhost`.
