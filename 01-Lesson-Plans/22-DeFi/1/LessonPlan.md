## 22.1 Lesson Plan: DeFi (Decentralized Finance)

---

### Please take the End-Course Instructional Staff Survey if You Haven't Yet

Trilogy, as a company, values transparency and data-driven change quite highly. As we grow, we know there will be areas that need improvement. It’s hard for us to understand what these areas are unless we’re asking questions. Your candid input truly matters to us, as you are key members of the Trilogy team. In addition to the individual feedback at the end of lesson plans, we would appreciate your feedback at the following link if you have not already taken the end-course survey:

[Instructional Staff Survey](https://docs.google.com/forms/d/e/1FAIpQLSfYVe6jUQwDoXferzGqfd3LZ1k0i_RWzgwccd1f5arSXg2pzA/viewform)

### Overview

In today's class, students will be introduced to the concept of DeFi (short for decentralized finance). Though DeFi most commonly refers to financial systems built upon distributed ledgers frequently leveraging smart contracts. Students will gain the scope that DeFi is not a particular technology or implementation but rather a movement within the financial technology sector where future financial systems are being created and deployed with an open, decentralized, and permissionless architecture.

### Class Objectives

By the end of the unit, students will be able to:

* Build non-fungible ERC721 tokens with OpenZeppelin

* Explain what events are and how they can be used to create a dApp

* Use IPFS to store immutable data off-chain to save gas

* Use Filters in Web3.py to react to Events from smart contracts

### Slideshow and Time Tracker

* The slides for this lesson can be viewed on Google Drive here: [Lesson Slides](https://docs.google.com/presentation/d/1v3vPpBsLchwg8EIWQGC4UXutou2DZmD20b7SyrjQhv4/edit?usp=sharing).

* To add the slides to the student-facing repository, download the slides as a PDF by navigating to File, selecting "Download as," and then choosing "PDF document." Then, add the PDF file to your class repository along with other necessary files. You can view instructions for this [here](https://docs.google.com/document/d/1XM90c4s9XjwZHjdUlwEMcv2iXcO_yRGx5p2iLZ3BGNI/edit?usp=sharing).

* **Note:** Editing access is not available for this document. If you wish to modify the slides, create a copy by navigating to File and selecting `Make a copy`.

* The Time Tracker for this lesson can be found here: [Time Tracker](TimeTracker.xlsx).

### Instructor Notes

* The contracts you will be deploying today are relatively large and may take a few minutes to compile.

* Refer to OpenZeppelin ERC721 documentation for further information about Non-Fungible Tokens. [ERC721 Docs](https://docs.openzeppelin.com/contracts/2.x/api/token/erc721)

* Refer to the `IPFS` documentation for further information about [IPFS Docs](https://docs.ipfs.io/)

* Have your TAs keep track with the [Time Tracker](TimeTracker.xlsx)

### 1. Instructor Do: Welcome Back (10 min)

Previously students have implemented both a basic token as well as the ERC21 fungible token standard using the OpenZeppelin libraries. Today they will be implementing their first ERC721 Non-fungible token using the Openzeppelin libraries. Take a few minutes to review ERC's, OpenZeppelin, and the concept of fungibility by discussing the following recall questions with the class.

* What are some differences between `fungible` and `non-fungible` tokens?

* **Answer** Non-fungible tokens are unique, fungible tokens are not unique.

* **Answer** Fungible tokens are interchangeable with one another whereas non-fungible are not.

* **Answer** non-fungible tokens use ERC 721, fungible tokens use ERC 777.

* What are some examples of `fungible` assets?

* **Answer** United States Dollars (USD)

* **Answer** Ethereum (ETH)

* **Answer** Bitcoin (BTC)

* **Answer** Gold

* What are some examples of `non-fungible` assets?

* **Answer** Art

* **Answer** Diamonds

* **Answer** Land Ownership

* What are some potential benefits of using open source libraries such as OpenZeppelin?

* **Answer** They are freely available to use and contribute to under the MIT license.

* **Answer** It's a community-backed project that has implemented many of the communities agreed-upon standards (EIPS/ERCS).

* **Answer** It provides a secure, standardized starting point for various smart contract standards.

Now that the class has been refreshed on fungibility set the stage for today's lesson by introducing the concept of `DeFi`.

* `DeFi` is short for decentralized finance.

* `DeFi` encompasses many of the technologies and paradigms that we have learned throughout the previous unit; however, DeFi is not a particular technology or implementation.

* `DeFi` is a movement within the financial technology sector where future financial systems are being created and deployed with an open, decentralized, and permissionless architecture.

### 2. Instructor Do: ERC721 Non-Fungible Tokens and Events (15 min)

In this activity, the class will be reintroduced to the ERC721 standard, review fungible vs. non-fungible, and demonstrate implementing ERC721 using OpenZeppelin. You will explain the concept of events in solidity and demonstrate defining new events (appraisal, etc.) and associating them with unique ERC721 tokens.

**Files:**

* [Erc721ArtToken.sol](Activities/01-Ins_ERC721_Non-Fungible_Tokens_and_Events/Solved/Erc721ArtToken.sol)

Start by opening [Remix](https://remix.ethereum.org) in your web browser and creating a new contract named `ArtToken.sol`. Set the `pragma` and import the OpenZeppelin libraries for ERC721Full and SafeMath counters.

 ```solidity
 pragma solidity ^0.5.0;

 import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721Full.sol";
 import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/drafts/Counters.sol";
 ```

* In this contract, we will be leveraging the contract for `ERC721Full` and the SafeMath counters data type.

Next, create a new contract named ArtToken that inherits from ERC721Full, for ERC721Full's constructor function's definition pass in the variables that ERC721Full expects, which are a `string` for the `token name` and a `string` for the token's `symbol`. Use `"ArtToken"` for the first parameter and `"ART"` for the second parameter.

 ```solidity
 contract ArtToken is ERC721Full {

 constructor() ERC721Full("ArtToken", "ART") public { }
 }
 ```

* We will be extending the `ERC721Full` contract for our ArtToken contract.

* The `ERC721Full` constructor accepts a `string` for the `token name` and a `string` for the token's `symbol`.

Now define a new counter to keep track of what current `token_id` we are on starting from 0. Apply the `using for` syntax to attach the SafeMath counter library to the counter type and create a new variable named `token_ids` that is of type Counters.counter.

 ```solidity
 using Counters for Counters.Counter;
 Counters.Counter token_ids;
 ```

* In order for us to track the number of tokes that have been minted and to generate the next `token_id`, we will be leveraging the custom Counter data structure from OpenZeppelin.

* Openzeppelin SafeMath counters allows us to increment and decrement a counter without worrying about overflows and other common types of errors.

Represent the artwork's information as a struct named `Artwork` containing these three attributes. A `string` named `name`, a `string` named artist, and a `uint` named `appraisal_value`.

 ```solidity
 struct Artwork {
 string name;
 string artist;
 uint appraisal_value;
 }
 ```

* Each ArtToken will contain one `string` representing a piece of artworks `name`, a second `string` representing the `artist` that created the artwork, and a `uint` representing the last `appraisal_value` of the Artwork.

* In this activity, we will be using a new data structure called a `struct`.

* As you might be able to guess, `struct` is short for `structure`.

* Structs allow you to have `structured collections` of data within a user-defined datatype.

* As you can see, the `struct` that we are creating for this contract contains two `string`s and a `uint`.

* You can think of a struct kind of like a python dictionary in that they are both types of objects containing data, however, make no mistake a struct is a fundamentally different data type than a python dictionary.

Define a new `mapping` named `art_collection` that maps a `uint` to our defined Artwork data structure.

 ```solidity
 mapping(uint => Artwork) public art_collection;
 ```

* We now have to associate each instance of an artwork's information as defined in the `struct` with each art token. This is done by means of a mapping between the `token_id` and the given art token's id.

Define a new event called `Appraisal` that will accept a `uint` named `token_id`, a second `uint` named `appraisal_value` and a string named `report_uri`.

 ```solidity
 event Appraisal(uint token_id, uint appraisal_value, string report_uri);
 ```

* The data that is stored on-chain for each art token is stored in the art_collection mapping, but appraisal reports are far too large to store on-chain.

* Instead, it is a much lower gas price to store appraisal reports in a decentralized storage provider such as IPFS and then referenced on-chain by hash. Calling an event is an easy and cheap way to permanently log a `URI` or `Uniform Resource Identifier`.

Define a function named `registerArtwork`; it accepts the following parameters:

 * address owner,

 * string memory name

 * string memory artist

 * uint initial_value

 * string memory token_uri

 and is a `public` function that `returns` a `uint`.

 ```solidity
 function registerArtwork(address owner, string memory name, string memory artist, uint initial_value, string memory token_uri) public returns(uint) {

 }
 ```

* This function will be responsible for registering a new piece of artwork on the chain.

* The token URI can be a link to some metadata anywhere on the internet. This can be a potential point of centralization, but we will solve that later by using a tool called IPFS.

* In our use case, we will be creating a JSON object that contains a `name`, `description`, and `image` field, then converting it to a special immutable URI with IPFS that ensures that you will always be getting that same piece of data. Essentially, we will be linking to some JSON metadata in a decentralized fashion, but for now, we just need to be able to store a string.

Add the following lines of code inside the `registerArtwork` function for generating the token's id.

 ```solidity
 token_ids.increment();
 uint token_id = token_ids.current();
 ```

* Inside the body of the `registerArtwork` function you must generate the next `token_id`, this is done by incrementing the `token_ids` counter with the `.increment()` method and then by fetching the current count with the `.current()` method; storing it as a `uint` named `token_id`.

Next, inside the `registerArtwork` function, call the internal `_mint` method from `ERC721Full`. Pass the `_mint` function the `owner` value that we defined and the new `token_id` that was generated.

 ```solidity
 _mint(owner, token_id);
 ```

* Now let's mint the new token.

On the next line inside of the `registerArtwork` function, call the internal `_setTokenURI` method from `ERC721Full` and pass it the generated `token_id` as well as the `token_uri` that was passed to the registerArtwork function.

 ```solidity
 _setTokenURI(token_id, token_uri);
 ```

* A typical ERC721 token contains an attached `tokenURI`. That usually links to a JSON object.

On the next line of the `registerArtwork` function, add the generated `token_id` and map it to a new artwork instance with the passed `name`, `artist`, `initial_value`. Then have the `registerArtwork` function return the generated `token_id`.

 ```solidity
 cars[token_id] = Car(vin, 0);
 return token_id;
 ```

* In order to register a piece of art, it's `token_id` must be stored in the defined mapping of art tokens.

* When our `registerArtwork` function finishes creating a new artwork token, it will then return the token's id.

Define a second function named `newAppraisal`; this function will be responsible for reporting a new artwork appraisal by logging it's `report_uri`, it accepts three parameters a `uint` named `token_id`, a second `uint` named `new_value` and a `string memory` representing the `report_uri`. Make `newAppraisal` a public function that returns a `uint`.

 ```solidity
 function newAppraisal(uint token_id, uint new_value, string memory report_uri) public returns(uint) {
 ```

Inside the body of the `newAppraisal` function set the passed token_id's appraisal_value to the new_amount passed to the function. Then `emit` the `Appraisal` event passing it the given `token_id`, the `new_amount` for the last appraisal, and the `report_uri`. Finally return the `new_amount` value.

 ```solidity
 art_collection[token_id].appraisal_value = new_value;

 emit Appraisal(token_id, new_value, report_uri);

 return art_collection[token_id].appraisal_value;
 ```

* This function will be responsible for reporting a new accident by logging it's `report_uri`.

* The `newAppraisal` function does three things:

 * it increments the new appraisal amount for the given `token_id` inside the `art_collection` mapping,

 * it `emits` the `Appraisal` event passing it the given `token_id`, the `new_amount` for the last appraisal and the `report_uri`

 * it returns the current artwork `appraisal_value` after the latest appraisal.

* We have now created a new ERC721 non-fungible token with custom attributes.

If you see a warning like this:

![ERC721 Warning](Images/erc721-warning.png)

This is coming from the OpenZeppelin library and is safe to ignore.

### 3. Students Do: Building the CryptoFax Car Token (20 min)

In this activity, students will implement a non-fungible car token containing an immutable vehicle history using the ERC721 OpenZeppelin contract. This contract will require them to apply their knowledge of SafeMath counters, structs, and events.

**Instructions:**

* [README.md](Activities/02-Stu_Building_CryptoFax_Car_Token/README.md)

**Files:**

* [Solved](Activities/02-Stu_Building_CryptoFax_Car_Token/Solved/CryptoFax.sol)

* [Unsolved](Activities/02-Stu_Building_CryptoFax_Car_Token/Unsolved/CryptoFax.sol)

### 4. Instructor Do: ERC721 + Structs and Events Review (10 min)

Open and review the solved solution from the previous activity.

```solidity
contract CryptoFax is ERC721Full {

 constructor() ERC721Full("CryptoFax", "CARS") public { }
```

* First, we inherited the properties of ERC721Full's contract in our new CryptoFax contract and called the ERC721Full's constructor passing it the name of the token `CryptoFax` and the token symbol `Cars`.

```solidity
 using Counters for Counters.Counter;
 Counters.Counter token_ids;
```

* We used the `using for` syntax to attach the functions of the SafeMath library to the defined Counter type.

* To track the number of tokens that have been minted so that the next `token_id` can be generated, a custom Counter data structure from OpenZeppelin was used.

```solidity
 struct Car {
 string vin;
 uint accidents;
 }
```

* A struct was defined to hold each car's on-chain information, it's `vin` and it's number of `accidents`.

```solidity
 mapping(uint => Car) public cars;
```

* The CryptoFax contract tracks each new token that is minted by storing it's `token_id` and corresponding info for each car.

```solidity
 event Accident(uint token_id, string report_uri);
```

* Here we defined a new event called `Accident` that accepts a `uint` named `token_id`, and a `string` named `report_uri`.

* As mentioned, the data that is stored on-chain for each car token is stored in the cars `mapping`; however, accident reports are far too large to store on-chain. Instead, it is much cheaper (in gas) to store accident reports in a decentralized storage provider such as [IPFS](https://ipfs.io/) and then reference them on-chain by hash.

* Calling an event is an easy and cheap way to permanently log a `URI` or `Uniform Resource Identifier`.

```solidity
 function registerVehicle(address owner, string memory vin, string memory token_uri) public returns(uint) {
 token_ids.increment();
 uint token_id = token_ids.current();

 _mint(owner, token_id);
 _setTokenURI(token_id, token_uri);

 cars[token_id] = Car(vin, 0);

 return token_id;
 }
```

* The `registerVehicle` function is responsible for registering a new vehicle on the chain.

* The `token_ids` counter is first incremented so that a new token can be minted; the new token id is stored as a uint named `token_id`.

* The mint function is then called passing it the owner's address from `registerVehicle` and the new `token_id`.

* The `_setTokenURI` function is then called to set the new token's `URI` based upon it's id.

* A newly defined car with a corresponding `vin` and a given number of `accidents` is then added to the car mapping with it's mapped `token_id`, and the new token_id is returned.

```solidity
 function reportAccident(uint token_id, string memory report_uri) public returns(uint) {
 cars[token_id].accidents += 1;

 // Permanently associates the report_uri with the token_id on-chain via Events for a lower gas-cost than storing directly in the contract's storage.
 emit Accident(token_id, report_uri);

 return cars[token_id].accidents;
 }
```

* The `reportAccident`function is responsible for reporting a new accident by logging it's `report_uri`, it accepts two parameters a `uint` named `token_id` and a `string memory` representing the `report_uri`.

* The `reportAccident` function does three things:

 * it increments the number of accidents for the given `token_id` inside the car's mapping,

 * it `emits` the `Accident` event passing it the given `token_id` and `report_uri`

 * it returns the current number of accidents after the latest accident.

* Remember, you are `emitting` the Accident function in order to trigger the logging of a new accident report.

* Congratulations, you've just built an `ERC721` compliant `non-fungible` token complete with on-chain custom attributes and several linked token `URI`s

Discuss the following review questions with the class:

* Why is a struct a useful data structure.

* **Answer** It allows you to create new dynamic data structures.

* **Answer** It allows you to create data structures that contain multiple types.

* **Answer** It allows you to create objects.

* What are some uses for solidity events.

* **Answer** Events are a cheap way of logging information on the blockchain.

* **Answer** Events alappsApps to update and monitor given values on the blockchain.

* What are some other examples of non-fungible tokens that could be created?

* **Answer** A token that represents a card in a card game.

* **Answer** A token that represents a person's debt.

* **Answer** A token that represents a certification that a person has earned.

### 5. Instructor Do: IPFS: The InterPlanetary File System (15 min)

In this activity, students are introduced to the `IPFS` technology and how it can be used to store immutable, hash-based content-routed data. Students will see first hand that when combined with blockchain, IPFS can store large datasets with the same degree of integrity as on-chain data.

**Files:**

* [Example URI file](Activities/03-Ins_IPFS_The_InterPlanetary_File_System/Solved/erc721example.sol)

Begin by giving the students some background on IPFS, what it is, how it works.

* So what is IPFS?

* IPFS stands for `InterPlanetary Filesystem`, it is both:

 * a `Protocol`

 * a `Network`

 * and a `Filesystem`

* So what exactly does this mean and how does it all fit together?

* For two users to exchange data with one another across the internet, they need a common set of rules for how the information is sent between them; this is a `communication protocol`.

* `Communication protocols` are usually built within a stack known as a `protocol suite`. For example, the `internet protocol suite` is widely used today, and of the protocols that make up the suite `HyperText Transfer Protocol` or `HTTP` is the foundation for communication.

* Another important piece is known as the `system's architecture` or how the actual computers within the network can communicate with one another. Traditionally this is done in a `client-server` model; however, IPFS leverages a `peer-to-peer` network model of connection.

* In a typical `client-server` model, `centralized` servers store data that is accessed via `location-based addressing`. This provides an easy way to secure and manage data in a scalable manner, though it doesn't come without its drawbacks.

 * Since data is stored on `centralized` servers, anyone with access to those servers, whether an authorized admin or a hacker with malicious intent, can alter and remove data. This poses problems in both the realms of privacy and security because, in this model, control of the server is equal to control of the data.

 * In `location-based addressing`; a piece of data is recognized by location as opposed to its content; this means that to access a piece of data, you must go to its specific location even if the same data is available from a closer source.

 * This also means a client has no defacto way to tell if the data it has received has been altered because the client isn't concerned with what the data is but rather where it is.

 * The `client-server` model works well for websites and small pieces of data, but it's not the most efficient when it comes to big pieces of data.

* IPFS hopes to address these issues with the traditional `client-server` model with the use of a distributed `peer to peer` file-sharing system.

Now that the students have a general grasp on what IPFS is and the purposes that it is trying to serve. Introduce the class to the Pinata service and how `IPFS` can be a valuable tool for building dApps and decentralized systems.

Open a web browser and navigate to the [Pinata Website](https://pinata.cloud/).

![Pinata](Images/pinata.png)

* Pinata is a file pinning service for IPFS. It allows you to host files on the IPFS network and reference them by hash; they also provide a free gateway for communicating with IPFS.

Click the `Try it for Free` or the `Signup` and register for a free account. If you already have an account login to the pinata dashboard.

![Pinata Signup](Images/pinata_singup.png)

![Pinata Login](Images/pinata_login.png)

* Pinata accounts are free and allow you to pin up to `1 gigabyte` of files on IPFS.

* The pinata website provides a simple user interface for developers to upload and access files on IPFS.

Open the [Example URI file](Activities/03-Ins_IPFS_The_InterPlanetary_File_System/Solved/example_uri.json) and display it to the class.

```json
{
 "name": "Mona Lisa",
 "description": "One of the most famous works of art by Leonardo da Vinci",
 "image": "ipfs://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq/I/m/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
}
```

* As previously mentioned, each `ERC721` token typically has an associated `token URI` that is stored on some off-chain storage provider such as IPFS. A URI may resolve to any file, but an ERC721 token URI usually looks something like this.

Click on the `Pinata Upload` link in the website's top navigation bar.

![Pinata Upload Link](Images/pinata_upload_link.png)

Now click the `Browse` button and upload the [Example URI file](Activities/03-Ins_IPFS_The_InterPlanetary_File_System/Solved/example_uri.json)

![Pinata Upload](Images/pinata_upload.png)

* Let's upload the example `token URI` to IPFS for an Artwork Token.

* Uploading a file on Pinata is as simple as clicking `Browse` and then clicking on `Upload`.

After the upload is successful, click the `Pin Explorer` link in the website's top navigation bar.

![Pin Explorer Link](Images/pinata_pin_explorer_link.png)

* Let's take a look at the file we uploaded by going to the `Pinata Explorer` page.

![Pinata Explorer](Images/pinata_pin_explorer.png)

* As you can see, our Artwork Token's JSON file shows up in our list of pinned files; make a note of the corresponding IPFS hash.

![Pin Hash Click](Images/pinata_pin_hash.png)

* If we click the hash link, pinata will even generate a link to the file on IPFS accessible through pinata's free IPFS gateway.

Make a note to the class that the Pinata gateway is a point of centralization. However, dApps can leverage the use of multiple IPFS gateways to mitigate this.

![Gateway File](Images/pinata_gateway_file.png)

* By default, pinata generates a connection to the IPFS network through their free IPFS gateway; however, we will be using a direct `ipfs://` link to the hash that will be resolved through the IPFS browser extension.

Navigate to the [IPFS Browser Companion github](https://github.com/ipfs-shipyard/ipfs-companion) and install the browser extension for your desired browser.

* You do not need to install the IPFS Desktop version.

* You also do not need to worry about if you cannot connect to an IPFS node, as the browser extension will fallback to the IPFS.io gateway. You do not need to install an IPFS node if you don't want to, though it is valuable to explore down the line.

 ![IPFS Install Links](Images/ipfs-browser-companion.png)

In your browser, open the [CID IPFS Website](https://cid.ipfs.io) and convert the CIDv0 hash to a CIDv1 hash.

![CID Converter](Images/cid-converter.png)

* Originally, the CIDv0 standard allowed for URL hashes that supported both upper and lowercase characters, but this breaks in many browsers nowadays since some of them automatically make your URL lowercase. Since the hash relied on case sensitivity to encode the necessary data, this broke it.

* CIDv1 is a longer, lowercase hash that also contains more metadata that can be converted for human-readable info in some applications. Since we're alway at the cutting edge, we are going to opt for the newer, more compatible standard.

* Pinata is a useful service, but they have yet to update their file pinning  website frontend to support CIDv1. In order to avoid bugs, we are going to convert the `IPFS hash` with a free CIDv1 converter.

Now to test the browser extension copy the files new CIDv1 `IPFS hash` and prepend `ipfs://` to the front of it, e.g., [ipfs://bafybeiamajrnvskqn4s7swwtnac33ewoo6dib7vx25tlhcnt7cbeysse4m](ipfs://bafybeiamajrnvskqn4s7swwtnac33ewoo6dib7vx25tlhcnt7cbeysse4m). Demonstrate creating the link and opening it in your browser.

* Once the IPFS browser extension is installed, files on IPFS can be accessed at `ipfs://whatever your file hash is`.

* When pasting an IPFS URI into our browser, we need to make sure it is navigating directly to the `ifps://` scheme, and not simply searching the string on Google.

Now navigate to [Remix](http://remix.ethereum.org/). Then open the example contract for the `Artwork Token` and compile/deploy the contract on your local ganache blockchain.

You may have to increase the `Gas Limit`, but once the contract has successfully deployed, click on the deployed contract and click the `newAppraisal` function. Fill in the fields with a generated address from your wallet, some sample details about the artwork, and the token URI; then call the function. The data you enter should be:

![Register Artwork](Images/remix_register_artwork.png)

* owner : `YOUR_ADDRESS_HERE`

* name: `Mona Lisa`

* artist: `Leonardo da Vinci`

* initial_value: `62,000,000`

* token_uri: `ipfs://bafybeiamajrnvskqn4s7swwtnac33ewoo6dib7vx25tlhcnt7cbeysse4m`

Congratulate them, that was a lot of new information to take in; then briefly introduce the next activity.

* We've now deployed our ERC721 non-fungible token with a linked IPFS `token URI`. In the next activity, you will be uploading a similar token URI file to Pinata for your CryptoFax car token.

### 6. Students Do: IPFS + Blockchain (15 min)

In this activity, students will upload a Car TokenURI to IPFS via Pinata and link them to a transaction via their ERC721 contracts.

**Instructions:**

* [README.md](Activities/04-Stu_IPFS_+_Blockchain/README.md)

**Files:**

* [Example Token URI](Activities/04-Stu_IPFS_+_Blockchain/Unsolved/example_uri.json)

### 7. Instructor Do: IPFS Review (10 min)

Discuss the following review questions with the class about the general concepts of IPFS.

* What are some potential issues that IPFS seeks to solve?

* **Answer** Inefficiencies in the web such as `duplicate files`.

* **Answer** Inefficiencies in the web such as having to route to a faraway server to get the file you need when it might be right next door.

* **Answer** Problems with security and file integrity, such as not knowing whether or not files you have accessed over the web have changed.

* **Answer** Problems with the security of centralized servers providing a centralized attack vector.

* What are some potential use cases of IPFS?

* **Answer** Hosting any file that you want to maintain an immutable copy of.

* **Answer** Hosting any file that needs to be censorship-resistant.

* **Answer** Hosting very-large files between organizations.

* **Answer** Hosting any file in general.

Have the class take a moment to brainstorm some potential use-cases for IPFS; potential use-cases include:

* **Potential Answer** An open street map application that shares panoramic photos of streets through a decentralized platform.

* **Potential Answer** A static website host.

* **Potential Answer** A decentralized social platform where users can upload photos.

* **Potential Answer** A p2p chat with file sharing.

---

### 8. BREAK (15 min)

---

### 9. Instructor Do: The Accident Report System (15 min) (Critical)

Now that students understand that IPFS is a content-routed system that works against hashes instead of IP addresses, it's time to put the systems together to make an Accident Report System.

In this activity, you will demonstrate uploading a sample "accident report" in JSON format to IPFS via the Pinata API, then permanently record the report's IPFS URI to the blockchain via the `reportAccident` function on the `CryptoFax` contract using a transaction generated with Web3.py.

**Files:**

* [crypto.py (web3.py + ipfs functionality)](Activities/05-Ins_Filters_Web3_IPFS/Solved/crypto.py)

* [accident.py (accident report system)](Activities/05-Ins_Filters_Web3_IPFS/Solved/accident.py)

* [CryptoFax.json (contract ABI, pasted from your compiled contract in Remix)](Activities/05-Ins_Filters_Web3_IPFS/Solved/CryptoFax.json)

First, create a new working directory called `accident`, and `cd` into it:

```bash
mkdir accident
cd accident
```

Create a file called `.env`. This is where we will store all of the environment variables needed in our Accident Report dApp.

```env
PINATA_API_KEY=
PINATA_SECRET_API_KEY=
WEB3_PROVIDER_URI=http://127.0.0.1:8545
CRYPTOFAX_ADDRESS=
```

* We will need to use our `.env` file to store our Pinata API credentials, as well as point Web3.py to our local Ganache chain via the `WEB3_PROVIDER_URI` variable.

* We also need to store the address of the `CryptoFax` contract we deployed here.

Fetch your Pinata API credentials by navigating to your [Pinata Account Page](https://pinata.cloud/account) and copying them into the `.env` file.

Paste the address of the deployed `CryptoFax` contract into the `CRYPTOFAX_ADDRESS` variable.

Next, create a file called `crypto.py`. This is where we will be writing the functions for uploading to IPFS via Pinata and initializing our contract via its ABI.

In this file, you will need to import the environment variables via the `python-dotenv`:

```python
from dotenv import load_dotenv

load_dotenv()
```

* This will now load the previously defined environment variables. The `python-dotenv` package automatically imports the environment variables from a `.env` file in your project directory.

*Note:* This requires the `python-dotenv` package for importing private keys and other environment variables. You may need to install it by using:

```bash
pip install python-dotenv
```

Now it's time to set up a `POST` request to the Pinata API that will pin arbitrary JSON data to IPFS.

First, import the `requests` library, as well as `json` and `os`:

```python
import requests
import json
import os

from dotenv import load_dotenv
```

Now, its time to set the request headers that Pinata expects. Open up the [Pinata Documentation](https://pinata.cloud/documentation#PinJSONToIPFS) for the endpoint `pinJSONToIPFS`.

![Pinata Headers](Images/pinata-headers.png)

* As you can see, the endpoint is `https://api.pinata.cloud/pinning/pinJSONToIPFS`, and we need to set the following headers:

 * `Content-Type` which is going to be `application/json` to specify that we're sending JSON.

 * `pinata_api_key` from our account.

 * `pinata_secret_api_key` from our account.

* Essentially, all we need to do is set up an object with these headers for later, then create a function that sends a `POST` request to that endpoint, with the JSON data that we want to pin to IPFS.

Below your imports, define the following variable:

```python
headers = {
 "Content-Type": "application/json",
 "pinata_api_key": os.getenv("PINATA_API_KEY"),
 "pinata_secret_api_key": os.getenv("PINATA_SECRET_API_KEY"),
}
```

* This object will now contain the keys that we defined in our `.env` file previously, and can be used as the request's header when sending JSON to IPFS with our account.

Next, define a function called `pinJSONToIPFS`, which will `POST` to the `pinJSONToIPFS` Pinata endpoint.

First, double-check the response that Pinata will send back when posting to the endpoint by scrolling down to the `Response` section on the [Pinata Documentation](https://pinata.cloud/documentation#PinJSONToIPFS):

![Pinata Response](Images/pinata-response.png)

* As you can see, it will return a JSON object that will contain a key called `IpfsHash` that returns the IPFS hash of the data we send, that we can use as a URI later.

```python
def pinJSONtoIPFS(json):
 r = requests.post(
 "https://api.pinata.cloud/pinning/pinJSONToIPFS", data=json, headers=headers
 )
 ipfs_hash = r.json()["IpfsHash"]
 return f"ipfs://{ipfs_hash}"
```

* In this request, we are simply taking in some JSON object as input, then sending a `POST` request to the `pinJSONToIPFS` endpoint on Pinata. We use the headers defined above to authorize our request.

* Then, we return the `IpfsHash` value from the JSON response that Pinata defines inside of an `f` string. The final output is an IPFS URI, formatted like `ipfs://some_hash_here`.

Up to this point, this process should be pretty familiar. The last Pinata related item we need to take care of is a function called `convertDataToJSON` that will take our user input and convert it to a JSON object formatted in a way that allows us to set some options in the Pinata API:

```python
def convertDataToJSON(time, description):
 data = {
 "pinataOptions": {"cidVersion": 1},
 "pinataContent": {
 "name": "Example Accident Report",
 "description": description,
 "image": "ipfs://bafybeihsecbomd7gbu6qjnvs7jinlxeufujqzuz3ccazmhvkszsjpzzrsu",
 "time": time,
 },
 }
 return json.dumps(data)
```

* In this function, we are simply taking in a `time` and `description` that we'll accept as user input later, then setting up a dictionary called `data` that contains a few fields.

* The first field, `pinataOptions`, tells the API to use `CIDv1` as the IPFS URL format. This just simply means to use the latest version of the way that IPFS generates the final address that allows for more metadata to be encoded versus using `CIDv0`, which are the shorter, case-sensitive URIs that IPFS used initially.

* `pinataContent` contains the object that will be pinned to IPFS by Pinata. Only what is in this field will be uploaded to IPFS.

* Finally, we are simply converting the `data` dictionary into a JSON string by using `json.dumps(data)`. The `json.dumps` function takes in a Python dictionary and outputs a compatible JSON `string`. Remember, JSON stands for `JavaScript Object Notation`. JSON originally came from JavaScript and is used in many other systems. However, Python needs to convert the way it stores data in dictionaries into the JSON format.

Now it's time to set up the functions we need to set up our `CryptoFax` contract object in Python using `web3.py`.

Before that, we need to get our contract's ABI. Hop over to Remix, make sure you have `CryptoFax` selected, head to the compile tab, and copy the ABI:

![CryptoFax ABI](Images/cryptofax-abi.png)

Paste this into a new file called `CryptoFax.json`. Make sure it is in the same working directory as the `crypto.py` and `.env` files.

Next, in `crypto.py`, add the following imports:

```python
from pathlib import Path

from web3.auto import w3
```

* Pathlib will be used to fetch our `CryptoFax.json` ABI.

* Web3.py will accept this ABI, plus the address we defined in our `.env` file, and output a contract object that we can use to interact with the `CryptoFax` contract.

* Since we configured `WEB3_PROVIDER_URI` in `.env`, `web3.auto` will automatically recognize the Ganache network and automatically connect and use the same accounts that Ganache generates. No need to work with private keys when using `web3.auto` and Ganache!

Now, create one last function in `crypto.py`:

```python
def initContract():
 with open(Path("CryptoFax.json")) as json_file:
 abi = json.load(json_file)

 return w3.eth.contract(address=os.getenv("CRYPTOFAX_ADDRESS"), abi=abi)
```

* This function opens up the `CryptoFax.json` ABI and converts it to a JSON object. Then, it returns a contract object using the `CRYPTOFAX_ADDRESS` we defined in our environment, and the ABI object. This is all we need to create the object we need to interact with our contract.

At this point, your code should match the provided [crypto.py](Activities/05-Ins_Filters_Web3_IPFS/Solved/crypto.py).

Finally, it's time to build the rest of the Accident Report System.

We'll need to create one more file called `accident.py`.

* `accident.py` is going to be a quick command-line interface between the person reporting the accident, the Pinata API, and the final transaction sent to the contract.

* The flow of the application will start by asking the user `When did the accident occur?` and for a `Description of the accident`, and the `Token ID` associated with the report.

* Next, it will take these three variables, `time`, `description`, and `token_id` and upload the report to IPFS in JSON format. Finally, it will create a transaction that will `emit` an `Accident` event on the contract, passing in the `report_uri` (the URL of the report on IPFS) and `token_id`, permanently recording that event on the blockchain.

In this file, import the following:

```python
from crypto import convertDataToJSON, pinJSONtoIPFS, initContract, w3

from pprint import pprint
```

* We're importing these functions individually, as we won't be using all of the imports in `crypto`, like `json` and `os` and we don't want to pollute our import namespace.

* `pprint` will be used to pretty-print our transaction receipts later.

Below the imports, add the following global variable:

```python
cryptofax = initContract()
```

* We can use this object to interact with our contract functions and events later.

Create a new function to create the accident report:

```python
def createAccidentReport():
 time = input("Date of the accident: ")
 description = input("Description of the accident: ")
 token_id = int(input("Token ID: "))

 json_data = convertDataToJSON(time, description)
 report_uri = pinJSONtoIPFS(json_data)

 return token_id, report_uri
```

* In this function, we are taking in the three variables as user input. We are also making sure to convert the `token_id` into a number.

* Then, we convert that data into the JSON object we want to send to Pinata via the `convertDataToJSON` function.

* We capture the final IPFS URI from our `pinJSONToIPFS` function, passing in the JSON data we want to upload and return the `token_id` and `report_uri` variables.

Next, we'll need to create the function that will etch the event to the blockchain:

```python
def reportAccident(token_id, report_uri):
 tx_hash = cryptofax.functions.reportAccident(token_id, report_uri).transact(
 {"from": w3.eth.accounts[0]}
 )
 receipt = w3.eth.waitForTransactionReceipt(tx_hash)
 return receipt
```

* In this function, we are calling the `reportAccident` function by using `cryptofax.functions.reportAccident`, and passing in our `token_id` and `report_uri`. This should match the parameters we set in our Solidity code.

* The `.transact` call creates and sends the transaction in one function, but we need to make sure to set our default `from` user to something like `w3.eth.accounts[0]`. This `accounts` array comes from the accounts that Ganache generates for you, so feel free to use any of them, or reference one specifically by index.

* Lastly, we wait for the transaction receipt from our chain and return it.

At this point, all we need to to is collect the data from the command line:

```python
def main():
 token_id, report_uri = createAccidentReport()

 receipt = reportAccident(token_id, report_uri)

 pprint(receipt)
 print("Report IPFS Hash:", report_uri)


main()
```

* What this main function does is simply collect the `token_id` and `report_uri` from the `createAccidentReport` function, pass the info to `reportAccident`, and pretty prints the Ethereum transaction receipt and the IPFS Hash of the report.

Feel free to demonstrate a sample report. Make sure you have previously called the `registerVehicle` function and have at least one Car Token on-chain and have its `token_id` available.

* What if we wanted to fetch all of the `Accident` report events relating to our `token_id`?

Simply add the following function:

```python
def getAccidentReports(token_id):
 accident_filter = cryptofax.events.Accident.createFilter(
 fromBlock="0x0", argument_filters={"token_id": token_id}
 )
 return accident_filter.get_all_entries()
```

* This function takes in a `token_id`, then creates a `Filter` on the `Accident event` available in the contract object. The filter captures from block `0x0` (genesis), to the current block, and makes sure that the `token_id` matches the argument parameters.

* Then, it returns all of the entries the filter found, by calling `accident_filter.get_all_entries()`.

We can make this a simple command-line interface by importing `sys`, and parsing the arguments from the command line and modifying our `main` function:

```python
import sys

...

def main():
 if sys.argv[1] == "report":
 token_id, report_uri = createAccidentReport()

 receipt = reportAccident(token_id, report_uri)

 pprint(receipt)
 print("Report IPFS Hash:", report_uri)

 if sys.argv[1] == "get":
 token_id = int(sys.argv[2])

 car = cryptofax.functions.cars(token_id).call()
 reports = getAccidentReports(token_id)

 pprint(reports)
 print("VIN", car[0], "has been in", car[1], "accidents.")
```

* `sys.argv` is the list of arguments passed from the command line. This is a universal concept in most general-purpose programming languages. This is the list that other programs use to parse out the arguments you send them, like `--help` or `--port`.

* In Python, `sys.argv[0]` is always the name of the script. `sys.argv[1]` is the first argument, and so on.

For example:

```
 sys.argv[0] sys.argv[1] sys.argv[2]
python accident.py report
python accident.py get 1
```

* We can use this to pass the word `get` as the first argument, and a `token_id` as the second.

* Then, we simply check if the first argument is a `report` or a `get`, and proceed accordingly.

* In our `get` flow, we simply collect the `token_id`, then fetch the `Car` struct from the `cars` mapping to get details from the contract, then we fetch the accident reports from our event filter using `getAccidentReports`, and pretty-print the results.

At this point, your code should match the provided [accident.py](Activities/05-Ins_Filters_Web3_IPFS/Solved/accident.py).

Test out the system by creating an accident report, and then fetching it using the following commands (you can replace the `token_id`):

```bash
python accident.py report
python accident.py get 1
```

Voila! A complete vehicle accident report system that permanently stores accident reports to the blockchain and IPFS. Now it's time for the students to build the same system.

### 10. Students Do: Building the Accident Report System (20 min)

In this activity, students will build the same Accident Report System, leveraging IPFS and event filters.

Send out the instructions and the starter code, and have TAs circulate the room, ensuring that students are following the instructions properly.

**Instructions:**

* [README.md](Activities/06-Stu_Accident_Report_System/README.md)

**Files:**

* [crypto.py](Activities/06-Stu_Accident_Report_System/Unsolved/crypto.py)

* [accident.py](Activities/06-Stu_Accident_Report_System/Unsolved/accident.py)

* [.env](Activities/06-Stu_Accident_Report_System/Unsolved/.env)

If students are having difficulties, make sure of the following:

* The student has installed the `python-dotenv` package. This can be done by running the following command:

```bash
pip install python-dotenv
```

* The `header` object is properly configured, and that the Pinata API secrets are saved to the `.env` file properly.

* The `.env` file contains the proper values (all should be filled in).

* The ABI is copied from Remix and pasted into the `CryptoFax.json` file.

* Students are `cd`'d into the same directory as the rest of the `.env`, `CryptoFax.json`, `crypto.py`, and `accident.py` files.

* Ganache is running and the `WEB3_PROVIDER_URI` points to it.

### 11. Instructor Do: Review Accident Report System (10 min)

**Files:**

* [crypto.py](Activities/06-Stu_Accident_Report_System/Solved/crypto.py)

* [accident.py](Activities/06-Stu_Accident_Report_System/Solved/accident.py)

Open `crypto.py` and explain the following:

* This file is used to establish functions dealing with the Pinata API and creating the function for returning the `cryptofax` contract object.

* The `requests` library is used to `POST` some JSON data to Pinata, and return the corresponding IPFS URI.

Open up `accident.py` and explain the following:

* The `createAccidentReport` function collects all of the user input, including the `time`, `description`, and `token_id`, converts it to valid JSON, then pins it to IPFS.

* The `reportAccident` function takes in the final `token_id` and `report_uri` and sends it as a transaction to the `CryptoFax` contract's `reportAccident` function, which emits an `Accident` event that we can filter for later.

* The `getAccidentReports` function simply filters for all `Accident` events on the contract that match the `token_id`, from the genesis block to now.

* The `main` function checks the command line arguments and decides which path to take. If the `sys.argv[1]` the argument is `report`, meaning we ran `python accident.py report` in our terminal, then we create and print an accident report.

* If `sys.argv[1]` is `get`, we follow the `getAccidentReports` flow. By running a command like `python accident.py get 1`, we can parse out the `sys.argv[2]` to be the `token_id` and use that for our event filter.

Ask for any remaining questions before moving on.

### 12. Instructor Do: Intro to Project 3 (25 min)

Congratulate the class on having made it this far!

Explain that, over the next two class weeks, students will work in groups to complete a capstone project for FinTech.

Explain that students can choose any topic from any section of the course as their capstone project. Point out that this allows them to align their capstone project with their specific career goals, and that the final project does not have to focus on Blockchain.

Tell students that they will also be able to choose their teams of 2-6 students for this final project. Students are also able to request placement on a team by the instructional staff.

Explain that the rest of the class will be dedicated to working on their final projects.

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
