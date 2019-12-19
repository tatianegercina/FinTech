# Creating a Genesis Block

In this activity, you will create your genesis block using `puppeth`, a tool bundled with the Go Ethereum tool.

The genesis block is the first step towards creating your very own new blockchain!

If you have not installed jet the Go Ethereum tool, or you have any issues, please refer to the [Unit 18 Installation Guide](../../../Supplemental/blockchain-install-guide.md) for help.

Recall that by **terminal window**, we refer to the `Terminal` in Mac, or `Git Bash` in Windows.

## Instructions

* Open a terminal window, navigate to the `Blockchain-Tools` folder and type the following command:

 ```bash
 ./puppeth
 ```

* This should show the following prompt:

 ![puppeth](Images/puppeth.png)

* Type in a name for your network, like "puppernet" and hit enter to move forward in the wizard.

* Type `2` to pick the `Configure new genesis` option, then `1` to `Create new genesis from scratch`:

 ![genesis](Images/puppeth-genesis.png)

Now you have the option to pick a consensus engine (algorithm) to use.

* Type `1` to choose `Proof of Work` and continue.

You will be asked to enter a pre-fund account.

* Copy and paste an address from your Ethereum wallet in MyCrypto, without the `0x` prefix.

* Once you paste an address and hit enter, hit enter again on the blank `0x` address to continue the prompt.

* Continue with the default option for the prompt that asks `Should the precompile-addresses (0x1 .. 0xff) be pre-funded with 1 wei?` by hitting enter again,
 until you reach the `Chain ID` prompt.

 ![prefunding accounts](Images/puppeth-prefund.png)

* Come up with a number to use as a chain ID (e.g. `333`) type it, then hit enter.

You should see a success message and redirected to the original prompt:

![success](Images/puppeth-success.png)

Awesome! Your genesis configuration is stored in your local home directory.

We'll export this later. For now, congratulate yourself on creating the rules for your new blockchain network!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
