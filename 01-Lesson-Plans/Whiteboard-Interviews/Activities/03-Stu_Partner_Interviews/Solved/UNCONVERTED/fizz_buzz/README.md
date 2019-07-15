# "FizzBuzz"

## Problem

Write a script that prints the numbers 1 to 100 in the console. But for multiples of three, print `Fizz` instead of the number. For multiples of five, print `Buzz`. For numbers which are multiples of both three and five, print `FizzBuzz`.

### Notes to the Interviewer

This is a common screening question. There is no need to drill your candidate on details with this problem.

### Prompts from the Interviewer

The interviewer may use these prompts to prompt additional problem-solving from the interviewee. It is not mandatory to raise every prompt.

* **Prompt**: Does the order in which we check if our number is a multiple of 3, 5, or both matter?

  * **Ask During**: Solution Sketch, Implementation Discussion

  * **Look For**

    * **Candidate Explains Solution**. It does matter, The candidate should be able to reason through why, if you raise this during the Sketch phase, or explain the error in their code, if you raise it during the Discussion phase.

### Hints

* Does the order in which we check if our number is a multiple of 3, 5, or both matter?

  * Whether you use this as a prompt or as a hint to a candidate with a broken solution is up to you.

### Solution

#### Brute Force | Constant Time

The solution is simply to check that the current number is a multiple of both 3 and 5; and then check whether it is a multiple of 3 or 5 if it is not.

```
var fizzBuzz = function(){

  // Loop 100 times, starting from the number 1
  for(var i = 1; i <= 100; i++){

    // If divisible by 3 and 5
    if(i % 3 === 0 && i % 5 === 0) {
      console.log('FizzBuzz');

    } 
    // If divisible by 3
    else if (i % 3 === 0) {
      console.log('Fizz');

    } 
    // If divisible by 5
    else if (i % 5 === 0) {
      console.log('Buzz');

    } 
    // If not divisible either 3 or 5
    else {
      console.log(i);
    }
  }
};
```
