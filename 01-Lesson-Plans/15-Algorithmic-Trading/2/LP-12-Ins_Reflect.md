### 12. Instructor Do: Reflect (10 min)

This activity will conclude today's lesson on Algorithmic Trading Day 2 and provide a chance for students to reflect upon what they've learned throughout the day.

The purpose of this activity is to allow students a chance to take a step back and digest the concepts that have been taught today by engaging students in such a way that students drive the conversation, thereby reinforcing their learning by "teaching" the class.

Recap the skills and concepts learned throughout the lesson, and engage students by having them lead the discussion as much as possible:

* Ask if there are any students who would like to volunteer to summarize the any of the following concepts.

  * What is the purpose of an algorithmic trading framework? What does it look like?

    **Answer:** The purpose of an algorithmic trading framework is to create an end-to-end implementation of working full stack financial trading application. Namely, a framework works by abstracting code into functions, so that the underlying code can potentially be further modified in the future to include additional functionality or be completely replaced altogether.  

  * What is the ccxt library and what does it do? Why is it a convenient library to have in terms of trading?

    **Answer:** The ccxt library is a Cryptocurrency Exchange Trading API that allows a developer to access the many cryptocurrency APIs, such as the Kraken API, through a single API interface.

  * What is the asyncio library? Why was it important for our algorithmic trading applications?

    **Answer:** The asyncio library is an asychronous framework that allows for producing concurrent code. Using asyncio allowed for us to bypass the blocking nature of the continuous while loop, thereby facilitating real-time data loads.

  * What is data persistence? Why is it important?

    **Answer:** Data persistence is the concept of storing or "persisting" data in a reliable location such as a database. It is often important for failure prevention/disaster recovery in the event that an application fails, meaning that an application can pick up where it last failed due to the most recent "save" point.

  * What is the streamz library? What benefits did it provide for our algorithmic trading applications?

    **Answer:** The streamz library allowed for streaming of data to our Panel dashboard and associated visualizations, thereby mitigating the need to re-build the dashboard each time.

* Ask if there are any volunteers who would like to add anything that has not been previously stated.

Then, get students reflecting on what they've learned so far:

* Ask students how might they apply what they've learned so far in Unit 15. Will they go on to manage their own investments through automation?

* Ask students how they now feel regarding algorithmic trading (comfortable or uncomfortable?).

* Ask students to identify two potential things they'd like to practice more from today's lesson that they might have struggled with conceptually.

Finish the recap with a few statements of encouragement:

* Tell students they should give themselves another round of applause. Students now have the tools necessary to engage in live algorithmic trading!

* Remind students that should they choose, they can continue to build out their trading applications to make them even more robust and scalable. In particular, this will be especially impressive to potential employers as not many individuals have an algorithmic trading application under their belts!

* The next step is to further enhance students' algorithmic trading frameworks with machine learning capabilities in Day 3. Students are on their way to not only managing their own trades better, but building a machine that can learn to do it better!
