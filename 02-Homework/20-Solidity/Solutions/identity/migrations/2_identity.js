const Identity = artifacts.require("Identity");

module.exports = function(deployer) {
  const params = {
    name: "Alec M. Wantoch",
    email: "awantoch@trilogyed.com",
    phone: "333-333-3333",
    location: "Earth, Milky Way"
  }
  deployer.deploy(Identity, params.name, params.email, params.phone, params.location);
};
