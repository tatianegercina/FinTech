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

#### copyrights

Accepts a given `copyright_id` as a `uint` and returns a `mapped struct` containing the copyright's `owner` and `uri`.

```Solidity
function copyrights(uint copyright_id) public returns(IWork memory);
```

#### copyrightWork

Generates a new `copyright_id` of type `uint` and maps it to a given `Work struct` containing the associated copyright `owner` and `uri`.

Must fire the Copyright event.

```Solidity
function copyrightWork(string memory reference_uri) public
```

#### openSourceWork

Generates a new `copyright_id` of type `uint` and maps it to a given `uri` by calling `copyright_uri`.

```Solidity
function openSourceWork(string memory reference_uri) public
```


#### transferCopyrightOwnership

Re-maps a given copyright_id to a new copyright owner. This function must only be callable by the `address` of the `owner` of the given `copyright_id`.

```Solidity
function transferCopyrightOwnership(uint copyright_id, address new_owner) public onlyCopyrightOwner(copyright_id)
```

#### renounceCopyrightOwnership

Re-maps a given copyright_id to the 0x0000000000000000000000000000000000000000 address in order to "open source" the copyright, and prevent anyone from modifying it further. This function must only be callable by the `address` of the `owner` of the given `copyright_id`.

```Solidity
function renounceCopyrightOwnership(uint copyright_id) public onlyCopyrightOwner(copyright_id)
```

### Events

#### Copyright

MUST trigger whenever a new copyrighted work is registered.

```Solidity
event Copyright(uint copyright_id, address owner, string reference_uri);
```

#### OpenSource

MUST trigger whenever a new open source work is registered.

```Solidity
event OpenSource(uint copyright_id, string reference_uri);
```

#### Transfer

MUST trigger whenever a copyright is transferred.

```Solidity
event Transfer(uint copyright_id, address new_owner);
```
