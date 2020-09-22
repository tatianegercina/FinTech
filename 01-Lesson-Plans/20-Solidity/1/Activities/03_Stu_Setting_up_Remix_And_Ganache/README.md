# Setting Up Remix and Ganache

In this activity, you will be configuring your development environment for writing and deploying smart contracts on your local development blockchain.

## Instructions

* Install and configure Ganache following the [Unit 20 Installation Guide](../../../Supplemental/unit-20-install-guide.md).

* Once you've completed the setup, take a moment to explore Ganache.

* Next, open the Remix IDE at [remix.ethereum.org](https://remix.ethereum.org) and use your remaining time exploring Remix by performing the following actions:

    * Enable the `Solidity` development environment by clicking on the "Solidity" button on the Remix Home tab.
    ![remix_solidity_env](Images/remix_enable_solidity_env.gif)

    * Create a new smart contract by clicking the Add local file button. Then, populate the contents with [MessageBoard.sol](Resources/MessageBoard.sol).
    ![remix_open_file](Images/remix_open_file.png)

    * The Solidity file's code should appear in the editor window. 
    ![remix_editor_message](Images/remix_editor_message_board.png)

    * Click the Solidity Compiler button on the Remix sidebar then click Compile to compile the contract.
    ![remix_compile_message_board](Images/remix_compile_message_board.png)

    * Now click the Deploy tab on the Remix sidebar. 
    ![remix_deploy_message_board](Images/remix_deploy_message_board.png)

    * Open MetaMask (MetaMask may prompt you to sign-in), then select localhost:8545 from the dropdown menu at the top.
    ![remix_meta_mask_chain](Images/remix_meta_mask_chain.png)

    * Back in Remix, change the Environment to Injected Web3. 
      
        * Once Injected Web3 is selected, it should connect to a Custom network (this is Ganache). 
        
        * When you connect to the Custom network, you may be asked to reload the page and then recompile the contract.

        * Finally, click the deploy button and confirm the transaction in Remix.
    ![Remix Deployment](Images/remix_deploy.gif)

Great job! It may look complicated now, but soon all of these steps will make perfect sense. You'll soon be navigating both Ganache and Remix with ease!

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
