## 22.2 Lesson Plan: dApp Deployment

### Overview

In today's class, students will be introduced to the thought processes and techniques that go into taking a formalized contract spec and implementing it into Solidity code. In the software development process, employees frequently collaborate, creating a separation of concerns within a system's architecture. Students will learn to take a simple, yet more formalized, smart contract specification and implement it to fit the interface of an already established front-end dApp. Students will then deploy the configured dApp to a centralized production environment, GitHub pages.

Students will use the remainder of the class to work on their projects.

---

### Class Objectives

By the end of the class, students will be able to:

* Implement a given smart contract specification into real Solidity code.

* Integrate the contract with a JavaScript/HTML/CSS front end.

* Deploy a bundled dApp to GitHub Pages.

* Customize and deploy a landing page for projects on GitHub Pages.

---

### Instructor Notes

* Refer to the `IPFS` documentation for further information about [IPFS Docs](https://docs.ipfs.io/)

---

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1nddRMy7DUMXZ7q9EeIpz0V78YT6wWjSjB_KaKK3Ts5k/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

---

### 1. Instructor Do: Welcome to Class (10 min)

In the previous class, students were introduced to the concept of DeFi (short for decentralized finance). Many of the concepts they have learned up to now can be leveraged to build financial systems based on DeFi principles, as well as given the tools that directly enable these systems through the deployment of dApps such as solidity events and IPFS. Briefly review the following talking points to refresh the class on DeFi, events, and IPFS.

* What are some benefits of Solidity events?

  **Answer:** They are a cheap amount of gas.

  **Answer:** They allow you to keep a log of information on-chain.

  **Answer:** Events are MUCH cheaper than contract storage.

  **Answer:** Events are Solidity's built-in way to interact with something external, such as a user interface.

* What are some potential issues that IPFS seeks to solve?

  **Answer:** Inefficiencies in the web such as `duplicate files`.

  **Answer:** Inefficiencies in the web such as having to route to a faraway server to get the file you need when it might be right next door.

  **Answer:** Problems with security and file integrity, such as not knowing if files you have accessed over the web have changed.

  **Answer:** Problems with the security of centralized servers providing a centralized attack vector.

### 2. Instructor Do: Building to a Smart Contract Specification (15 min)

The instructor will discuss the process of breaking down the elements of a smart contract specification, such as its interface, and how to turn it into functioning code. The EIP provides an example interface file for testing the contract linked below.

**Files:**

* [Solved - CryptoRight.sol](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Solved/CryptoRight.sol)

* [ICryptoRight.sol](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ICryptoRight.sol)

* [Example CryptoRight EIP](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md)

Begin by opening the [Example CryptoRight EIP](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md) and displaying it for the class.

* In earlier classes, we took a look at a variety of the EIP specifications located on [https://eips.ethereum.org/](https://eips.ethereum.org/)

* Today, we will take a new example EIP, break it down, and translate it into functioning code. Remember—an EIP is an Ethereum Improvement Proposal. An ERC is an application-level (aka, Solidity) EIP.

* Let's begin by identifying the goal of the current contract. This will allow us to gain scope on the logic that we will be implementing.

* A good way to identify the goal of a given contract specification is by reading the `Simple Summary`, `Abstract`, and `Motivation`.

Together with the class, read the `Simple Summary`, `Abstract`, and `Motivation` sections of the EIP.

Open [Remix](https://remix.ethereum.org/) in your web browser and create two new contracts—the first named `ICryptoRight.sol` and the second named `CryptoRight.sol`.

Inside `ICryptoRight.sol` paste the contents of [ICryptoRight.sol](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ICryptoRight.sol) from the Resources folder.

Inside `CryptoRight.sol` define a new contract named `CryptoRight` that extends the `ICryptoRight` interface.

```Solidity
pragma solidity ^0.5.0;

import "./ICryptoRight.sol";

contract CryptoRight is ICryptoRight {
}
```

* We can ignore the `ABIEncoderV2` warning that appears. This specification is using the latest ABI encoder in order to support checking certain functionalities at a more granular level (such as checking if we return a Work struct from a mapping).

Next, pull up Remix side by side with the [Example CryptoRight EIP](Activities/01-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md).

* Now that we've familiarized ourselves with the goal of the example ERC333 copyright contract, let's define the structure of our contract and scaffold out each function's business logic.

* When writing code to a particular specification, it can be very helpful to write comments for each step that must be performed inside a function's body. In this activity, we will take the contract specification and break down each component of the method's business logic and backing data structures into descriptive comments.

Read aloud the `copyrights` method's interface definition and description.

* `copyrights`

* Accepts a given `copyright_id` as a `uint` and returns a `mapped struct` containing the copyrights `owner` and `uri`.

Highlight the CryptoRight contract interface definition.

```Solidity
function copyrights(uint copyright_id) public returns(IWork memory);
```

* The ERC333 spec defines this interface for the copyrights method.

Now, demonstrate what this looks like implemented inside the smart contract.

```Solidity
mapping(uint => Work) public copyrights;
```

  * The details of the method were "Accepts a given `copyright_id` as a `uint` and returns a `mapped string`".
  * This translates to a `mapping` of a `uint` and a `Work` datatype.

  * Pay particular attention to the wording  "as a `uint` and returns a `mapped string`, this can be translated to "a `uint` mapped to a `string`", e.g., a mapping.

  * Remember that a variable defined with the public modifier automatically generates a getter function with defined parameters. In this case, our publically defined mapping `copyrights` generates a getter function that accepts a `uint` and returns a `Work` struct.

  * This is a great example of how a specification's defined interface may not always exactly match what the actual code will look like, but rather the interface that will be generated. `Interface` is both a defined function and the concept of what input/output for a given `API` is expected to be present.

Inside the CryptoRight contract under the `copyright_ids` counter, create a new `struct` named `Work`. Inside this `struct` create an `address` attribute named `owner` and a `string` attribute named `uri`.

  ```Solidity
  struct Work {
      address owner;
      string uri;
  }
  ```

* We've created our map that references a custom datatype named `Work`, but now we have to define that datatype with a `struct`.

* According to the `copyrights` method's spec, we need a "`struct` containing the copyrights `owner` and `uri`".

Read aloud the `copyrightWork` method interface definition and description.

* `copyrightWork`

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

* The `copyrightWork` method spec says that we have to generate an `id` for our copyrights, but it doesn't specify how. This leaves it up to us to decide. For this contract, let's use a SafeMath counter and make each id the incremented value from the counter.

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

* `openSourceWork`

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

  * Also make the observation that since this type of copyright is `open source`, there is no need to set `address(0)` because in the copyrights mapping, this is already the default for empty address types.

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

Read aloud the `transferCopyrightOwnership` method interface definition and description.

* transferCopyrightOwnership

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public;
```

  * The ERC333 spec defines this interface for the `transferCopyrightOwnership` method.

  * Now let's first focus on the second half of the `transferCopyrightOwnership` method's description "This function must only be callable by the `address` of the `owner` of the given `copyright_id`".

Add a modifier between the `copyrights mapping` and `copyrightWork` function named `onlyCopyrightOwner`. Have the modifier accept a given `uint` named `copyright_id` and inside the modifier body add a `require statment` that checks if the given `copyrights_id` is equal to the current `msg.sender`.

```Solidity
    modifier onlyCopyrightOwner(uint copyright_id) {
        require(copyrights[copyright_id].owner == msg.sender, "You do not have permission to alter this copyright!");
        _;
    }
```

* Here we are adding a modifier named `onlyCopyrightOwner` with a  `require statement` that checks if the given `copyrights_id` is equal to the current `msg.sender`.

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

* Now, let's take a look at the first part of the `transferCopyrightOwnership` function definition, and break it down into comments about what steps must take place inside the function.

* As you can see, the `transferCopyrightOwnership` method is relatively simple; the first part of the description can be copied into a single comment consisting of the exact text.

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

  * However, this time around, we already have our `onlyCopyrightOwner` defined. Let's add it to our function definition.

* Now, let's focus on the second part of the function's description and break it down into comments about what steps must take place inside the function.

* Remap a given copyright ID to the 0x0000000000000000000000000000000000000000 address to "open source" the copyright, and prevent anyone from modifying it further.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
    }
```

* Here the important part of the method descripton is "Remaps a given copyright_id to the 0x0000000000000000000000000000000000000000".

* Remember: we've already implemented a function that can remap copyright to a new owner's address called `transferCopyrightOwnership`.

Next, add the code implementation for each commented step inside the `renounceCopyrightOwnership` method.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
      transferCopyrightOwnership(copyright_id, address(0));

    }
```

* Here we call the previously `transferCopyrightOwnership` method, passing it the given `copyright_id` and `address(0)`.

* Mapping, something to `address(0)` in effect, makes it so that no one can ever control that copyright; e.g., it becomes `open source`.

Now all of the method definitions with their accompanying business logic have been implemented. Go back over the contract in Remix and implement the defined `events` within the contract specification's events section.

Read aloud the `Copyright` event interface definition and description.

```Solidity
event Copyright(uint copyright_id, address owner, string reference_uri);
```

* The copyright event requires a `uint copyright_id`, an `address owner`, and a `string reference_uri`.

* According to the `Copyright` event's description, it MUST trigger whenever a new copyrighted work is registered.

* Let's define our events towards the top of our contract, above our modifiers.

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

* Now, as per the event description, we have to emit the event when a new copyrighted work is registered or, in other words, when the `copyrightWork` function is called.

On the last line inside the body of the `copyrightWork` function `emit` the copyright event, passing it the required parameters.

```Solidity
emit Copyright(id, msg.sender, reference_uri);
```

* This should look something like this.

Read aloud the `OpenSource` event interface definition and description.

```Solidity
event OpenSource(uint copyright_id, string reference_uri);
```

* The copyright event requires a `uint copy_right_id`, and a `string reference_uri`.

* According to the `OpenSource` event's description, it MUST trigger whenever a new open source work is registered.

Add the `OpenSource` event definition below the `Copyright` event.

```Solidity
event Copyright(uint copyright_id, address owner, string reference_uri);

event OpenSource(uint copyright_id, string reference_uri);
```

* As you can see, we are going to add the `OpenSource` event below the `Copyright` event, but the order does not matter.

* Now, as per the event description, we have to `emit` the event when a new open source work is created, such as when the `openSourceWork` and `renounceCopyrightOwnership` functions are called.

On the last line inside the body of the `OpenSource` function, `emit` the copyright event, passing it the required parameters.

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

On the last line inside the body of the `renounceCopyrightOwnership` function `emit` the copyright event, passing it the required parameters.

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

* According to the `Transfer` event's description, it MUST trigger whenever copyright ownership is transferred.

Add the `Transfer` event definition below the `OpenSource` event.

```Solidity
event Copyright(uint copyright_id, address owner, string reference_uri);

event OpenSource(uint copyright_id, string reference_uri);

event Transfer(uint copyright_id, address new_owner);
```

* We are going to add the `Transfer` event below the `OpenSource` event.

* Now, as per the event description, we have to emit the event whenever copyright is transferred or, in other words, when the `transferCopyrightOwnership` function is called.

On the last line inside the body of the `transferCopyrightOwnership` function, `emit` the `Transfer` event passing it the required parameters.

```Solidity
    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        // Re-maps a given copyright_id to a new copyright owner.
        copyrights[copyright_id].owner = new_owner;

        emit Transfer(copyright_id, new_owner);
    }
```

* We've now completed the code for an implementation of the Example ER333 copyright contract specification.

### 3. Student Do: Building to a Smart Contract Specification (15 min)

In this activity, students will take a simple, smart contract specification—in this case, the ERC333 example contract specification—and implement it.

**Instructions:**

* [README.md](Activities/02-Stu_Matching_a_Contract_Specification/README.md)

**Files:**

* [Solved - CryoptoRight.sol](Activities/02-Stu_Matching_a_Contract_Specification/Solved/CryptoRight.sol)

* [Resources - ICryptoRight.sol](Activities/02-Stu_Matching_a_Contract_Specification/Resources/ICryptoRight.sol)

### 4. Instructor Do: Smart Contract Specifications Review (10 min)

Review the solution and highlight the following:

```Solidity
using Counters for Counters.Counter;

Counters.Counter copyright_ids;

struct Work {
    address owner;
    string uri;
}

mapping(uint => Work) public copyrights;

```

* Our contract makes use of SafeMath counters to generate the next `copyright_id`.

* We've also defined a custom `struct` named `Work` that contains an `address` of the `owner` of the copyright and the corresponding `uri`.

* A mapping named `copyrights` is used in our contract to map generated `copyright_id`s to their corresponding `Work` info.

```Solidity
event Copyright(uint copyright_id, address owner, string reference_uri);

event OpenSource(uint copyright_id, string reference_uri);

event Transfer(uint copyright_id, address new_owner);
```

* We've also defined the three events defined in our copyright specification: `Copyright`, `OpenSource`, and `Transfer`.

```Solidity
modifier onlyCopyrightOwner(uint copyright_id) {
    require(copyrights[copyright_id].owner == msg.sender, "You do not have permission to alter this copyright!");
    _;
}
```

* To restrict the `transferCopyrightOwnership` and `renounceCopyrightOwnership` methods so that only the owner of the `copyright_id` given to the function can call it, we implemented the `onlyCopyrightOwner` modifier containing a require that compares the given `copyright_id` parameter to the current `msg.sender`.

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

* The `copyrightWork` and `openSourceWork` functions were both implemented in a very similar way. Both functions generate a new `copyright_id` by incrementing the `copyright_ids` counter and taking its current value. Where the two functions differ is when it comes to setting the Work's owner's address. Since open source works don't have an owner in this system, we leave the `owner` attribute set to the default `address(0)`.


```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
    // Re-maps a given copyright_id to a new copyright owner.
    copyrights[copyright_id].owner = new_owner;

    emit Transfer(copyright_id, new_owner);
    }
