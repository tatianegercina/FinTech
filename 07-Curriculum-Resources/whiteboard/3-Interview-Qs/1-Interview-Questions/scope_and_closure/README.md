# Scope & Closure

### Problem

Consider the snippet below.

```
var obj = {};

function foo () {
  var updated = 0;

  return bar;
}

function bar (arg) {
  var key = JSON.stringify(arg);

  if (!(obj[key])) {
    obj[key] = arg
  }
  else {
    return obj[key];
  }

  console.log(updated);
}
```

1. What will happen if we call `bar`? Why? How can we rearrange our code to fix this, and why does this work?

2. After updatin your code, explain where `bar` and `obj` are visible, and why.

3. Run `foo`; store its return value in a variable; and experiment with it. Explain its behavior. What fundamental JavaScript concept is responsible for this behavior?

### Notes to the Interviewer

This problem tests a candidate's knowledge of **scope** and **closure**.

### Prompts from the Interviewer

* **Prompt**: How can we modify this code so that `obj` is only visible in `foo`?

  * **Ask During**: Solution Sketch

  * **Ask If**: Ask this question to candidates who have trouble getting started on the question on their own.

  * **Look For**

    * **Candidate Answers Prompt**

      * Candidates should be able to explain that we must move the `var obj = {}` declaration into `function foo`.

* **Prompt**: How can we modify this code so that `bar` is only visible in `foo`?

  * **Follow-Up**: Can we declare functions inside of other functions?

  * **Ask During**: Solution Sketch

  * **Ask If**: Ask this question to candidates who have trouble moving past the stage of moving `obj` into `foo`.

  * **Look For**

    * **Candidate Answers Prompt**

      * Candidates should be able to explain that we must move the `function bar = { ... }` declaration into `function foo`.

* **Prompt**: When we run `foo`, what does it return?

  * **Ask During**: Implementation Discussion

  * **Look For**

    * **Candidate Answers Prompt**

      * Candidates should be able to explain that running `foo` returns the function `bar`.

* **Prompt**: When we execute the return value of `foo`, what does it do?

  * **Ask During**: Implementation Discussion

  * **Look For**

    * **Candidate Answers Prompt**

      * Candidates should be able to explain that running the instance of `bar` that `foo` returns updates the `obj` object inside of `foo`.

### Notes

This exercise is relatively straightforward, in that it doesn't require students to write new code, but may be challenging precisely _because_ it doesn't require students to write new code. Use prompts liberally if this is the case.

### Solution
