# Creating a Genesis Block

In this activity, you will be using `puppeth` -- a tool bundled with `geth` (the official Ethereum client software)
to create your own genesis block in order to create a new blockchain!

## Instructions

* Open a terminal window and type the following command:

```bash
puppeth
```

This should show the following prompt:

![puppeth](Images/puppeth.png)

* Type in a name for your network, like "puppernet" and hit enter to move forward in the wizard.

* Type `2` to pick the `Configure new genesis` option, then `1` to `Create new genesis from scratch`:

![genesis](Images/puppeth-genesis.png)

Now you have the option to pick a consensus engine (algorithm) to use.

* Type `1` to choose `Proof of Work` and continue.

You will be asked to pre-fund accounts.

* Paste an address from any Ethereum wallet that you control, without the `0x` prefix.

* Once you paste an address and hit enter, hit enter again on the blank `0x` address to continue the prompt.

* Continue with the default option for the prompt that asks to pre-fund "precompile-addresses" by hitting enter again,
  until you reach the `Chain ID` prompt:

![prefunding accounts](Images/puppeth-prefund.png)

* Come up with a number to use as a chain ID, type it, then hit enter.

You should see a success message and be redirected to the
original prompt:

![success](Images/puppeth-success.png)

Great! Your genesis configuration is stored in your local home directory.
We'll export this later. For now, congratulate yourself on creating the rules to your new blockchain network!
