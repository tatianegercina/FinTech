### 2. Building to a Smart Contract Specification : (15 min)

Instructor will discuss the process of breaking down the elements of a smart contract specification, such as it's interface, and how to turn it into functioning code.

**Files:**

* [Solved - CryptoRight.sol](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Solved/CryptoRight.sol)

* [Unsolved - CryptoRight.sol](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Unsolved/CryptoRightSpec.sol)

* [Example CryptoRight EIP](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md)

Begin by opening the [Example CryptoRight EIP](Activities/LP-02-Ins_Building_to_a_Smart_Contract_Specification/Resources/ExampleEIP.md) and displaying it for the class.

* In earlier classes we took a look at a variety of the EIP specifications located on [https://eips.ethereum.org/EIPS](https://eips.ethereum.org/EIPS)

* Today we will be taking a new example EIP, and are going to be breaking it down and translating it into functioning code.

* Let's begin by identifying the goal of the current contract This will allow us to gain scope on the logic that we will be implementing.

* A good way to identify the goal of a given contract specification is by reading the `Simple Summary`, `Abstract` and `Motivation`.

Together with the class read the `Simple Summary`, `Abstract` and `Motivation` sections of the EIP.

Open [Remix](https:://remix.ethereum.org/) in your web browser and create a new contact named `CryptoRight.sol`. Define  a new contract named `CryptoRight` that extends the `ICryptoRight` interface.

```Solidity
contract CryptoRight is ICryptoRight {
}
```

Next go through each method definition inside the specification section of the EIP document and scaffold out each function with the class.

* Now that we've familiarized ourselves with the goal of the example ERC333 copyright contract lets define the structure of our contract and scaffold out each functions business logic.

* When writing code to a particular specification it can be very helpful to write comments for each step that must be performed inside a functions body. In this activity we will take the contract specification and break down each methods business logic and backing data structures into descriptive comments.

Walk through the copyrights method interface defintion.

* copyrights

  * Accepts a given `copyright_id` as a `uint` and returns a `mapped struct` containing the copyright's `owner` and `uri`.

  Inside the CryptoRight contract create a new struct named `Work`. Inside this struct create an `address` attribute named `owner` and a `string` attribute named `uri`.

  ```Solidity
    struct Work {
        address owner;
        string uri;
    }
  ```

* According to the `copyrights` method's spec we need a "`struct` containing the copyright's `owner` and `uri`".

  ```Solidity
  function copyright(uint copyright_id) public returns(string memory reference_uri);
  ```

  * The ERC333 spec defines this interface for the copyrights method.

  Now demonstrate what this looks like implemented inside the smart contract.

  ```Solidity
  mapping(uint => Work) public copyrights;
  ```

  * This translates to a function defintion that looks like this.

  * The details of the method were "Accepts a given `copyright_id` as a `uint` and returns a `mapped string`".

  * Pay particular attention to the wording  "as a `uint` and returns a `mapped string`, this can be translated to "a `uint` mapped to a `string`", eg, a mapping.

  * Remember that a variable defined with the public modifier automatically generates a getter function with defined parameters. In this case our publically defined mapping `copyrights` generates a getter function that accepts a `uint` and retruns a `Work` struct.

  * This is a great example of how a specification's defined interface may not always exactly match what the actual code will look like but rather the interface that will be generated. Interface being both a defined function and the concept of what input/ouput for a given API is expected to be present.

Walk through the `copyrightWork` method interface defintion.

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

  * This translates to code that looks like this inside the smart contract.

* Now let's focus on the function's description and break it down into comments about what steps must take place inside the function.

Read the `copyrightWork` method's description.

* Generates a new `copyright_id` of type `uint` and maps it to a `Work struct` containing the given copyright `owner` and `uri`.

Add the imports for `SafeMath counters` under the `pragma` and bind the `counter library` to the `Counter` datatype below the contrat defintion.

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

```Solidity
    function copyrightWork(string memory reference_uri) public {
    // Increment the copyright_ids counter with .increment() method.

    // Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

    // Map the copyright_id to a Work struct containing the given uri and the msg.sender using the copyrights mapping.

    }
  ```

* The `copyrightWork` method description can be broken down into the following steps.

  * Increment the copyright_ids counter with .increment() method.

  * Define a new uint for the current_id and set it to the current value of the copyright_ids counter using the .current() method.

  * Map the copyright_id to a Work struct containing the given uri and the msg.sender using the copyrights mapping.

Next add the code implementation for each commented step inside the `copyrightWork` method.

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

Walk through the `openSourceWork` method interface defintion.

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

Next add the code implementation for each commented step inside the `openSourceWork` method.

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

Walk through the `transferCopyrightOwnership` method interface defintion.

* transferCopyrightOwnership

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public;
```

  * The ERC333 spec defines this interface for the `transferCopyrightOwnership` method.

  * Now let's first focus on the second half of the `transferCopyrightOwnership` method's description "This function must only be callable by the `address` of the `owner` of the given `copyright_id`".

Add a modifier between the `copyrights mapping` and `copyrightWork` function named `onlyCopyrightOwner`. Have the modifier accept a given `uint` named `copyright_id` and inside the modifer body add a `require statment` that checks if the given. `copyrights_id` is equal to the current `msg.sender`.

```Solidity
    modifier onlyCopyrightOwner(uint copyright_id) {
        require(copyrights[copyright_id].owner == msg.sender, "You do not have permission to alter this copyright!");
        _;
    }
```

* Here we are adding a modifier named `onlyCopyrightOwner` with a  `require statment` that checks if the given. `copyrights_id` is equal to the current `msg.sender`.

Add the`transferCopyrightOwnership` function defintion with the included `onlyCopyrightOwner`   modifier.

```Solidity
    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
    }
```

Add the following comments to the `transferCopyrightOwnership` function body.

```Solidity
    function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        // Re-maps a given copyright_id to a new copyright owner.
    }
