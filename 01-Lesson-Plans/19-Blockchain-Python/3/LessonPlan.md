## 19.3 Lesson Plan: Wallet Standards (BIP39, BIP32, and BIP44)

### Overview

Today's class students will learn how BIP44 works in preparation for the homework.

The goal of today's class is for the students to understand how to talk to Ethereum and Bitcoin nodes using Python,
and to understand how wallets work across the blockchain ecosystem.

### Class Objectives

* By the end of the unit, students will be able to:

* Explain that BIP32 generates a tree of keys from a single "master key" 256bit seed, and why it is used (increased privacy, merchants, etc).

* Explain that BIP39 allows you to back up this master key as a set of words (mnemonic phrase).

* Explain that BIP44 allows you to use your master key with multiple coins (blockchains).

* Use `hd-wallet-derive` (BIP44 wallet) to generate BIP44 keys using their own mnemonic.

* Discuss the differences in wallet implementations and the pros and cons (cold -> hot, paper/hardware -> software).

* Integrate basic terminal output (stdout) into Python code.

- - -

### Instructor Notes

* Ensure that you have your 12 word mnemonic ready. We will be using it throughout the class.

* Take some time before class to familiarize yourself with the [BIP39 online wallet converter](https://iancoleman.io/bip39/) and how to convert your mnemonic into different coins.

* Ensure that you have properly installed the [hd-wallet-derive](https://github.com/dan-da/hd-wallet-derive#installation-and-running) PHP CLI tool at least once before class.

- - -

### Class Slides and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides]().

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting "Make a copy...".

* The time tracker for this lesson can be viewed here: [Time Tracker](TimeTracker.xlsx).

- - -

### 1. Instructor Do: Welcome Class (5 min)

Welcome students back and refresh a bit on some blockchain wallet architecture.

Open the slides, cover the agenda for the day, then navigate to the beginning of the slideshow.

Ask the students the following questions:

* What is a UTXO?

  **Answer:** Unspent Transaction Output

* What is a private key in the context of blockchain?

  **Answer:** A key that allows you to sign transactions.

* What is a wallet?

  **Answer:** A piece of software that manages your private keys and allows you to sign and send transactions.

Explain to the class that there are two parts of a wallet.

Ask the students to make an educated guess as to what the two main parts are.

Then, explain that the two parts of a wallet is:

* **Key Manager** -- Code that takes your mnemonic or private key and converts it to the proper blockchain address format.
  This is the low-level cryptographic library.

* **Blockchain Node Connectors** -- Code that connects to the blockchains that the wallet supports.
  This is the library that connects the wallet to live blockchain nodes, where signed transactions from the key manager are sent to the network.

Remind the class that we have already worked with several wallets already, that contain both of these parts.

Ask the class to name a few, such as:

  **Answer:** MyCrypto

  **Answer:** Web3.py

  **Answer:** Bit

Elaborate:

* Notice how we have used the same 12 word mnemonic phrase across each blockchain?

* While this is incredibly useful, wouldn't it be easier to have one library that works with both Ethereum, Bitcoin, and potentially others?

* Today we will learn the wallet standards that allow us to use the same master key across multiple blockchains,
  as well as how to integrate a universal key manager tool with Web3.py and Bit using our good pal, Python.

  This will allow us to have one Python wallet that supports both of the blockchains we've learned so far, so that we no longer
  have to use separate tools to send transactions!

### 2. Instructor Do: Intro to BIP39 (Mnemonic Phrases) (10 min)

First, let's begin to explain how these wallets work.

* Explain to the class that just like how the blockchain community comes up with standards for how the chains are designed,
  standards for how crypto wallets work are also agreed upon!

* This is why we are able to use the same 12 word mnemonic phrase across Bitcoin and Ethereum.
  In fact, we can use it across many more blockchains than that!

Now, let's talk about how these mnemonic phrases we've been using.

* So far, we've been using English words as our crypto keys. How might this be possible?

* This is possible because of something called the BIP39 Standard.

* "BIP" means "Bitcoin Improvement Proposal" and in this case, BIP39 helps more than just Bitcoin.

* This standard comes up with exact lists of 2048 words per language like English, Spanish, Japanese, etc.
  as well as a formula that allows you to take a set of those words and generate private keys with them.

* That way, instead of having to remember your private key (which is a long and confusing alphanumeric string),
  or worrying about writing it down correctly, you can remember the exact words that generate the master key/master seed instead,
  and securely convert back and forth from seed to mnemonic phrase.

Now, open up IanColeman's BIP39 online tool [here](https://iancoleman.io/bip39/).

Tell the students to ignore most of the things you see here for now, and pay attention to a couple fields first.

Paste your Instructor Mnemonic into the `BIP39 Mnemonic` field to allow the tool to derive addressess:

![mnemonic conversion](Images/mnemonic-convert.png)

Point out the `BIP39 Seed` field that is generated.

* Explain to the class that this is the "master seed" or "master key" that can be used to derive any of the rest of the keys we'd need/want to use.

* The mnemonic phrase is converted from our English language back to the random numbers
  and letters that make up crypto keys. Great! Can you imagine having to write down the
  master seed instead of just the words?

Now, it's time to have the class convert their mnemonics to a master seed.

### 3. Students Do: Converting Mnemonic to Seed (10 min)

In this activity, students will download a local copy of the BIP39 online tool
and paste their mnemonics into it to convert to a master seed.

**Instructions:**

* [README.md](Activities/03-Stu_Converting_Mnemonic.md/README.md)

Have TAs circulate and ensure that students are able to convert their mnemonics successfully by verifying the `BIP39 Seed`
segment is generated from the `BIP39 Mnemonic` segment.

### 4. Instructor Do: Review BIP39 (5 min)

Ask the students the following questions:

* Why is BIP39 important?

  **Answer:** It allows people to remember and write down a much more human-friendly version of the key.

* What sort of mistakes do human readable keys prevent?

  **Answer:** Incorrectly writing down the private key string.

* Why did we download the offline version of the BIP39 tool?

  **Answer:** It is more secure, since the online version can still get hacked.
  It is safer to download the open source code straight from Github and run it locally.

### 5. Instructor Do: Back to BIP32 (10 min)

Now let's actually generate some Bitcoin keys from this!

Back in the BIP39 tool, scroll down to the `Derivation Path` section and click the `BIP32` tab.

![BIP32](Images/bip32-tab.png)

Explain to the students:

* The BIP32 standard allows us to "derive" a tree of new Bitcoin keys from the master seed. BIP32 compatible wallets are also called HD wallets.

* This means that we can generate many addresses from a single seed, without having to create new wallets constantly and having to track their private keys.

Scroll down to the list of derived addresses:

![BIP32 Derivation](Images/bip32-derived.png)

Point out the `Path` column on the left. Explain to the students:

* This is the "derivation path" that is applied to the master seed. By applying this path to the master seed,
  the address and public/private keypair to the right is generated.

* By incrementing the derivation path by 1, you can generate a new address and keypair.

Ask the students:

* Why is this useful?

Allow them to answer, then explain:

* Since Bitcoin is UTXO native, we can generate a new address for every transaction.
  This allows us to make the accounting very easy.

* Because we own all of the keys anyway, we can sign the UTXOs that belong to each of the "child" keys and spend from them all simultaneously.

* Let's say you were a merchant selling goods. For every customer purchase, you can increment the path by 1 and generate a new address for that customer to pay you through.

Ask the students:

* Why might you want to do that?

  **Answer:** That way customers can't see your entire balance and purchase history!

  **Answer:** Accounting becomes much easier, as each address becomes a receipt of sorts containing that transaction only.

  **Answer:** Bitcoin is pseudonymous, not anonymous, so generating new addresses helps preserve privacy.

Now, time for the students to derive some keys of their own!

### 6. Students Do: Deriving BIP32 Keys (HD Wallets) (10 min)

Have the students derive some Bitcoin keys and check their addresses.
They should all have empty balances, as we are generating mainnet Bitcoin keys, not the testnet keys used earlier this week.

**Instructions:**

* [README.md](Activities/01-Stu_BIP32_Derivation/README.md)

Have the TAs circulate and ensure that students are deriving the proper BIP32 keys.

### 7. Instructor Do: Review BIP32 (5 min)

Ask the students:

* Why is BIP32 useful?

  **Answer:** Since Bitcoin is UTXO native, we can generate a new address for every transaction.

  **Answer:** Allows for better and easier accounting on the blockchain.

  **Answer:** Preserves privacy by using new addresses for receiving money.

* What do you notice about the balance on these addresses?

  **Answer:** They are empty, and not the same as we used last week.

* Why are these addresses different from those we used last week?

  **Answer:** These are mainnet keys, which are different from Bitcoin's testnet keys.

Explain to the students that we will learn how to generate keys for different coins,
including Bitcoin Testnet and Ethereum in this next activity.

### 8. Instructor Do: Multi-Coin Wallets with BIP44 (10 min)

In this activity, you will demonstrate the multi-coin functionality of BIP44 and how it has become the "universal wallet" standard.

* Now that we can generate a tree of keys from a single master seed, wouldn't it be awesome to be able to use the same
  master seed for multiple coins as well?

* The BIP44 standard is what allows us to do just that! BIP44 is the standard that most "Universal Wallets" or "Multi-Coin Wallets"
  leverage. This is also the standard that exchanges use to generate your crypto addresses and keep track of customer balances and transactions.

Scroll back to the `Derivation Path` section in the BIP39 tool, then click the `BIP44` tab:

![BIP44](Images/bip44-tab.png)

Scroll down to the list of keys like before.

Point out:

* While these are all different keys than from BIP32, they are still mainnet Bitcoin keys.

* Let's change that by creating some testnet Bitcoin keys.

* The `Coin` number listed is `0` in the derivation path, as well as the `Coin` field under the `Purpose`.

Scroll up to the top, and change the `Coin` dropdown from Bitcoin to Bitcoin Testnet:

![BTC Testnet BIP44](Images/bip44-btc-testnet.png)

Navigate back down to the derived addresses. You should now see the same testnet keys we used earlier this week.

* Notice that the `Coin` number changed from `0` to `1` -- Bitcoin's mainnet is coin 0 and the BTC testnet is coin 1!

* Now, let's generate some Ethereum keys!

Scroll back up to the `Coin` dropdown and select `ETH - Ethereum` .

Back down at the derived addresses section, you should see a list of Ethereum addresses:

![ETH BIP44](Images/bip44-eth-derived.png)

Notice these are the same as used throughout class as well!

Point out:

* The derivation path now uses `60` as the coin number. This means that Ethereum was assigned coin number 60 in the standard.

* Since Ethereum uses the same addresses across main and test networks, these should be the same keys that we've been using since we started learning about blockchain!

Explain to the students that they may be wondering where the list of coins and their corresponding coin numbers come from, and how you might add yours in the future.

Navigate to the [SLIP44](https://github.com/satoshilabs/slips/blob/master/slip-0044.md) spec page.

Explain to the students that this is the sister-standard that contains the list of coin numbers and their corresponding blockchain.

![SLIP44](Images/slip44.png)

* This contains the data needed to get a coin registered onto this standard.
  New blockchains need to have a PR opened on this SLIP44 standard and other wallets will use this list for integration.

That was quite a lot, let's have the students get some practice generating keys for multiple coins!

### 9. Students Do: Deriving Multiple Coins with BIP44 (10 min)

Now it's time for the students to derive multiple coins from their mnemonics.

**Instructions:**

* [README.md](Activities/02-Stu_BIP44_Derivation/README.md)

Have the TAs circulate and ensure that students are generating BTC testnet and Ethereum keys, and that they match those that they used previously in the course.

### 10. Instructor Do: Review BIP44 (5 min)

Ask the students:

* Why is BIP44 useful?

  **Answer:** It allows you to use one master key across multiple blockchains!

  **Answer:** It still supports multiple addresses like BIP32.

  **Answer:** It allows the rest of the crypto and blockchain community to be more interoperable.

* Would an exchange or an innovative bank use BIP44? Why?

  **Answer:** Yes, it would use it to keep track of customer's keys across multiple blockchains.

* Where does the list of coin types come from?

  **Answer:** BIP44's sister standard, SLIP44.

Congratulate the students on learning about the wallet standards that the entire crypto community has settled upon using!

Explain that they can now take this understanding anywhere in the blockchain space, and
that all blockchains have an incentive to integrate with this universal standard.

- - -

### 11. BREAK (15 min)

- - -

### 12. Instructor Do: Welcome Back to Class (5 min)

Welcome the students back to class and ask a few recall questions:

* What is BIP39?

  **Answer:** The standard that allows us to convert mnemonics to master keys.

* What is BIP32?

  **Answer:** The standard that allows us to generate a tree of keys from the master seed.

* What is BIP44?

  **Answer:** The standard that allows us to generate trees of keys for multiple coins, all from the original master seed!

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

### 15. Everyone Do: Processing Terminal Output in Python (10 min)

Now it's time to show the class how to process the terminal output in Python by leading a code-along.

* We are now going to call this CLI tool from within Python, and capture some of its output.

First, have everyone open a new Python file called `wallet.py`:

Type the following:

```python
import subprocess

command = ''
```

* The subprocess module allows us to call other processes, such as CLI tools, from within our Python process.

* We are using single quotes since our command has double quotes in it. We can later use more advanced string formatting.

Wait for everyone to catch up, and then have everyone paste the command that they used in the terminal
inside of the command string:

```python
import subprocess

command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey'
```

Then, we will actually call the command from python with this:

```python
import subprocess

command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

print(output)
```

Have everyone copy this down, and explain:

* While we don't need to know every detail of this command, we are essentially telling the subprocess module to call this command through a system "pipe" and telling it that the program is interactive with the `shell=True` flag.

* "stdout" means "standard output" -- aka the output that programs return to the operating system to print. When you run "print" in Python, it pipes the string to `stdout`.

* The next line captures the output and the error from the process.

* Then, we wait for the process to finish and capture the status code. We don't need to use the status yet, but we do need to wait for the process to finish.

* Then we print out the result.

Once everyone has successfully copied and run this program, ask the following questions:

* What do you notice about the output, particularly the format?

  **Answer:** It is not formatted very nicely, or in a way we can process this easily.

* What would be another format that would be easier to work with in this case?

  **Answer:** JSON or CSV format.

Great! Let's tell the derivation tool to give us output in JSON format. We can do this by adding the `--format=json` flag to the command string:

```python
command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'
```

Awesome! Now challenge the class what Python module and function we might want to use for this.

When they have provided their answers, reveal that we can `import json` and use `json.loads` to convert a the JSON string output to a JSON object!

Add the `json.loads` function to convert the output:

```python
import subprocess
import json

command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
```

Ensure the students are caught up and are printing their keys in JSON format. You can challenge them to `pprint` it as well.

Much better, right? Now that we have the keys in an object, we can access the address of the first key like so:

```python
print(keys[0]['address'])
```

* Amazing! Now we are able to work with many different keys across different blockchains. Look forward for this week's homework, where you'll be expanding this to support transacting on ETH and BTC testnets!

### 16. Instructor Do: Capturing `stdout` Review (5 min)

Ask the students:

* What might we use this for?

  **Answer:** We can build a universal wallet with this!

  **Answer:** We can build payment gateways with this!

  **Answer:** We can integrate crypto into many different systems!

* What is `stdout`?

  **Answer:** The standard output that programs can print to.

* What is the more ideal and secure way of managing our mnemonic in our Python code?

  **Answer:** Environment variables.

* What could we use to pass different arguments to the command with? (Think strings)

  **Answer:** We can use "f" strings or complex string formatting to customize the output we want.

### 17. Instructor Do: Wallets vs Wallets (15 min)

In this activity you will return to the slideshow for visual assistance.

Now it's time to explain to the students some critical differences in the security models of different wallets.

Ask the students:

* Have any of you ever heard the term "hardware wallet" before?

* Have any of you heard the term "hot" or "cold" wallets before?

* Let's clarify a bit on what these mean.

Continue through the slideshow until:

![hardware wallet](https://image.shutterstock.com/image-photo/cryptocurrency-hardware-wallet-on-laptop-600w-1114321721.jpg)

* This is a hardware wallet. It looks like a USB drive right? Instead of storing files, what this device does is store your private keys. It can also sign transactions with those keys.

* Does anyone know why this is more secure than using our mnemonics like we have been?

  **Answer:** The hardware wallet never outputs the private keys once they are generated the first time.

* Essentially what this means is that this device will give you one, and only one opportunity to write down your mnemonic phrase.
  After that, the device will never output the private keys again. You can only use it to restore or generate a mnemonic.

* You are effectively asking the device to sign a transaction that you send to it over USB.
  Then, using the physical buttons on the device, you enter a PIN and confirm the details.

* Even if you lose the device, or it is stolen, your private keys are safe. If you get the PIN wrong too many times, it'll erase itself.
  Only the person that knows the PIN can spend the funds, and they won't be able to get the device to print out the keys either.

Now ask the students:

* If hardware wallets are so secure, why would we ever use anything else?

  **Answer:** Security is a spectrum.

Elaborate that a software wallet on your phone or laptop is like carrying physical cash with you, you only want to carry so much.

* It's really easy to pull cash out of your wallet, but it also carries some risk.

* A hardware wallet is more like a sealed bank vault, or an ATM.
  You're protected by a lot more security measures, but it's not always as convenient.
  Imagine being in line at the store, pulling out a hardware wallet, plugging it into your phone, opening the companion app,
  confirming the transaction details, then entering your PIN on the hardware wallet.
  That would take forever, and probably be a bit embarrasing!
  In this case, storing a bit of crypto in a software wallet app on your phone is much easier, and you can refill it when convenient.

Ask the students:

* Can anyone guess as to why software wallets aren't as secure as a hardware wallet?

  **Answer:** Computers and phones get hacked all the time!

Explain to the class:

* Since software wallets have to store the private keys in the devices memory, or RAM, there is a potential for malicious programs
  to steal it. If your operating system is compromised, so is all of the data it stores, including your private keys.

So what's this talk about "hot" vs "cold" wallets?

* When we refer to hot vs cold, we are referring to generally how often the wallet is accessed.

* "Hot" wallets tend to be live and ready to spend funds, and much easier to access.

* "Cold" wallets tend to store larger funds and are accessed less frequently, more like a vault.

Ask the students:

* So what would a "hot" wallet be in this case? Software or hardware?

  **Answer:** Software wallets are hot wallets.

* What would be a "cold" wallet?

  **Answer:** Hardware wallets.

Congratulations! Now you understand the different wallet standards, the different implementations of these wallets in hardware
and software, and when to use each!

### 18. Students Do: "If I Were an Exchange" Thought Experiment (15 min)

In this activity, students will break into small groups and design an exchange given the different wallet standards
and software/hardware implementations.

**Instructions:**

* [README.md](Activities/04-Stu_If_I_Were_Exchange/README.md)

Have TAs circulate and ask questions about the students exchange designs, including what type of wallets they'd use
and how they manage the funds.

### 19. Instructor Do: Exchange Design Review (10 min)

While each group of students may have slightly different designs, generally the centralize exchanges use similar implementations.

Have the students present their designs, picking a group leader to describe the architecture to the class.

Ask the students the following questions:

* What type of wallet would be the best for an exchange to use?

  **Answer:** Hardware wallet

* Should you keep all of the funds available to spend or should you keep a percentage offline?

  **Answer:** You should store most of the funds offline, then when customers withdraw, do the withdraws in bulk.

* How might a decentralized exchange work differently?

  **Answer:** The exchange wouldn't need to hold any keys or funds, but would purely facilitate direct peer to peer trades.

* What is the advantage to a centralized exchange?

  **Answer:** Easy onboarding, you can hold the company liable.

  **Answer:** Potentially higher liquidity, and leverage options. More advanced services may be provided.

* What are some disadvantages to centralized exchanges?

  **Answer:** If the exchange gets hacked, the crypto is gone for good. This can sink the exchange.

  **Answer:** Customers don't own or manage the private keys being used, which means the exchange has control over the funds.

* What wallet standards have we learned?

  **Answer:** BIP39, BIP32, and BIP44

### 20. Instructor Do: Structured Review (35 mins)

**Note:** If you are teaching this Lesson on a weeknight, please save this 35 minute review for the next Saturday class.

Please use the entire time to review questions with the students before officially ending class.

Suggested Format:

* Ask students for specific activities to revisit.

* Revisit key activities for the homework.

* Allow students to start the homework with extra TA support.

Take your time on these questions! This is a great time to reinforce concepts and address misunderstandings

- - -

### End Class

- - -

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
