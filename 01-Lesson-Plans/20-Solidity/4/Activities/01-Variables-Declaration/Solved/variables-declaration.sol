// Variables Declaration and Basic Operations

pragma solidity ^0.5.0;

// This is a comment - any code commented is not executed -

/*
This is a multi-line comment.
You can comment out many lines at once.
For the most part you will see single line comments but it is good to see this.

As in single line comments, any code contained within multi-line comments
are not executed.
*/

contract CodeDrills {
    // 1. Create an unsigned integer named `balance`.
    uint balance;

    // 2. Create a signed integer called `x`.
    int x;

    // 3. Define and assign an integer named `y` that has the value `2000`.
    int y = 2000;

    // 4. Create a constant `256 bit` integer `z` with an initial value of `3000`.
    int256 constant z = 3000;

    // 5. Create a `32 bit` integer named `mask` with an initial value of `0`.
    int32 mask = 0;

    // 6. Create a `256 bit` integer `default_mask` and assign a value of `4`.
    int256 constant default_mask = 4;

    // 7. Create a new `256 bit` integer named `a` and assign it the value of `x` times `y`.
    int256 a = x * y;

    // 8. Create a new public `256 bit` integer variable named `b` that has the initial value of `a` plus `z`.
    int256 public b = a + z;

    function Demo() public {
        // 9. Assign `x` the value of `1000`.
        x = 1000;

        // 10. Create a `32 bit` integer variable named `c`.
        int32 c;

        // 11. Assign `c` the value of `mask` times `5`.
        c = mask * 5;

        // 12. Create an unsigned `256 bit` integer named  `d` and assign it an initial value of `1`.
        uint256 d = 1;

        // 13. Create an address variable named `owner`.
        address owner;

        // 14. Assign a valid Ethereum address to `owner`.
        owner = 0x77B2aD074a1aF1AF2a408E3D48465E5F9ec75f45;

        // 15. Create an in-memory string variable called `account_owner` and assign it to your name.
        string memory account_owner = "John Doe";

        // 16. Create an in-memory string called `beneficiary_name` and assign it to the name of the person next to you.
        string memory beneficiary_name = "Jane Doe";

        // 17. Create a payable address variable called `main_account` and assign it a valid Ethereum address.
        address payable main_account = 0x873Ad450656C46cb564eaf418472A1c77d7327Ad;

        // 18. Create a boolean variable called `has_funds` and assign it the value of `true`.
        bool has_funds = true;

        // 19. Increment the value of `x` in one unit using a shorthand operator.
        x += 1;

        // 20. Decrement the value of 'y' in five units using a shorthand operator.
        y -= 5;
    }
}
