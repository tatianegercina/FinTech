## 22.2 Lesson Plan: dApp Deployment

### Overview

In today's class, students will be introduced to the thought process and techniques that go into taking a formalized contract spec and implementing it into solidity code. Throughout the process of software development, employees are often required to collaborate with one another creating a separation of concerns within a system's architecture. Students will learn to take a simple yet more formalized smart contract specification and implement it to fit the interface of an already established frontend dApp. Students will then deploy the configured dApp to a centralized production environment, Github pages.

Students will use the remainder of class to work on their projects.

---

### Class Objectives

By the end of the unit, students will be able to:

* Implement a given smart contract specification into real solidity code.

* Integrate the contract with a JavaScript/HTML/CSS frontend.

* Deploy a bundled dApp to Github Pages

* Customize and deploy a landing page for projects on Github Pages

---

### Instructor Notes

* Refer to the `IPFS` documentation for further information about [IPFS Docs](https://docs.ipfs.io/)

---

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1devzesQ1UKT2weYAz43Ei9YBIM863dYDtw9IFIMfLis/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome to Class (10 min)

During the previous lecture students were introduced to the concept of DeFi (short for decentralized finance). Students were given the scope that many of the concepts that they had learned up to this point can be leveraged to build financial systems based off of the principals of DeFi as well as given the tools that directly enable these systems through the deployment of dApps such as solidity events and IPFS. Briefly review the following talking points to refresh the class on DeFi,events, and IPFS.

* What are some benefits of solidity events?

  * **Answer** They are a cheap amount of gas.

  * **Answer** They allow you to keep a log of information on-chain.

  * **Answer** Events are MUCH cheaper than contract storage

  * **Answer** Events are solidity's built-in way to interact with something external, such as a user interface.

* What are some potential issues that IPFS seeks to solve?

  * **Answer** Inefficiencies in the web such as `duplicate files`.

  * **Answer** Inefficiencies in the web such as having to route to a faraway server to get the file you need when it might be right next door.

  * **Answer** Problems with security and file integrity, such as not knowing whether or not files you have accessed over the web have changed.

  * **Answer** Problems with the security of centralized servers providing a centralized attack vector.

### 2. Instructor Do: Building to a Smart Contract Specification (15 min)

The instructor will discuss the process of breaking down the elements of a smart contract specification, such as it's interface, and how to turn it into functioning code. The EIP provides an example interface file for testing the contract linked below.

**Files:**

* [Solved - CryptoRight.sol](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Solved/CryptoRight.sol)

* [ICryptoRight.sol](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ICryptoRight.sol)

* [Example CryptoRight EIP](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md)

Begin by opening the [Example CryptoRight EIP](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md) and displaying it for the class.

* In earlier classes we took a look at a variety of the EIP specifications located on [https://eips.ethereum.org/EIPS](https://eips.ethereum.org/EIPS)

* Today we will take a new example EIP, break it down and translate it into functioning code.

* Let's begin by identifying the goal of the current contract This will allow us to gain scope on the logic that we will be implementing.

* A good way to identify the goal of a given contract specification is by reading the `Simple Summary`, `Abstract` and `Motivation`.

Together with the class read the `Simple Summary`, `Abstract` and `Motivation` sections of the EIP.

Open [Remix](https:://remix.ethereum.org/) in your web browser and create two new contracts the first-named `ICryptoRight.sol`  and the second named `CryptoRight.sol`.

Inside `ICryptoRight.sol` paste the contents of [ICryptoRight.sol](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ICryptoRight.sol) from the resources folder.

Inside `CryptoRight.sol` define a new contract named `CryptoRight` that extends the `ICryptoRight` interface.

```Solidity
pragma solidity ^0.5.0;

import "./ICryptoRight.sol";

contract CryptoRight is ICryptoRight {
}
```

Next, pull up remix side by side with the [Example CryptoRight EIP](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md) and go through each method definition/description inside the specification section of the EIP document while scaffolding out each function with the class in realtime.

* Now that we've familiarized ourselves with the goal of the example ERC333 copyright contract lets define the structure of our contract and scaffold out each function's business logic.

* When writing code to a particular specification it can be very helpful to write comments for each step that must be performed inside a function's body. In this activity, we will take the contract specification and break down each of the method's business logic and backing data structures into descriptive comments.

Read aloud the `copyrights` method's interface definition and description.

* copyrights

* Accepts a given `copyright_id` as a `uint` and returns a `mapped struct` containing the copyright's `owner` and `uri`.

Highlight the CryptoRight contract interface definition.

```Solidity
function copyrights(uint copyright_id) public returns(IWork memory);
```

* The ERC333 spec defines this interface for the copyrights method.

Now demonstrate what this looks like implemented inside the smart contract.

```Solidity
mapping(uint => Work) public copyrights;
```

  * The details of the method were "Accepts a given `copyright_id` as a `uint` and returns a `mapped string`".
  * This translates to a `mapping` of a `uint` and a `Work` datatype.

  * Pay particular attention to the wording  "as a `uint` and returns a `mapped string`, this can be translated to "a `uint` mapped to a `string`", eg, a mapping.

  * Remember that a variable defined with the public modifier automatically generates a getter function with defined parameters. In this case, our publically defined mapping `copyrights` generates a getter function that accepts a `uint` and returns a `Work` struct.

  * This is a great example of how a specification's defined interface may not always exactly match what the actual code will look like but rather the interface that will be generated. `Interface` being both a defined function and the concept of what input/output for a given `API` is expected to be present.

Inside the CryptoRight contract under the `copyright_ids` coutner create a new `struct` named `Work`. Inside this `struct` create an `address` attribute named `owner` and a `string` attribute named `uri`.

  ```Solidity
  struct Work {
      address owner;
      string uri;
  }
  ```

* We've created our map that reference's a custom datatype named `Work`, but now we have to define that datatype with a `struct`.

* According to the `copyrights` method's spec we need a "`struct` containing the copyright's `owner` and `uri`".

Read aloud the `copyrightWork` method interface definition and description.

* copyrightWork

  ```Solidity
  function copyrightWork(string memory reference_uri) public
  ```

  * The ERC333 spec defines this interface for the `copyrightWork` method.

Add the `copyrightWork` function to the contract.

  ```Solidity
  function copyrightWork(string memory reference_uri) public {
  }
  ```

  * This translates to a function definition that looks like this inside the smart contract.

* Now let's focus on the function's description and break it down into comments about what steps must take place inside the function.

Highlight the `copyrightWork` method's description.

* Generates a new `copyright_id` of type `uint` and maps it to a `Work struct` containing the given copyright `owner` and `uri`.

Add the imports for `SafeMath counters` under the `pragma` and bind the `counter library` to the `Counter` datatype below the contract definition.

```Solidity
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/drafts/Counters.sol";
import "./ICryptoRight.sol";

contract CryptoRight is ICryptoRight {

    using Counters for Counters.Counter;

    Counters.Counter copyright_ids;

    struct Work {
        address owner;
        string uri;
    }

    mapping(uint => Work) public copyrights;

    function copyrightWork(string memory reference_uri) public {
}
```

* The `copyrightWork` method spec says that we have to generate an `id` for our copyrights but it doesn't specify how. This leaves it up to us to decide. For this contract let's use a Safemath counter and make each id the incremented value from the counter.

Add the following comments inside the body of the `copyrightWork` function.

```Solidity
    function copyrightWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

    // Map the copyright_id to a Work struct containing the given uri and the msg.sender using the copyrights mapping.

    }
  ```

* The `copyrightWork` method description can be broken down into the following steps.

  * Increment the `copyright_ids` counter with `.increment()` method.

  * Define a new `uint` for the `current_id` and set it to the current value of the `copyright_ids` counter using the `.current()` method.

  * Map the `copyright_id` to a `Work struct` containing the given `uri` and the `msg.sender` using the `copyrights` mapping.

Next, add the code implementation for each commented step inside the `copyrightWork` method.

```Solidity
    function copyrightWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.
    copyright_ids.increment();

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.
    uint id = copyright_ids.current();

    // Map the copyright_id to a Work struct containing the given uri and the msg.sender using the copyrights mapping.
    copyrights[id] = Work(msg.sender, reference_uri);

    }
```

Read aloud the `openSourceWork` method interface definition.

* openSourceWork

  ```Solidity
  function openSourceWork(string memory reference_uri) public
  ```

  * The ERC333 spec defines this interface for the `openSourceWork` method.

  ```Solidity
  function openSourceWork(string memory reference_uri) public {
  }
  ```

  * This translates to code that looks like this inside the smart contract.

* Now let's focus on the `openSourceWork` function's description and break it down into comments about what steps must take place inside the function.

* Generates a new `copyright_id` of type `uint` and maps it to a `Work struct` containing the `uri`.

Add the following comments to the `openSourceWork` function body.

```Solidity
    function openSourceWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

    // Map the copyright_id to a Work struct containing the given uri using the copyrights mapping.

    // No need to set address(0) in the copyrights mapping as this is already the default for empty address types
    }
  ```

* The `openSourceWork` method description can be broken down into the following steps.

  * Increment the copyright_ids counter with .increment() method.

  * Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

  * Map the copyright_id to a Work struct containing the given uri using the copyrights mapping.

  * Also make the observation that since this type of copyright is `open source` there is no need to set `address(0)` because in the copyrights mapping this is already the default for empty address types.

Next, add the code implementation for each commented step inside the `openSourceWork` method.

```Solidity
    function openSourceWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.
    copyright_ids.increment();

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.
    uint id = copyright_ids.current();

    // Map the copyright_id to the given reference uri using the copyrights mapping.
    copyrights[id] = reference_uri;

    // No need to set address(0) in the copyrights mapping as this is already the default for empty address types

    }
  ```

Read aloud the `transferCopyrightOwnership` method interface defintion and description.

* transferCopyrightOwnership

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public;
```

  * The ERC333 spec defines this interface for the `transferCopyrightOwnership` method.

  * Now let's first focus on the second half of the `transferCopyrightOwnership` method's description "This function must only be callable by the `address` of the `owner` of the given `copyright_id`".

Add a modifier between the `copyrights mapping` and `copyrightWork` function named `onlyCopyrightOwner`. Have the modifier accept a given `uint` named `copyright_id` and inside the modifier body add a `require statment` that checks if the given. `copyrights_id` is equal to the current `msg.sender`.

```Solidity
    modifier onlyCopyrightOwner(uint copyright_id) {
        require(copyrights[copyright_id].owner == msg.sender, "You do not have permission to alter this copyright!");
        _;
    }
```

* Here we are adding a modifier named `onlyCopyrightOwner` with a  `require statment` that checks if the given. `copyrights_id` is equal to the current `msg.sender`.

Add the`transferCopyrightOwnership` function defintion with the included `onlyCopyrightOwner` modifier.

```Solidity
    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id){
    }
```

Add the following comments to the `transferCopyrightOwnership` function body.

```Solidity
    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        // Re-maps a given copyright_id to a new copyright owner.
    }
```

* Now let's take a look at the first part of the `transferCopyrightOwnership` function definition and break it down into comments about what steps must take place inside the function.

* As you can see the `transferCopyrightOwnership` method is relatively simple, the first part of the description can be copied into a single comment consisting of the exact text.

Next, add the code implementation for each commented step inside the `transferCopyrightOwnership` method.

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        // Re-maps a given copyright_id to a new copyright owner.
        copyrights[copyright_id].owner = new_owner;
    }
```

* Here we are passing our given `copyright_id` into our `copyrights mapping` to set the `owner` attribute to the `address` of the given `new_owner`

Read aloud the `renounceCopyrightOwnership` method interface definition and description.

* renounceCopyrightOwnership

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public;
```

  * The ERC333 spec defines this interface for the `renounceCopyrightOwnership` method.

Add the `renounceCopyrightOwnership` function defintion with the `onlyCopyrightOwner` modifier.

  ```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
    }
  ```

  * Let's once again focus on the second part of the `renounceCopyrightOwnership` method's description. "This function must only be callable by the address of the owner of the given copyright_id".

  * However this time around we already have our `onlyCopyrightOwner` defined. let's add it to our function definition.

* Now let's focus on the second part of the function's description and break it down into comments about what steps must take place inside the function.

* Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000 address to "open source" the copyright, and prevent anyone from modifying it further.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
    }
```