```

* The `transferCopyrightOwnership` function simply remaps a given copyright_id to a new copyright owner, and emits the `Transfer` event.

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

* **Answer** Common functionality such as generating copyright_ids could be abstracted to an internal function.

* What are some reasons for using a struct with two attributes, as opposed to two mappings for the copyright `owner` and `uri`?

* **Answer:** Cheaper gas cost.

* **Answer:** Less complex code.

* After having completed this exercise, can you think of any interesting EIP/ERC specification ideas?

### 5. Instructor Do: Front-end Introduction (10 min)

In this activity, you will demonstrate combining the `CryptoRight` contract with a pre-made frontend.

**Files:**

* [index.html](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/index.html)

* [dapp.js](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/dapp.js)

* [CryptoRight.json](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/CryptoRight.json)

Explain to the class:

* Since we built our `CryptoRight` contract to spec, we should be able to integrate a front end that was designed against the same interface.

* In this scenario, a front-end developer built a graphical interface using the specification while you implemented the contract.

Copy the files linked above into a new directory, or copy the [cryptoright-frontend](Activities/03-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend) folder into your workspace, to a project folder called `cryptoright-frontend`.

`cd` inside of the `cryptoright-frontend` folder in a new terminal window, and run the following command:

```python
python -m http.server 8000
```

* This is a built-in, Python one-liner that creates a local HTTP server that is hosting the files inside of the current directory.

* This is necessary in order to register our dApp with MetaMask. While we could just open the `index.html` file directly in our browser, MetaMask wouldn't register in this case.

* By serving from the directory, we are able to navigate to `localhost:8000`. Browsers automatically try to load `index.html` first, so since that file is present in our directory, our site will load automatically.

Next, you will need to modify the `contract_address` variable stored in the front-end code to point at your deployed contract.

Open up `dapp.js` in a code editor, and modify the first line of code. Copy the deployed contract address (redeploy a fresh contract if needed) from Remix, and set the `contract_address` variable:

```javascript
const contract_address = "0xa5b70b3f9e02b2d0b85E10042a76b1A7F397Cc6b";
```

* We must ensure this address matches our deployed contract; otherwise, the front end will not know where to find the contract.

After that, all that remains is to ensure that the `CryptoRight.json` has the contract's ABI within.

* The `CryptoRight.json` file contains the contract's ABI. This dApp automatically loads this file and expects it to be in the same directory. We'll want to ensure that our contract's ABI is in this file.

Copy over the ABI from the `Compile` tab in Remix, then paste the contents into `CryptoRight.json`, replacing any previous content completely.

Next, navigate to `localhost:8000` in your web browser. You should see an interface like:

![CryptoRight UI](Images/cryptoright-ui.png)

* This front-end fetches all `OpenSource` and `Copyright` events and displays them in a collapsible list. Since we have not copywritten anything yet, the UI is fairly empty.

* The UI also allows us to upload files and JSON to Pinata, completely locally. It takes in the `name` and `description` fields we want to account for in our `reference_uri` JSON, as well as uploading an `image`.

* The UI first uploads the image to IPFS via Pinata, then takes the image's hash, and places it inside a JSON object that contains the `name`, `description`, and `image`. This JSON object is also uploaded to IPFS, and the resulting IPFS hash is used as the final `reference_uri`.

* Once the JSON is pinned to IPFS, a transaction is created via MetaMask that calls the `copyrightWork` or `openSourceWork` functions on the `CryptoRight` contract, passing in the `reference_uri` we generated.

Now it's time to demonstrate using the front end by creating sample copyright.

First, navigate to your [Pinata Account Page](https://pinata.cloud/account), and copy over your API key and Secret API key into the corresponding fields in the form.

* This code directly communicates with Pinata, meaning only us and Pinata ever see the keys.

Type in a sample name and description, and upload a sample image. You can use this image as an example:

![Sample Image](Images/sample-image.jpg)

The form should look something like:

![CryptoRight Form](Images/cryptoright-form.png)

You can choose to `Check to Open Source`, or leave unchecked. If checked, the `openSourceWork` function is called instead of `copyrightWork`.

Once the form is filled out, submit by clicking `COPYRIGHT WORK` at the bottom of the form, and confirm the transaction that appears after uploading to IPFS:

![Form Submit](Images/cryptoright-submit.gif)

* As you can see, notifications appeared on-screen, updating the status of the copyright process.

* Once finished, a transaction appears for confirmation. Confirming this transaction permanently etches the `reference_uri` we uploaded via Pinata to the blockchain.

Voila! Repeat the process by uploading an `OpenSource` work by checking the `Check to Open Source` button on the form.

You can expand the items in the accordion menus:

![Cryptoright Work](Images/cryptoright-work.png)

* This front end fetches the `reference_uri` and parses the JSON automatically, and also parses and renders the `image` as well!

* Even though the only data stored on-chain is the `reference_uri`, we can fetch all of this metadata with it!

Now it's time for students to integrate the front end with their contracts!

### 6. Student Do: Integrating a Pre-Built Front end (15 min)

In this activity, students will integrate the same front-end code with their `CryptoRight` contracts, and upload a few sample copyrights using the interface.

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

* Have successfully implemented the contract. If the contract is not implemented properly, the front end will not function.

### 7. Instructor Do: Front end Review (5 min)

**Files:**

* [dapp.js](Activities/04-Stu_Integrating_Frontend/Resources/cryptoright-frontend/dapp.js)

Open the solution and explain the following:

* By setting `contract_address` to point at our deployed contract, the front end can communicate with the contract via MetaMask.

* Since our contract was built to spec, the ABI generated will be the same as any other contract built to the same spec. This allows the front end to be developed independently from the contract.

* The dApp uploads an image to IPFS, then takes that image's URI and stuffs it into a JSON object that also contains `name` and `description`, and uploads that to IPFS. The final URI is used for the `reference_uri` when calling the `copyrightWork` or `openSourceWork` functions on the contract.

Ask for any remaining questions before moving on.

### 8. Instructor Do: Intro to GitHub Pages (10 min)

In this activity, you will demonstrate the elegant but simple GitHub themes that GitHub Pages provides. You will create a landing page for this dApp explaining its purpose, the technology it is written with, and linking it to the subfolder.

In the following activity, students will create a simple website explaining their application, which will allow them to explain their applications to future employers better, and the world in general.

**Files:**

* [index.html](Activities/05-Ins_Intro_Github_Pages/Resources/cryptoright/frontend/index.html)

* [dapp.js](Activities/05-Ins_Intro_Github_Pages/Resources/cryptoright/frontend/dapp.js)

* [CryptoRight.json](Activities/05-Ins_Intro_Github_Pages/Resources/cryptoright/frontend/CryptoRight.json)

* [README.md](Activities/05-Ins_Intro_Github_Pages/Resources/cryptoright/README.md)

First, explain to students what Github Pages allows us to do:

* GitHub Pages is a service provided by GitHub that automatically creates websites from your git repositories.

* It allows us to define a `README.md` file and convert it into a simple landing page website that we can use to describe our application to new users, other developers, or future employers; essentially, anyone who might not fully understand what the application does and how it works.

* We are going to create a simple `README.md` file, describe our application, and link to it. Then, we just need to create a repository on GitHub, push our code to it, set a theme, and then we're live!

In your workspace, create a folder called `cryptoright` and `cd` into it:

```bash
mkdir cryptoright
cd cryptoright
```

Next, move the front-end code from the previous folder you were working in that contained the `dapp.js`, `index.html`, and `CryptoRight.json` into a subfolder called `frontend`.

Create a `README.md` inside the top-level `cryptoright` folder.

Your directory tree should look something like:

![Github Pages file tree](Images/github-pages-tree.png)

Within this `README.md` file, add some information explaining the application.
You will also need to include a link to the dApp's `frontend` directory.

* GitHub Pages will automatically convert the Markdown file into the HTML necessary to render the website's landing page. By including a link to the `frontend` directory in the `README.md` file, we can generate a URL that points to the dApp's front-end code from our landing page.

For now, just add something simple like:

```markdown

