### 5. Instructor Do: Frontend Introduction (10 min)

In this activity, you will demonstrate combining the `CryptoRight` contract with a pre-made frontend.

**Files:**

* [index.html](Activities/05-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/index.html)

* [dapp.js](Activities/05-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/dapp.js)

* [CryptoRight.json](Activities/05-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend/CryptoRight.json)

Explain to the class:

* Since we built our `CryptoRight` contract to spec, we should be able to integrate a frontend that was designed against the same interface.

* In this scenario, a frontend developer built a graphical interface using the specification while you implemented the contract.

Copy the files linked above into a new directory, or copy the [cryptoright-frontend](Activities/05-Ins_Integrating_Frontend_Intro/Resources/cryptoright-frontend) folder into your workspace, to a project folder called `cryptoright-frontend`.

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