* Here the important part of the method descripton is "Re-maps a given copyright_id to the 0x0000000000000000000000000000000000000000".

* Remember we've already implemented a function that can re-map a copyright to a new owner's address called `transferCopyrightOwnership`.

Next, add the code implementation for each commented step inside the `renounceCopyrightOwnership` method.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
      transferCopyrightOwnership(copyright_id, address(0));

    }
```

* Here we call the previously `transferCopyrightOwnership` method passing it the given `copyright_id` and `address(0)`.

* Mapping something to `address(0)` in effect makes it so that no-one can ever control that copyright, eg, it becomes `open source`.

Now that all of the method definitions with their accompanying business logic have been implemented. Go back over the contract in remix and implement the defined `events` within the contract specification's events section.

Read aloud the `Copyright` event interface definition and description.

```Solidity
event Copyright(uint copyright_id, address owner, string uri);
```

* The copyright event requires a `uint copy_right_id`, an `address owner`, and a `string reference_uri`.

* According to the `Copyright` event's description it MUST trigger whenever a new copyrighted work is registered.

* Let's define our events towards the top of our contract above our modifiers.

Define the `Copyright` event above the modifier. This section of your contract should now look something like this.

```Solidity
    using Counters for Counters.Counter;

    Counters.Counter copyright_ids;

    struct Work {
        address owner;
        string uri;
    }

    mapping(uint => Work) public copyrights;

    event Copyright(uint copyright_id, address owner, string reference_uri);

    modifier onlyCopyrightOwner(uint copyright_id) {
        require(copyrights[copyright_id].owner == msg.sender, "You do not have permission to alter this copyright!");
        _;
    }
