### 13. Students Do: Bringing the blockchain to life (15 min)

Students will now launch their own chains using the same techniques.

**Instructions:**

* [README.md](Activities/13-Stu_Starting_Chain/README.md)

Have the TAs circulate and ensure that students are able to start their chains and mine blocks.

If students encounter errors, have them enter the command to clear the chain data without clearing the accounts:

```bash
rm -Rf node1/geth node2/geth
```

### 14. Instructor Do: Ensuring Block Production (15 min)

Take this time to ensure that every student is successfully mining blocks.

Ensure that:

* The `--mining` flag is set on the first node.

* The `--minerthreads` flag is set to at least 1 on the first node.

* The `enode://` address of the **first** node is copied into the **second** node's `--bootnodes` flag in quotes.

* The firewall of the student's machine is allowing `geth` to bind to the proper ports.

* The `--port` on the second node is set to something different from the first.
  The default sync port is `30303`, so recommend `30304` for the second node.

* The `--rpc` flag is enabled on the second node. This will be necessary to connect MyCrypto to the blockchain in the next activity.
