# Delegation to Prototype

## Problem

Consider the constructor function.

```
'use strict';

function User (firstName, lastName, email) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.email = email;
}
```

1. How could you update this code such that all `User` objects have a `fullName` method that returns the user's full name? Sketch and implement your solution.

2. Can _all_ `User` objects call `fullName`—including those created _before_ you defined the method? If not, how would you update this code such that this is the case?

3. In your implementation, you use `User.prototype`. What object does `fullName` live on? Draw how it's related to individual `User` objects.

## Notes to the Interviewer

This problem tests your candidate's familiarity with JavaScript's prototype mechanism.

### Prompts from the Interviewer

The below prompts are not additional questions the interviewer can ask, but notes on how to pose and grade responses to the three questions in the problem statement.

* **Prompt**: How could you update this code such that all `User` objects have a `fullName` method that returns the user's full name?

  * **Ask During**: Restate the Problem

  * **Look For**

    * **Candidate Explains Approach**

      * Strong candidates will attach a `fullName` method to `User.prototype`. This is the best answer.

      * Many candidates will instinctively add a function property inside of the `User` constructor, like `this.fullName = function () { ... }`. This is a legitimate solution as well, but candidates will have to modify it later.

* **Prompt**: Suppose you had created a few user objects before updating your code. Can those objects call `fullName`? If not, how would you update this code such that this is the case?

  * **Ask During**: Implementation Discussion after Question 1

  * **Look For**

    * **Candidate Explains Instance Method**

      * Some strong candidates may add their `fullName` function to `User.prototype`. They should answer **yes**—previously created `User` objects _can_ call `fullName` if it is defined on `User.prototype`.

      * Strong candidates who add a function property, like `this.fullName = function () { ... }`, will correctly answer **no**, and explain that their code creates a `fullName` method on every _individual_ `User` object we create with the `User` constructor function.

        * Candidates who implemented their initial solution this way will move their `fullName` method out of the `User` constructor and onto `User.prototype`.

* **Prompt**: In your implementation, you use `User.prototype`. What object does `fullName` live on? Draw how it's related to individual `User` objects.

  * **Ask If**: Only proceed to this question if your candidate successfully attaches their `fullName` method to `User.prototype`.

  * **Ask During**: Implementation Discussion

  * **Look For**

    * **Candidate Explains Prototype Linkage**

      * Strong candidates will explain that `fullName` lives on the `User.prototype` object.

        * Crucially, they will **not** state that it lives on individual `User` objects. This would be a definitively incorrect answer.

      * Strong candidates will explain that all individual `User` objects are _linked_ to, or _point_ to, `User.prototype`. The relationship looks like the image below.

## Solution

The solution is available in [User.js](Solved/User.js).