```

* Now as per the event description we have to emit the event when a new copyrighted work is registered or in other words when the `copyrightWork` function is called.

On the last line inside the body of the `copyrightWork` function `emit` the Copyright event passing it the required parameters.

```Solidity
emit Copyright(id, msg.sender, reference_uri);
```

* This should look something like this.

Read aloud the `OpenSource` event interface definition and description.

```Solidity
event OpenSource(uint copyright_id, string reference_uri);
```

* The copyright event requires a `uint copy_right_id`, and a `string reference_uri`.

* According to the `OpenSource` event's description it MUST trigger whenever a new open-source work is registered.

Add the `OpenSource` event definition below the `Copyright` event.

```Solidity
event Copyright(uint copyright_id, address owner, string uri);

event OpenSource(uint copyright_id, string reference_uri);
```

* We are going to add the `OpenSource` event below the `Copyright` event.

* Now as per the event description we have to `emit` the event when a new Open Source work is created or in other words when the `openSourceWork` and `renounceCopyrightOwnership` functions are called.

On the last line inside the body of the `OpenSource` function `emit` the Copyright event passing it the required parameters.

```Solidity
  function openSourceWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.
    copyright_ids.increment();

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.
    uint id = copyright_ids.current();

    // Map the copyright_id to the given reference uri using the copyrights mapping.
    copyrights[id] = reference_uri;

    // No need to set address(0) in the copyrights mapping as this is already the default for empty address types

    emit OpenSource(copyright_id, copyrights[copyright_id].uri);
    }
