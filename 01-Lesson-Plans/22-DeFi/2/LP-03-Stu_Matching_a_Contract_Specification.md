### 3. Students Do: Practice What the Instructor Just Covered (15 min)

In this activity, students will take a simple smart contract specification, in this particular case the ERC333 example contract specification and implement it.

**Instructions:**

* [README.md](Activities/LP-03-Stu_Matching_a_Contract_Specification/README.md)

**Files:**

* [Solved - CryoptoRight.sol](Activities/LP-03-Stu_Matching_a_Contract_Specification/Solved/CryptoRight.sol)

* [Resources - ICryptoRight.sol](Activities/LP-03-Stu_Matching_a_Contract_Specification/Resources/ICryptoRight.sol)

### 4. Instructor Do: Smart Contract Specifications review (10 min)

Walkthrough the solution and highlight the following:

```Solidity
using Counters for Counters.Counter;

Counters.Counter copyright_ids;

struct Work {
    address owner;
    string uri;
}

mapping(uint => Work) public copyrights;

```

* Our contract makes use of safemath counters to generate the next `copyright_id`.

* We've also defined a custom `struct` named `Work` that contains an `address` of the `owner` of the copyright and the corresponding `uri`.

* A mapping named `copyrights` is used in our contract to map generated `copyright_id`s to their corresponding `Work` info.

```Solidity
event Copyright(uint copyright_id, address owner, string reference_uri);

event OpenSource(uint copyright_id, string reference_uri);

event Transfer(uint copyright_id, address new_owner);
```

* We've also defined the three events defined in our copyright specification `Copyright`, `OpenSource` and `Transfer`.

```Solidity
modifier onlyCopyrightOwner(uint copyright_id) {
    require(copyrights[copyright_id].owner == msg.sender, "You do not have permission to alter this copyright!");
    _;
}
```

* To restrict the `transferCopyrightOwnership` and `renounceCopyrightOwnership` methods so that only the owner of the `copyright_id` given to the function can call it we implemented the `onlyCopyrightOwner` modifier containing a require that compares the given `copyright_id` parameter to the current `msg.sender`.

```Solidity
function copyrightWork(string memory reference_uri) public {
    copyright_ids.increment();
    uint id = copyright_ids.current();

    copyrights[id] = Work(msg.sender, reference_uri);

    emit Copyright(id, msg.sender, reference_uri);
    }

function openSourceWork(string memory reference_uri) public {
    copyright_ids.increment();
    uint id = copyright_ids.current();

    copyrights[id].uri = reference_uri;
    // No need to set address(0) in the copyrights mapping as this is already the default for empty address types

    emit OpenSource(id, reference_uri);
    }
```

* The `copyrightWork` and `openSourceWork` functions were both implemented in a very similar way. Both functions generate a new `copyright_id` by incrementing the `copyright_ids` counter and taking its current value. Where the two functions differ is when it comes to setting the Work's owner's address. Sine open-source works don't have an owner we leave the `owner` attribute set to the default `address(0)`.


```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
    // Re-maps a given copyright_id to a new copyright owner.
    copyrights[copyright_id].owner = new_owner;

    emit Transfer(copyright_id, new_owner);
    }
```

* The `transferCopyrightOwnership` function simply re-maps a given copyright_id to a new copyright owner and emits the `Transfer` event.

```Solidity
function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
    // Re-maps a given copyright_id to the 0x0000000000000000000000000000000000000000
    transferCopyrightOwnership(copyright_id, address(0));

    emit OpenSource(copyright_id, copyrights[copyright_id].uri);
}
```

* The `renounceCopyrightOwnership` simply invokes the `transferCopyrightOwnership` passing it `address(0)` as the new owner.

Ask the class the following review questions.

* Are there any ways that you felt the `CryptoRight` contract code could be improved upon?

* **Potential Answer** Common functionality such as generating copyright_ids could be abstracted to an internal function.

* What are some reasons for using a struct with two attributes instead of as opposed to two mappings for the copyright `owner` and `uri`.

* **Answer** Cheaper gas cost

* **Answer** Less complex code

* After having completed this exercise, can you think of any interesting EIP/ERC specification ideas?
