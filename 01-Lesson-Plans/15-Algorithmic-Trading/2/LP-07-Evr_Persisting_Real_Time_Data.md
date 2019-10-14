### 7. Everyone Do: Persisting Real-Time Data (15 mins)

In this activity, students will learn how to transition their trading frameworks from a batch processing data load paradigm (data retrieved all at once) to that of real-time (data retrieved every second), and persist the real-time data to a sqlite database.

The purpose of this activity is to showcase the differences between batch processing vs. real-time data loads and how the latter allows for the trading application to operate on a more granular level (operating and making decisions looking forward in time as data continues to flow) rather than the former (operating and making decisions looking backwards in time based on historical data). In addition, persisting data allows for the de-coupling of the `fetch_data` and `update_dashboard` functions, in which the `update_dashboard` is no longer dependent on the `fetch_data` function and can continue to work should the `fetch_data` function fail.

**Files:** [ninja_trader_v3.py](Activities/05-Evr_Persisting_Real_Time_Data/Solved/ninja_trader_v3.py)

Quickly discuss the following before proceeding onward to the walk through:

* What is batch data processing vs. real-time data processing?

  **Answer:** Batch data processing refers to the concept of processing data that represents a duration of time that has already occurred, such as historical daily closing price data. In contrast, real-time data processing refers to the concept of processing data that is continually flowing, such as a new up-to-date closing price record every second.

* What are the advantages/disadvantages of batch data processing vs. real-time data processing?

  **Answer:** Batch data processing works well for efficiently processing large volumes of data collected over a period of time, but lacks the granular control of processing data at the record-level. Real-time data processing, however, works well for processing a continual flow of data at the record-level, but is generally less efficient and adds more complexity.

* What is data persistence?

  **Answer:** Data persistence is the concept of saving data to a database so as to have a reliable copy of data that is *persisted* rather than transiently stored as in-memory data structures.

Open the solution file and walk through the following with the class:

* 

Ask if there are any questions before moving on.
