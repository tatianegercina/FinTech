### 6. Students Do: Integrating a Pre-Built Frontend (15 min)

In this activity, students will integrate the same frontend code with their `CryptoRight` contracts, and upload a few sample copyrights using the interface.

Send out the instructions and have TAs circulate the class.

**Instructions:**

* [README.md](Activities/06-Stu_Integrating_Frontend/README.md)

**Files:**

* [index.html](Activities/06-Stu_Integrating_Frontend/Resources/cryptoright-frontend/index.html)

* [dapp.js](Activities/06-Stu_Integrating_Frontend/Resources/cryptoright-frontend/dapp.js)

* [CryptoRight.json](Activities/06-Stu_Integrating_Frontend/Resources/cryptoright-frontend/CryptoRight.json)

Have the TAs ensure that students:

* Are running the `python -m http.server 8000` command **only** when `cd`'d directly within the directory.

* Have replaced the `contract_address` variable in the `dapp.js` file with their deployed contract.

* Have successfully implemented the contract. If the contract is not implemented properly, the frontend will not function.

### 7. Instructor Do: Frontend Review (5 min)

**Files:**

* [dapp.js](Activities/06-Stu_Integrating_Frontend/Resources/cryptoright-frontend/dapp.js)

Open the solution and explain the following:

* By setting `contract_address` to point at our deployed contract, the frontend is able to communicate with the contract via MetaMask.

* Since our contract was built to spec, the ABI generated will be the same as any other contract built to the same spec. This allows the frontend to be developed independently from the contract.

* The dApp uploads an image to IPFS, then takes that images URI and stuffs it into JSON object that also contains `name` and `description`, and uploads that to IPFS. The final URI is used for the `reference_uri` when calling the `copyrightWork` or `openSourceWork` functions on the contract.

Ask for any remaining questions before moving on.