```

* Now let's take a look at the first part of the `transferCopyrightOwnership` function defintion and break it down into comments about what steps must take place inside the function.

* As you can see the `transferCopyrightOwnership` method is relatively simple, the first part of the description can be copied into a single comment consisting of the exact text.

Next add the code implementation for each commented step inside the `transferCopyrightOwnership` method.

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id) {
        // Re-maps a given copyright_id to a new copyright owner.
        copyrights[copyright_id].owner = new_owner;
    }
```

* Here we are passing our given `copyright_id` into our `copyrights mapping` in order to set the `owner` attribute to the `address` of the given `new_owner`

Walk through the `renounceCopyrightOwnership` method interface defintion.

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

  * However this time around we already have our `onlyCopyrightOwner` defined. let's add it to our function defintion.

* Now let's focus on the second part of the function's description and break it down into comments about what steps must take place inside the function.

* Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000 address in order to "open source" the copyright, and prevent anyone from modifying it further.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
    }
```

* Here the important part of the method descripton is "Re-maps a given copyright_id to the 0x0000000000000000000000000000000000000000".

* Remember we've already impelmented a function that is able to re-map a copyright to a new owner's address called `transferCopyrightOwnership`.

Next add the code implementation for each commented step inside the `renounceCopyrightOwnership` method.

```Solidity
    function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id) {
      //Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000
      transferCopyrightOwnership(copyright_id, address(0));

    }
```

* Here we call the previously `transferCopyrightOwnership` method passing it the given `copyright_id` and `address(0)`.

* Mapping something to `address(0)` in effect makes it so that nonone can ever control that copyright, eg, it becomes `open source`.

Now that all of the method defintions with their accompanying bussiness logic have been implemented. Go back over the contract in remix and implement the defined `events` within the contract specification's events section.

Walk through the `Copyright` event.

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

Walk through the `OpenSource` event.

```Solidity
event OpenSource(uint copyright_id, string reference_uri);
```

* The copyright event requires a `uint copy_right_id`, and a `string reference_uri`.

* According to the `OpenSource` event's description it MUST trigger whenever a new open source work is registered.

Add the `OpenSource` event defintion below the `Copyright` event.

```Solidity
event Copyright(uint copyright_id, address owner, string uri);

event OpenSource(uint copyright_id, string reference_uri);
```

* We are going to add the `OpenSource` event below the `Copyright` event.

* Now as per the event description we have to `emit` the event when a new Open Source work is created or in other words when the `openSourceWork` and `renounceCopyrightOwnership` functions are called.

On the last line inside the body of the `OpenSource` function `emit` the Copyright event passing it the required parameters.

```Solidity
    function openSourceWork(string memory reference_uri) public {
        copyright_ids.increment();
        uint id = copyright_ids.current();

        copyrights[id].uri = reference_uri;
        // no need to set address(0) in the copyrights mapping as this is already the default for empty address types

        emit OpenSource(id, reference_uri);
    }
```

* Inside the `openSourceWork` function we emit the `OpenSource` event like this.

On the last line inside the body of the `renounceCopyrightOwnership` function `emit` the Copyright event passing it the required parameters.

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

Walk through the `Transfer` event.

```Solidity
event Transfer(uint copyright_id, address new_owner);
```

* The `Transfer` event requires a `uint copyright_id`, and an `address new_owner`.

* According to the `Transfer` event's description it MUST trigger whenever copyright ownership is transferred.

Add the `Transfer` event defintion below the `OpenSource` event.

```Solidity
event Copyright(uint copyright_id, address owner, string uri);

event OpenSource(uint copyright_id, string reference_uri);

event Transfer(uint copyright_id, address new_owner);
```

* We are going to add the `Transfer` event below the `OpenSource` event.

* Now as per the event description we have to emit the event whenever a copyright is transferred or in other words when the `transferCopyrightOwnership` function is called.

On the last line inside the body of the `transferCopyrightOwnership` function `emit` the `Transfer` event passing it the required parameters.
