pragma solidity ^0.5.0;

contract Identity {
    address owner;
    string public name;
    string public email;
    string public phone;
    string public location;

    address payable[] addresses;

    constructor(
        string memory _name,
        string memory _email,
        string memory _phone,
        string memory _location
    ) public {
        owner = msg.sender;
        name = _name;
        email = _email;
        phone = _phone;
        location = _location;
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

    function setPhone(string memory newPhone) public onlyBy(owner) {
        phone = newPhone;
        emit infochanged("phone", newPhone);
    }

    function setLocation(string memory newLocation) public onlyBy(owner) {
        location = newLocation;
        emit infochanged("location", newLocation);
    }

    function addAddress(address payable newAddress) public onlyBy(owner) {
        addresses.push(newAddress);
    }

    function getAddress(uint256 index) public view returns(address payable selectedAddress) {
        return addresses[index];
    }
}
