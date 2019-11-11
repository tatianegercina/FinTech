### 5. Everyone Do: Importing Private Keys into Web3.py (15 min)

Now it's time to import the private key of this address into Web3.py.

First, let's extract the private key from the mnemonic phrases we've been using.

Open up MyCrypto, import the mnemonic, and select the first address:

![mycrypto import mnemonic](Images/mycrypto-import-mnemonic.gif)

Then, click on the dropdown at the top and select "Wallet Info," then click the eye icon
to reveal the private key:

![mycrypto private key](Images/mycrypto-private-key.gif)

Have the students catch up to this point and ensure everyone knows how to extract the private key.

Now, navigate back to your Python editor.

Define the private key in a variable. Your code should look like this at this point:

```python
from web3 import Web3
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")

private_key = "0x31938fae629c2e5f42c7c983dfba11a1b5122d005ba4ab43caaf59ad611bf734"
```

Ask the students:

* Can anyone tell what's wrong with this code so far?

  **Answer**: We have a private key directly in the code! That is a big no-no for security.

* Can anyone guess as to what solutions might exist out here to help us keep private variables more secure?

  **Answer**: Environment Variables!

Great, let's find a way to import this a more secure way.

Create a file called `.env` in the same directory. Have the class follow along.

In this file, define the private key in an environment variable as such:

```bash
PRIVATE_KEY=0x31938fae629c2e5f42c7c983dfba11a1b5122d005ba4ab43caaf59ad611bf734
```

Great! Explain to the class that this `.env` file should **never** be committed to any Git repo, or uploaded to any server. It should stay on your local machine **ALWAYS**.

In fact, we'll add it to a `.gitignore` just in case:

```bash
echo ".env" >> .gitignore
```

Ensure students are complete to this point.

Now, we need to import the key from the environment variable. Replace the `private_key` definition with the following:

```python
private_key = os.environ["PRIVATE_KEY"]
```

Then, `import os` at the top of the file:

```python
import os
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")

private_key = os.getenv("PRIVATE_KEY")

print(private_key)

```

* If we were to run this code, we would print `None`, since the environment variable hasn't actually been loaded into the system.

* We can solve this problem by installing a pip module called `python-dotenv` to do this automatically.

Install `python-dotenv`:

```bash
pip install python-dotenv
```

Then, at the top of our [file](Activities/05-Ins_Importing_Private_Keys/Solved/main.py), we can auto-import the environment variables:

```python
import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

w3.eth.getBalance("0xc3879B456DAA348a16B6524CBC558d2CC984722c")

private_key = os.getenv("PRIVATE_KEY")

print(private_key)

```

Have the students save and run this file. Ensure that the students are successfully printing their keys.

Now we're getting keys loaded in a much more secure way!
Congratulate the students on learning a bit of cyber security on top of all of their FinTech skills.