```

* Inside the `renounceCopyrightOwnership` function we emit the `OpenSource` event like this.

On the last line inside the body of the `renounceCopyrightOwnership` function `emit` the Copyright event passing it the required parameters.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
        // Re-maps a given copyright_id to the 0x0000000000000000000000000000000000000000
        transferCopyrightOwnership(copyright_id, address(0));

        emit OpenSource(copyright_id, copyrights[copyright_id].uri);
    }
```

* Inside the `renounceCopyrightOwnership` function we emit the `OpenSource` event like this.

Read aloud the `Transfer` event interface definition and description.

```Solidity
event Transfer(uint copyright_id, address new_owner);
```

* The `Transfer` event requires a `uint copyright_id`, and an `address new_owner`.

* According to the `Transfer` event's description it MUST trigger whenever copyright ownership is transferred.

Add the `Transfer` event definition below the `OpenSource` event.

```Solidity
event Copyright(uint copyright_id, address owner, string uri);

event OpenSource(uint copyright_id, string reference_uri);

event Transfer(uint copyright_id, address new_owner);
```

* We are going to add the `Transfer` event below the `OpenSource` event.

* Now as per the event description we have to emit the event whenever a copyright is transferred or in other words when the `transferCopyrightOwnership` function is called.

On the last line inside the body of the `transferCopyrightOwnership` function `emit` the `Transfer` event passing it the required parameters.

