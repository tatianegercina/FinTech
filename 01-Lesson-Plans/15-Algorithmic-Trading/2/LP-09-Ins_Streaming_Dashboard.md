### 9. Instructor Do: Streaming Dashboard (15 min)

In this activity, students will learn how to use the Streamz library to create a dedicated pipeline for continuous streaming data.

The purpose of this activity is to showcase the need for a pipeline or buffer that manages incoming streaming data, as doing so allows for a more robust and scalable dashboard in which streaming data is handled at the visual component level rather than done via a re-draw of the entire dashboard each time.

**File:** [nano_trader_v2.py](Activities/08-Ins_Streaming_Dashboard/Solved/nano_trader_v2.py)

Quickly discuss the following before proceeding onward to the walk through:

* What is Streamz?

    **Answer:** Streamz is a library that helps to build pipelines that manage continuous streams of data such as Pandas dataframes containing tabular data.

* Why should you use Streamz?

    **Answer:** When creating a dashboard, oftentimes it is necessary to be able to have multiple tabs with other visualizations running in parallel; however, re-drawing a full dashboard each time (as is currently done) will "refresh" the dashboard and redirect users to the home screen (or tab) each time. Therefore, in order to have visualizations running in separate tabs in parallel, it is essential to separate the streaming data layer from the dashboard creation layer.

Open the solution file and review the following:

*

Answer any questions before moving on.
