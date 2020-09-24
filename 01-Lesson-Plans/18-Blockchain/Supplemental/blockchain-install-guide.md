# Blockchain Installation Guide

In this Unit, you will use some software tools and utilities to interact with blockchains and to create your very own blockchain from scratch.

Please complete the instructions in this guide so you can follow all the activities and homework assignments in Unit 18.

**Important Note:** Windows users **MUST** use `git-bash` and not the default Windows command prompt when you are requested to open the terminal window to execute commands.

## Installing MyCrypto Desktop App

[MyCrypto](https://www.mycrypto.com/) is a free, open-source, client-side interface that allows you to interact directly with the blockchain.

For this Unit, we will use MyCrypto Desktop App to manage ethereum wallets and make transactions on the blockchain.

To install MyCrypto Desktop App, please follow the next steps:

1. Open your browser and navigate to the downloads page at https://download.mycrypto.com/.

 ![MyCrypto installation - step 1](Images/mycrypto-1.png)

2. Depending on your operating system, you will be redirected to the corresponding application installer. If you are not correctly redirected, choose the appropriate installer for your operating system.

3. Once you download the installer, open the file, and follow the installation wizard. You will start using this application on Day 1.

### MyCrypto Installation Notes

General Notes:

* The first time you execute MyCrypto, you will see the following starting tutorial, we suggest you read through it as you click "Next" to continue.

 ![MyCrypto installation - step 2](Images/mycrypto-2.gif)

Running in OS X:

* The first time you execute MyCrypto, you will see the following warning message. You can safely click on the "Open" button to start the application.

 ![OS X Warning](Images/mycrypto-mac-wanrning.png)

### Allowing Permission to Open Apps from Unidentified Developers

When an app is not registered with Apple, it can be automatically blocked by the Mac OS operating system when attempting to open the "unidentified" application. Therefore, in order to allow the use of the MyCrypto app, you may need to allow it as an exception to your Mac OS security preferences. To do so perform the following.

1. Open the MyCrypto app, it should produce a warning error saying that you cannot open the application due to security reasons. Therefore, we'll need to make a security exception for it.

2. Look to the top-left of the screen, click on the Apple Logo and navigate to System Preferences > Security & Privacy.

    ![system-preferences](Images/system-preferences.png)

3. Click on the General tab and allow your MyCrypto application security access to be opened in the "Allow Apps Downloaded From" section. Your screen should look similar to the image below.

    ![catalina-allow-unidentified-app](Images/catalina-allow-unidentified-app.jpg)

## Installing Go Ethereum Tools

[Go Ethereum](https://geth.ethereum.org/) is one of the three original implementations of the Ethereum protocol. It is written in Go, fully open-source and licensed under the GNU LGPL v3.

In this Unit, we will use Go Ethereum Tools to create our very own blockchain, from the genesis block to mining tokens and making transactions.

Though there are installers for OS X and Windows, we will use the application executable binary files to have a seamless experience between both operating systems and to avoid some technical issues that currently exist in Windows.

To install the Go Ethereum Tools, please follow the next steps:

1. Open your browser and navigate to the Go Ethereum Tools download page at https://geth.ethereum.org/downloads/

2. Scroll down to the "Stable Releases" section and proceed depending on your operating system.

    * Installing on OS X: 
    Click on the **"Geth & Tools 1.9.7"** to download the applications bundle archive.
    ![Installing Geth - 1](Images/geth-1.gif)

    * Installing on Windows:
        * *NOTE:* You need to know if you are running a `32 bit` or `64 bit` version of Microsoft Windows, if you are not sure about that, you can check your version following [these steps](https://support.microsoft.com/en-us/help/13443/windows-which-version-am-i-running)):

       * Depending on your Windows version, you should download the `32 bit` or `64 bit` version of the Go Ethereum Tools.
    ![Installing Geth - 2](Images/geth-2.gif)
    

3. After downloading the tools archive, open your "Downloads" folder, and you will find a file named `geth-alltools-darwin-amd64-1.9.7-a718daa6.tar.gz` in OS X, and a file called `geth-alltools-windows-amd64-1.9.7-a718daa6.zip` in Windows. Note that the last numbers in the filename could vary depending on the last build available.

4. Decompress the archive in the location of your preference on your computer's hard drive, and rename the containing folder as `Blockchain-Tools`. We recommend using a location that can be easily accessed from the terminal window like the user's home directory.

 ![Installing Geth - 3](Images/geth-3.png)

5. You have finished the installation process; you will use these tools to create your very own blockchain!

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
