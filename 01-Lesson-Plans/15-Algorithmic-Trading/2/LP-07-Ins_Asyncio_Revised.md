### 7. Instructor Do: Concurrent Code with Asyncio (15 min)

In this activity, students will learn how to use the asyncio library--an asynchronous framework that allows a developer to write concurrent (or non-sequential) code.

The purpose of this activity is to teach students how to write concurrent code that mitigates the issue of *blocking code* or code that halts the further execution of a program.

**File:** [asyncio.ipynb](Activities/05-Ins_Asyncio/Solved/asyncio.ipynb)

Open the slideshow and discuss the following before proceeding onward to the walk through:

* What is asyncio?






* What is batch data processing vs. real-time data processing?

  **Answer:** Batch data processing refers to the concept of processing data that represents a duration of time that has already occurred, such as historical daily closing price data. In contrast, real-time data processing refers to the concept of processing data that is continually flowing, such as a new up-to-date closing price record every second.

* What are the advantages/disadvantages of batch data processing vs. real-time data processing?

  **Answer:** Batch data processing works well for efficiently processing large volumes of data collected over a period of time, but lacks the granular control of processing data at the record-level. Real-time data processing, however, works well for processing a continual flow of data at the record-level, but is generally less efficient and adds more complexity.

* What is asyncio?

  **Answer:** Asyncio is a library to write concurrent code using the async/await syntax. Specifically, asyncio provides the concept of asynchrony, which unlike multi-threading, implements asynchronous events as independent schedules that are "out of sync" with one another while contained within a single thread.

* What is multi-threading?

  **Answer:** Multi-threading is another method of implementing concurrent code, and uses multiple threads or scheduled tasks that run in the same allocated memory context of a process.

* What is the difference between asynchrony and multi-threading?

  **Answer:** While both can achieve concurrency, asynchrony prevents much of the downsides associated with multi-threading such as memory safety and race conditions by providing control over when a program shifts from one task to the next. In addition, asychrony tends to use less memory as operations are kept on a single thread.


asyncio is a library to write concurrent code using the async/await syntax.

asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.

asyncio is often a perfect fit for IO-bound and high-level structured network code.

asyncio provides a set of high-level APIs to:

run Python coroutines concurrently and have full control over their execution;

perform network IO and IPC;

control subprocesses;

distribute tasks via queues;

synchronize concurrent code;

Additionally, there are low-level APIs for library and framework developers to:

create and manage event loops, which provide asynchronous APIs for networking, running subprocesses, handling OS signals, etc;

implement efficient protocols using transports;

bridge callback-based libraries and code with async/await syntax.


We say that an object is an awaitable object if it can be used in an await expression. Many asyncio APIs are designed to accept awaitables.

There are three main types of awaitable objects: coroutines, Tasks, and Futures.



Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.

Assumptions:

24 opponents
Judit makes each chess move in 5 seconds
Opponents each take 55 seconds to make a move
Games average 30 pair-moves (60 moves total)
Synchronous version: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.

Asynchronous version: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour.
