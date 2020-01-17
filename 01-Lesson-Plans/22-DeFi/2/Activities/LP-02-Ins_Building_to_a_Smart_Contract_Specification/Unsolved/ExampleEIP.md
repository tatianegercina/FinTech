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

#### copyrights:

Accepts a given copyright ID as a `uint` and returns a mapped `string` for the copyright's reference_URI.

```Solidity
function copyrights(uint token_id) external returns(string memory);
```

#### copyright_owner:

Accepts a given copyright ID and returns a mapped address for the copyright owner.

#### copyrightWork:

Generates a new copyright ID and maps it to a given reference_uri and the given owner.

```Solidity
function copyrightWork(string calldata reference_uri) external;
```

#### renounceCopyrightOwnership

Re-maps a given copyright ID to the 0x0000000000000000000000000000000000000000 address in order to "open source" the copyright, and prevent anyone from modifying it further.

```Solidity
function renounceCopyrightOwnership(uint token_id) external;
```

#### transferCopyrightOwnership

Re-maps a given copyright ID to a new copyright owner.

```Solidity
function transferCopyrightOwnership(uint token_id, address recipient) external;
```

### Events

#### Transfer

MUST trigger whenever ownership of a copyright is transferred.

```Solidity
    event Transfer(uint token_id, address recipient);
```
