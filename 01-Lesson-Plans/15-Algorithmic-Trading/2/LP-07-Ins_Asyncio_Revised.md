### 7. Instructor Do: Concurrent Code with Asyncio (15 min)

In this activity, students will learn how to use the asyncio library--an asynchronous framework that allows a developer to write concurrent (or non-sequential) code.

The purpose of this activity is to teach students how to write concurrent code that mitigates the issue of *blocking code* or code that halts the further execution of a program.

**File:** [asyncio.ipynb](Activities/05-Ins_Asyncio/Solved/asyncio.ipynb)

Open the slideshow and discuss the following before proceeding onward to the walk through:

* What is asyncio?

  **Answer:** Asyncio is a library for writing concurrent, or more specifically, asynchronous code that allows for coroutines or functions to "pause" while waiting on their result, thereby allowing other coroutines to run in the meantime; asyncio uses an `async/await` syntax when defining such coroutines.

* Is there a difference between concurrent and asynchronous code?

  **Answer:** Concurrency is merely a broader term used for defining multiple tasks that have the ability to run in parallel. Asynchrony is a more specific type of concurrency in which tasks are able to run in parallel by allowing a task to "pause" and allow other tasks to run while it awaits for its result.

* What would be an example of a synchronous (sequential) vs asychronous (non-sequential) process?

  **Answer:** Imagine an application needs to send an API request and receive the corresponding response for 12 URLs. Each request takes 5 seconds to send to the API and 55 seconds for the API to return a response. A sequential process could be to send a request, wait for the response, and then move onto the next URL, resulting in a total completion time of 720 seconds or 12 minutes ((5 second request + 55 response) x 12 URLs); however, a non-sequential process could be to send a request, and while waiting for the response, send the next request for the next URL and so on for all 12 URLs. This would mean that the total completion time would be cut to 330 seconds ((5 second request x 12 URLs) + 55 second response for all 12 URLs).
  
Then open the solution file and explain the following:

* We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables; there are three main types of awaitable objects: Coroutines, Tasks, and Futures.