```Solidity
    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        // Re-maps a given copyright_id to a new copyright owner.
        copyrights[copyright_id].owner = new_owner;

        emit Transfer(copyright_id, new_owner);
    }
```

* We've now completed the code for an implementation of the Example ER333 copyright contract specification.

### 3. Student Do: Practice What the Instructor Just Covered (15 min)

In this activity, students will take a simple smart contract specification, in this particular case the ERC333 example contract specification and implement it.

**Instructions:**

* [README.md](Activities/02-Stu_Matching_a_Contract_Specification/README.md)

**Files:**

* [Solved - CryoptoRight.sol](Activities/02-Stu_Matching_a_Contract_Specification/Solved/CryptoRight.sol)

* [Resources - ICryptoRight.sol](Activities/02-Stu_Matching_a_Contract_Specification/Resources/ICryptoRight.sol)

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

### 5. Instructor Do: Frontend Introduction (10 min)

In this activity, you will demonstrate combining the `CryptoRight` contract with a pre-made frontend.

**Files:**

* [index.html](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/index.html)

* [dapp.js](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/dapp.js)

* [CryptoRight.json](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/CryptoRight.json)

Explain to the class:

* Since we built our `CryptoRight` contract to spec, we should be able to integrate a frontend that was designed against the same interface.

* In this scenario, a frontend developer built a graphical interface using the specification while you implemented the contract.

Copy the files linked above into a new directory, or copy the [cryptoright-frontend](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend) folder into your workspace, to a project folder called `cryptoright-frontend`.

`cd` inside of the `cryptoright-frontend` folder in a new terminal window, and run the following command:

```python
python -m http.server 8000
```

* This is a built-in Python one-liner that creates a local HTTP server that is hosting the files inside of the current directory.

* This is necessary in order to register our dApp with MetaMask. While we could just open the `index.html` file directly in our browser, MetaMask wouldn't register in this case.

* By serving from the directory, we are able to navigate to `localhost:8000`. Browsers automatically try to load `index.html` first, so since that file is present in our directory, our site will load automatically.

Next, you will need to modify the `contract_address` variable stored in the frontend code to point at your deployed contract.

Open up `dapp.js` in a code editor, and modify the first line of code. Copy the deployed contract address (redeploy a fresh contract if needed) from Remix, and set the `contract_address` variable:

```javascript
const contract_address = "0xcBE34754fE19B9b7068f6E1e1CEB4E9A1e4AAB35";
```

* We must ensure this address matches our deployed contract, otherwise the frontend will not know where to find the contract.

After that, all that is left to ensure that the `CryptoRight.json` has the contract's ABI within.

* The `CryptoRight.json` file contains the contract's ABI. This dApp automatically loads this file and expects it to be in the same directory. We'll want to ensure that our contract's ABI is in this file.

Copy over the ABI from the `Compile` tab in Remix, then paste the contents into `CryptoRight.json`, replacing any previous content completely.

Next, navigate to `localhost:8000` in your web browser. You should see an interface like:

![CryptoRight UI](Images/cryptoright-ui.png)

* This frontend fetches all `OpenSource` and `Copyright` events and displays them in a collapsable list. Since we have not copywritten anything yet, the UI is pretty empty.

