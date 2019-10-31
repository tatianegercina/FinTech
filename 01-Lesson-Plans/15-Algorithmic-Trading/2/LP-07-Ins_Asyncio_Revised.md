### 7. Instructor Do: Concurreny with Asyncio (15 min)

In this activity, students will learn how to use the asyncio library--an asynchronous framework that allows a developer to write concurrent (or non-sequential) code.

The purpose of this activity is to teach students how to write concurrent code that mitigates the issue of sequential code, namely *blocking code* or code that halts the further execution of downstream processes within a program.

**File:** [asyncio.ipynb](Activities/05-Ins_Asyncio/Solved/asyncio.ipynb)

Open the slideshow and discuss the following before proceeding onward to the walk through:

* What is asyncio?

  **Answer:** Asyncio is a library for writing concurrent, or more specifically, asynchronous code that allows for coroutines or functions to "pause" while waiting on their result, thereby allowing other coroutines to run in the meantime; asyncio uses an `async/await` syntax when defining such coroutines.

* Is there a difference between concurrent and asynchronous code?

  **Answer:** Concurrency is merely a broader term used for defining multiple tasks that have the ability to run in parallel. Asynchrony is a more specific type of concurrency in which tasks are able to run in parallel by allowing a task to "pause" and allow other tasks to run while it awaits for its result.

* What would be an example of a synchronous (sequential) vs asychronous (non-sequential) process?

  **Answer:** Imagine an application needs to send an API request and receive the corresponding response for 12 URLs. Each request takes 5 seconds to send to the API and 55 seconds for the API to return a response. A sequential process could be to send a request, wait for the response, and then move onto the next URL, resulting in a total completion time of 720 seconds or 12 minutes ((5 second request + 55 response) x 12 URLs); however, a non-sequential process could be to send a request, and while waiting for the response, send the next request for the next URL and so on for all 12 URLs. This would mean that the total completion time would be cut to 330 seconds or 5 1/2 minutes ((5 second request x 12 URLs) + 55 second response for all 12 URLs).
  
Then open the solution file and explain the following:

* The event loop is the core of every asyncio application and manages the execution of awaitable objects, or objects that can be used in an await expression, such as Coroutines, Tasks, and Futures (we'll only focus on coroutines and tasks for simplicity); the `get_event_loop` function gets the current event loop and creates a new event loop if no current one is found.

  ```python
  import asyncio
  import time
  
  loop = asyncio.get_event_loop()
  ```

* A Coroutine is an asyncio process defined by the `async/await` syntax. Despite its name, a Coroutine is merely a single process that does not run concurrently but *can* if used in conjunction with asyncio Tasks. In this case, a coroutine defined as the `main` function is executed using the `run_until_complete` function of the current event loop and prints the string "One", then waits 1 second, and finally prints the string "Two".

  ![single-coroutine-no-error](Images/single-coroutine-no-error.png)

* It should be noted that Jupyter already runs an event loop for the cells in a Jupyter Notebook file. It is for this reason that we used a try-catch clause to ignore the following RunTimeError (for aesthetic reasons). Normally, asyncio would be used in a classic Python or .py file.

  ![single-coroutine-error](Images/single-coroutine-error.png)

* Multiple coroutines can be run in sequence by merely calling the await expression on multiple async defined functions. In this case, the `say_after` waits 1 second before printing the string "One" and then waits another 2 seconds before printing the string "Two". Total completion time is 3 seconds.

  ![single-coroutine-multiple-times](Images/single-coroutine-multiple-times.png)

* A Task is a concurrent execution of a coroutine. Therefore, multiple tasks of a single coroutine will be executed concurrently. In this case, tasks are explicitly created using the asyncio `create_task` function and the first task waits 1 second and prints the string "One", and *while* the first task is waiting for the 1 second duration, the second task is executed, waits 2 seconds, and prints the string "Two". Total completion time is now only 2 seconds, a 33% reduction in time.

  ![multiple-tasks](Images/multiple-tasks.png)

* Similarly, the asyncio `gather` function can accept multiple calls of a single coroutine and create multiple tasks under-the-hood. Therefore, the multiple tasks are executed concurrently and the total completion time is still 2 seconds.

  ![multiple-tasks-gather](Images/multiple-tasks-gather.png)

* As can be seen, running code asychronously (non-sequentially) as opposed to synchronously (sequentially) can have significant performance benefits and should be implemented to optimize and ultimately make applications more robust.
