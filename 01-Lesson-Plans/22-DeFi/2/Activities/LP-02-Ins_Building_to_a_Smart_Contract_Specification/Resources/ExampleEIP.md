# EIP 333: ERC-333 Copyright Standard

## Simple Summary

A standard interface for copyright contracts.

## Abstract

The following standard allows for the implementation of a standard API for copyright claims within smart contracts. This standard provides basic functionality to register and create new claims, as well as allowing the owner of a copyrighted work to transfer or renounce ownership of said work.

## Motivation

 A standard interface for copyright would allow copyrights to be used, leveraged and referenced by applications such as wallets and exchanges.

## Specification

### Methods

#### Notes:

  * The following specifications use syntax from Solidity 0.5.0 (or above)

#### copyright_uri:

Accepts a given `copyright_id` as a `uint` and returns a mapped `string` for the copyright's `reference_uri`.

```Solidity
function copyright_uri(uint copyright_id) public returns(string memory reference_uri);
```

#### copyright_owner:

Accepts a given `copyright_id` as a `uint`and returns a mapped `address` for the `copyright_owner`.

```solidity
function copyright_owner(uint copyright_id) public returns(address copyright_owner);
```

#### copyrightWork:

Generates a new `copyright_id` of type `uint` and maps it to a given `reference_uri` by calling `copyright_uri`. Also maps the genrated `copyright_id` to the address of the current `msg.sender` by calling `copyright_owner`.

Must fire the Copyright event.

```Solidity
function copyrightWork(string memory reference_uri) public
```

### openSourceWork

Generates a new `copyright_id` of type `uint` and maps it to a given `reference_uri` by calling `copyright_uri`.

```Solidity
function openSourceWork(string memory reference_uri) public
```

#### renounceCopyrightOwnership

Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000 address in order to "open source" the copyright, and prevent anyone from modifying it further.

```Solidity
function renounceCopyrightOwnership(uint token_id) external;
```

#### transferCopyrightOwnership

Re-maps a given copyright ID to a new copyright owner.

```Solidity
   function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id)
```

### Events

#### Copyright

MUST trigger whenever ownership of a copyright is transferred.

```Solidity
    event Copyright(uint copyright_id, address owner, string reference_uri);
```

### OpenSource

MUST trigger whenever a new OpenSource copyright is created.

```Solidity
event OpenSource(uint copyright_id, string reference_uri);
```

### Transfer

MUST trigger whenever a copyright is transferred.

```Solidity
event Transfer(uint copyright_id, address new_owner);
```
