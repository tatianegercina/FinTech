### 3. Students Do: Activate Ethereum Network (10 min)

Students will now activate their local custom chains they build last unit.

Provide a checklist for the students with the commands necessary to start the chain, as well as a backup chain for students to use if something went wrong with theirs.

**Instructions:**

* [README.md](Activities/03-Stu_Activate_Network/README.md)

**Files:**

* ["puppernet" Backup Blockchain](../../../02-Homework/18-Blockchain/Solutions/puppernet.zip) -- Use this for students that do not have a functioning local blockchain.

### 4. Instructor Do: Review Networks (5 min)

Ask the students a few questions that they might have realized during the homework.

* What does the RPC port allow us to do?

  **Answer**: This exposes this Ethereum APIs needed to talk to our node.

Assure the students that if they don't know the answers to these next questions, it's totally okay:

* What is a `bootnode`?

  **Answer**: A special type of node that facilitates connecting to other nodes. It helps
  new nodes get connected quickly by providing a list of peers to connect to.

* Why can we use a regular node as a `bootnode`?

  **Answer**: A regular node still is connected to other nodes, so it can provide its peer list as well, even though it might not be as large.

Alright, that's enough architecure for now, let's start fetching data from our blockchain!