* The UI also allows us to upload files and JSON to Pinata, completely locally. It takes in the `name` and `description` fields we want to account for in our `reference_uri` JSON, as well as uploading an `image`.

* The UI first uploads the image to IPFS via Pinata, then takes the image's hash, and places it inside a JSON object that contains the `name`, `description`, and `image`. This JSON object is also uploaded to IPFS, and the resulting IPFS hash is used as the final `reference_uri`.

* Once the JSON is pinned to IPFS, a transaction is created via MetaMask that calls the `copyrightWork` or `openSourceWork` functions on the `CryptoRight` contract, passing in the `reference_uri` we generated.

Now it's time to demonstrate using the frontend by creating a sample copyright.

First, navigate to your [Pinata Account Page](https://pinata.cloud/account), and copy over your API key and Secret API key into the corresponding fields in the form.

* This code directly communicates with Pinata, meaning only us and Pinata ever see the keys.

Type in a sample name and description, and upload a sample image. You can use this image as an example:

![Sample Image](Images/sample-image.jpg)

The form should look something like:

![CryptoRight Form](Images/cryptoright-form.png)

You can choose to `Check to Open Source`, or leave unchecked. If checked, the `openSourceWork` function is called instead of `copyrightWork`.

Submit the form once filled out by clicking `COPYRIGHT WORK` at the bottom of the form, and confirm the transaction that appears after uploading to IPFS:

![Form Submit](Images/cryptoright-submit.gif)

* As you can see, notifications appeared on screen updating the status of the copyright process.

* Once finished, a transaction appears for confirmation. Confirming this transaction permanently etches the `reference_uri` we uploaded via Pinata to the blockchain.

Voila! Repeat the process by uploading an `OpenSource` work by checking the `Check to Open Source` button on the form.

You can expand the items in the accordion menus:

![Cryptoright Work](Images/cryptoright-work.png)

* This frontend fetches the `reference_uri` and parses the JSON automatically, and also parses and renders the `image` as well!

* Even though the only data stored on-chain is the `reference_uri`, we are able to fetch all of this metadata with it!

Now it's time for students to integrate the frontend with their contracts!

### 6. Student Do: Integrating a Pre-Built Frontend (15 min)

In this activity, students will integrate the same frontend code with their `CryptoRight` contracts, and upload a few sample copyrights using the interface.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/04-Stu_Integrating_Frontend/README.md)

**Files:**

* [index.html](Activities/04-Stu_Integrating_Frontend/Resources/cryptoright-frontend/index.html)

* [dapp.js](Activities/04-Stu_Integrating_Frontend/Resources/cryptoright-frontend/dapp.js)

* [CryptoRight.json](Activities/04-Stu_Integrating_Frontend/Resources/cryptoright-frontend/CryptoRight.json)

Have the TAs ensure that students:

* Are running the `python -m http.server 8000` command **only** when `cd`'d directly within the directory.

* Have replaced the `contract_address` variable in the `dapp.js` file with their deployed contract.

* Have successfully implemented the contract. If the contract is not implemented properly, the frontend will not function.

### 7. Instructor Do: Frontend Review (5 min)

**Files:**

* [dapp.js](Activities/04-Stu_Integrating_Frontend/Resources/cryptoright-frontend/dapp.js)

Open the solution and explain the following:

* By setting `contract_address` to point at our deployed contract, the frontend is able to communicate with the contract via MetaMask.

* Since our contract was built to spec, the ABI generated will be the same as any other contract built to the same spec. This allows the frontend to be developed independently from the contract.

* The dApp uploads an image to IPFS, then takes that images URI and stuffs it into JSON object that also contains `name` and `description`, and uploads that to IPFS. The final URI is used for the `reference_uri` when calling the `copyrightWork` or `openSourceWork` functions on the contract.

Ask for any remaining questions before moving on.

---

### 8. BREAK (15 min)

---

### 9. Students Do: Project Work (Remainder of Class)

Students will use the remainder of class to work on their projects.

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
