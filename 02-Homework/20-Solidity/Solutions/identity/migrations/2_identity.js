const Identity = artifacts.require("Identity");

module.exports = function(deployer) {
  const params = {
    name: "Satoshi Nakamoto",
    email: "satoshi@vistomail.com",
    website: "https://bitcoin.org",
    github: "https://github.com/trottier/original-bitcoin",
    image: "https://en.bitcoinwiki.org/upload/en/images/5/5b/Satoshi-Nakamoto-who-is.jpg",
    bio: "Pushing forward the state of the art in decentralized technology"
  };
  deployer.deploy(Identity, params.name, params.email, params.website, params.github, params.image, params.bio);
};
