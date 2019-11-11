### 13. Everyone Do: Using the `hd-wallet-derive` Tool (15 min)

In this activity, you will lead a code along leveraging the `hd-wallet-derive`
command line tool to generate addresses using the same BIP44 scheme as the online tool.

Before starting, ensure that everyone has PHP7 installed on their systems. The quick install guide is located [here]().

Students can check their PHP installation by typing `php -v` in the terminal, which should output version `7.3`.

* Explain to the class that while this tool is written in PHP, we just need it to be installed to run it,
  similarly how Python needs to be installed to run Python programs.

* We will not be writing any PHP ourselves, but rather capturing the output of this tool inside of Python.

First, share the `hd-wallet-derive` tool's [Github page](https://github.com/dan-da/hd-wallet-derive#installation-and-running)
and have them navigate to the `Installation and Running` section.

Have the students copy and paste the `Basics` section, ignoring the Ubuntu requirements (unless the student is running Ubuntu)
into their terminal to clone and install the tool's dependencies.

The commands should be:

```bash
git clone https://github.com/dan-da/hd-wallet-derive
cd hd-wallet-derive
php -r "readfile('https://getcomposer.org/installer');" | php
php composer.phar install
```

Run these commands and install the dependencies. Have the students run the example given once the installation completes.

Ensure that everyone has successfully installed and can run the `hd-wallet-derive` tool from the command line.
Once everyone has successfully installed the tool, have everyone `cd ..` into the directory containing the `hd-wallet-derive` folder.

* Explain that we are going to be working in the directory right above the tool's, so that we don't mix our code with the tool's code.

First, let's create something called a "symlink" -- essentially a shortcut -- to our `hd-wallet-derive.php` script called `derive` to make the command shorter.

Have everyone type:

```bash
ln -s hd-wallet-derive/hd-wallet-derive.php derive
```

Now, instead of calling the program by its full name, like `./hd-wallet-derive/hd-wallet-derive.php`, we can just call `./derive`.

Type the following command into the terminal, explaining each flag:

```bash
./derive -g --mnemonic="INSERT MNEMONIC HERE" --cols=path,address,privkey,pubkey
```

* The `-g` flag tells the tool to "Go" -- this is required to run the tool.

* The `--mnemonic` flag tells the tool which mnemonic to derive from.

* The `--cols` flag tells the tool to print the derivation path, address, and keypair.

You should see output that looks like:

![hd-wallet-derive output](Images/hd-wallet-derive.png)

Point out the derived addresses and compare them to the addresses from the BIP39 online tool.

Have the students type the same command format into their terminals, but replacing the mnemonic phrase with their own.

Challenge the students to try to change the coin type using the `--coin` flag by generating `ETH` keys.

Have the TAs circulate the class and ensure that students are properly generating their keys.
If students are having difficulty importing their mnemonics, make sure they are in double quotes like this: `mnemonic="INSERT HERE"`.

### 14. Instructor Do: `hd-wallet-derive` Review (5 min)

Ask the students the following questions:

* Why would we want to have a CLI version of the online tool?

  **Answer:** We can capture the output and use it in Python.

  **Answer:** We don't always want to use a GUI for things when a command can get the job done quicker.

* What is the point of BIP44?

  **Answer:** We can manage keys from many blockchains using a single master seed.

* What is the derivation path?

  **Answer:** The derivation path is the path along the tree that key is created from, starting at the master key.

* Why might we want to use this tool over others?

  **Answer:** Good documentation.

  **Answer:** Supports many different coins.

  **Answer:** Supports many different wallet standards other than just BIP44.

* What might be a downfall of using this tool over others?

  **Answer:** We have to have PHP installed on our systems, which we might not have control over.

  **Answer:** We are relying on an external tool for the work, versus using a library.
  Having a pure Python library that supported all of the same features would be ideal for us.