# CryptoRight Blockchain Copyright System

## Summary

This application is a copyright management system built on the Ethereum blockchain.

### Demo App

Click [here](frontend/index.html) to launch the CryptoRight application.

```

* We can use regular Markdown syntax when writing our `README.md`. We just need to make sure that we include a link to `frontend/index.html` somewhere to point to our dApp.

Next, create a new GitHub repository by navigating to [Github](https://github.com), clicking the `+` at the top right, and selecting `New Repository`:

![New Github Repo](Images/github-new-repo.png)

Give it a title and a short description.

* We need to set this repo to public in order to publish it as a website.

* We also do not need to initialize the repository with a `README` since we have one already.

Next, run the first set of commands that GitHub provides for uploading existing code to the repo, minus the first line of code that `echo`s to the `README.md` file:

![Github Upload CLI](Images/github-repo-cli.png)

* We need to run these commands within the `cryptoright` directory that contains all of our code, including the `README.md` and the `frontend` folder.

* We don't need to run the `echo "# cryptoright" >> README.md` line, since we already have content in there.

Once you run this set of commands, you will need to upload the rest of the front-end code, since this set only uploads the `README.md`:

```bash
git add -A
git commit -m "add frontend code"
git push
```

After running this, all of the code should be uploaded to the repository.

![Github Upload Complete](Images/github-upload.png)

Navigate to the repo settings on GitHub by clicking the `Settings` tab, and scroll down to the `Github Pages` section, and set the `Source` to `master`:

![Github Pages Setup](Images/github-pages-setup.gif)

* By setting up the `Source` that GitHub Pages will use to `master`, we are telling it to build out everything inside of our repository into a website.

* All we need to do next is set a theme!

Click the theme chooser in the same section, and play around with the themes, showing them off to the class a bit. Pick a theme, then navigate to the URL that GitHub Pages provides. You should see your website generated! **(This may take a few moments to reflect and may need a refresh.)**

Click on the link that you generated to take you to your dApp, and ensure MetaMask is pointed at the correct network. The dApp should request permissions to connect, and once on the same network the contract is deployed to, the CryptoRight data should populate.

![Github Pages Theme](Images/github-pages-theme.gif)

* Just like that, we have created an elegant landing page website for our dApp. GitHub Pages has a lot of customization that you can dig even deeper into to make a nice website without yet having to learn front-end development.

* We can also deploy our contracts to a live testnet like Kovan or Ropsten, or even the Mainnet. All we need to change is the contract address in our front-end code!

Voila! Now it's time to have students create their own landing pages!

### 9. Student Do: Create a Landing Page with GitHub Pages (15 min)

Now it's time for the students to create their own landing pages!

Send out the instructions and have TAs circulate the room.

**Instructions:**

* [README.md](Activities/06-Stu_Github_Pages/README.md)

**Files:**

* [CryptoRight.json](Activities/06-Stu_Github_Pages/Resources/cryptoright/frontend/CryptoRight.json)

* [dapp.js](Activities/06-Stu_Github_Pages/Resources/cryptoright/frontend/dapp.js)

* [index.html](Activities/06-Stu_Github_Pages/Resources/cryptoright/frontend/dapp.js)

* [README.md](Activities/06-Stu_Github_Pages/Resources/cryptoright/README.md)

Ensure the following:

* Students are using their own ABIs in `CryptoRight.json` and that their front ends are functioning with the local `python -m http.server 8000` command before attempting this activity.

* Ensure that students' directory trees look like the following:

  ![Github File Tree](Images/github-pages-tree.png)

* Ensure that within the `README.md` there is a link to the `frontend/index.html` file somewhere in order to generate the URL to the front-end dApp.

### 10. Instructor Do: GitHub Pages Review (10 min)

Ask students the following questions:

* What is the purpose of having a GitHub Pages website for our dApp?

  **Answer:** It allows us to demonstrate our expertise in a context that we can control.

  **Answer:** It allows us to write documentation websites, explain the purpose of our project, gain developer and user traction, and much more.

* What facilitates the connection between our front-end code that GitHub Pages hosts, and the Ethereum networks that we have configured/connected to?

  **Answer:** MetaMask!

* Would our front-end code work if we deployed it anywhere else?

  **Answer:** Yes, as long as the browser has MetaMask installed, our dApp will run!

* Would it be possible to deploy our front-end code to IPFS?

  **Answer:** Absolutely! However, it would require some code changes to make sure that the URLs referenced work properly.

* Would it be possible to use GitHub Pages to create a portfolio website that allows us to show off more than this application?

  **Answer:** Absolutely! It should be leveraged wherever possible to give your work more exposure.

---

### 11. BREAK (15 min)

---

### 12. Student Do: Project Work (Remainder of Class)

Students will use the remainder of the class to work on their projects.

---

### End Class

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
