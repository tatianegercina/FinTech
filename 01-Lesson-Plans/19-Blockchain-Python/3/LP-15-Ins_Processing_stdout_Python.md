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
