import identityJson from "./build/contracts/Identity.json";

const Web3 = require("web3");

const contractAddress = "0xEFEcaE036d15009835f485eD1DE704e6783d3E41";

const dApp = {
  ethEnabled: function() {
    // If the browser has injected Web3.js
    if (window.web3) {
      // Then replace the old injected version by the latest build of Web3.js version 1.0.0
      window.web3 = new Web3(window.web3.currentProvider);
      window.ethereum.enable();
      return true;
    }
    return false;
  },
  init: async function() {
    if (!this.ethEnabled()) {
      alert("Please install MetaMask to use this dApp!");
    }
    this.accounts = await window.web3.eth.getAccounts();
    this.contractAddress = $("#id-address").val() || contractAddress;
    this.identityContract = new window.web3.eth.Contract(
      identityJson.abi,
      this.contractAddress,
      { defaultAccount: this.accounts[0] }
    );
    console.log("Contract object", this.identityContract);
  },
  collectVars: async function() {
    // get basic variables
    this.name = await this.identityContract.methods.name.call();
    this.website = await this.identityContract.methods.website.call();
    this.email = await this.identityContract.methods.email.call();
    this.github = await this.identityContract.methods.github.call();
    this.image = await this.identityContract.methods.image.call();
    this.bio = await this.identityContract.methods.bio.call();

    this.totalAddresses = Number(await this.identityContract.methods.getAddressCount.call());

    // get addresses from array in parallel
    const promises = [];
    for (let i = 0; i < this.totalAddresses; i++) {
      promises.push(this.identityContract.methods.getAddress(i).call());
    }
    this.addresses = await Promise.all(promises);
  },
  addAddress: function() {
    const address = $("#id-add-address").val();
    this.identityContract.methods.addAddress(address).send({}, ((error) => {
      if (error) alert(error);
      window.dApp.updateUI();
    }));
  },
  delAddress: function(index) {
    this.identityContract.methods.delAddress(index).send({}, ((error) => {
      if (error) alert(error);
      window.dApp.updateUI();
    }));
  },
  setAdmin: async function() {
    // if account selected in MetaMask is the same as owner then admin will show
    if (this.accounts[0] !== await this.identityContract.methods.owner.call()) {
      $(".id-admin").hide();
    } else {
      $(".id-admin").show();
    }
  },
  updateUI: async function() {
    // check if new contract and reinitialize if different
    if (this.contractAddress !== $("#id-address").val() && $("#id-address").val()) {
      await this.init();
    }
    // refresh variables
    await this.collectVars();

    // set basic values
    $("#id-address").val(this.contractAddress);
    $("#id-name").html(this.name);
    $("#id-website").attr("href", this.website);
    $("#id-email").attr("href", `mailto:${this.email}`);
    $("#id-github").attr("href", this.github);
    $("#id-image").attr("src", this.image);
    $("#id-bio").html(this.bio);

    // set array of addresses
    $("#id-addresses").html("");
    this.addresses.forEach((account, index) => {
      // don't show blank addresses
      if (account !== "0x0000000000000000000000000000000000000000") {
        $("#id-addresses").append(
          `<p>${account} <i onclick="window.dApp.delAddress(${index})"
          class="fa fa-times-circle id-admin" aria-hidden="true"></i></p>`
        );
      }
    });
    $("#id-add-address").val("");

    // hide or show admin functions based on contract ownership
    await this.setAdmin();
  },
  main: async function() {
    // Initialize web3
    await this.init();
    await this.updateUI();
  }
};

window.dApp = dApp;
window.dApp.main();
