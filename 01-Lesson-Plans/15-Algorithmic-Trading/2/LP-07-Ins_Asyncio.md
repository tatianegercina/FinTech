### 7. Instructor Do: Asyncio (15 min)

In this activity, students will learn how to transition their trading frameworks to use a real-time data load paradigm (data retrieved continuously) rather than a batch processing data load paradigm (data retrieved all at once) with the help of asyncio, a library to write concurrent or asynchronous code that mitigates the issue of *blocking code* or code that halts the further execution of a program.

The purpose of this activity is to not only demonstrate what processing real-time data looks like, but also showcase the role asyncio plays in preventing the issue of blocking code.

**File:** [nano_trader.py](Activities/05-Ins_Asyncio/Solved/nano_trader.py)

Quickly discuss the following before proceeding onward to the walk through:

* What is batch data processing vs. real-time data processing?

  **Answer:** Batch data processing refers to the concept of processing data that represents a duration of time that has already occurred, such as historical daily closing price data. In contrast, real-time data processing refers to the concept of processing data that is continually flowing, such as a new up-to-date closing price record every second.

* What are the advantages/disadvantages of batch data processing vs. real-time data processing?

  **Answer:** Batch data processing works well for efficiently processing large volumes of data collected over a period of time, but lacks the granular control of processing data at the record-level. Real-time data processing, however, works well for processing a continual flow of data at the record-level, but is generally less efficient and adds more complexity.

* What is asyncio?

  **Answer:** Asyncio is a library to write concurrent code using the async/await syntax. Specifically, asyncio provides the concept of asynchrony, which unlike multi-threading, implements asynchronous events as independent schedules that are "out of sync" with one another entirely within a single thread.

* What is multi-threading?

  **Answer:** Multi-threading is another method of implementing concurrent code, and uses multiple threads or scheduled tasks that run in the same allocated memory context of a process.

* What is the difference between asynchrony and multi-threading?

  **Answer:** While both can achieve concurrency, asynchrony prevents much of the downsides associated with multi-threading such as memory safety and race conditions by providing control over when a program shifts from one task to the next. In addition, asychrony tends to use less memory as operations are kept on a single thread.

Open the solution file and review the following:

*  

Answer any questions before moving on.
