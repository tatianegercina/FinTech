pragma solidity ^0.5.0;

contract Identity {
  address public owner;
  string public name;
  string public email;
  string public website;
  string public github;
  string public image;
  string public bio;

  address payable[] addresses;

  constructor(
    string memory _name,
    string memory _email,
    string memory _website,
    string memory _github,
    string memory _image,
    string memory _bio
  ) public {
      owner = msg.sender;
      name = _name;
      email = _email;
      website = _website;
      github = _github;
      image = _image;
      bio = _bio;
  }

  modifier onlyBy(address _account) {
    require(msg.sender == _account, "Not authorized!");
    _;
  }

  event infochanged(string info, string value);

  function setOwner(address newOwner) public onlyBy(owner) {
    owner = newOwner;
  }

  function setName(string memory newName) public onlyBy(owner) {
    name = newName;
    emit infochanged("name", newName);
  }

  function setEmail(string memory newEmail) public onlyBy(owner) {
    email = newEmail;
    emit infochanged("email", newEmail);
  }

  function setWebsite(string memory newWebsite) public onlyBy(owner) {
    website = newWebsite;
    emit infochanged("website", newWebsite);
  }

  function setGithub(string memory newGithub) public onlyBy(owner) {
    github = newGithub;
    emit infochanged("github", newGithub);
  }

  function setImage(string memory newImage) public onlyBy(owner) {
    image = newImage;
    emit infochanged("image", newImage);
  }

  function setBio(string memory newBio) public onlyBy(owner) {
    bio = newBio;
    emit infochanged("bio", newBio);
  }

  function addAddress(address payable newAddress) public onlyBy(owner) {
    addresses.push(newAddress);
  }

  function getAddress(uint256 index) public view returns(address payable selectedAddress) {
    return addresses[index];
  }

  function getAddressCount() public view returns(uint256) {
    return addresses.length;
  }

  function delAddress(uint256 index) public onlyBy(owner) {
    delete addresses[index];
  }

}
