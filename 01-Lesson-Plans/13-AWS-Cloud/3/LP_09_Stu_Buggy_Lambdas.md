### 9. Student Do: Buggy Lambdas (10 mins)

In this activity, students will test their Lambdas and will practice their ability to find runtime errors. Slack out the instructions to students together with the [starter test event](Activities/09-Stu_Buggy_Lambdas/Unsolved/convertOkTest.json).

**Instructions:**

* [README.md](Activities/09-Stu_Buggy_Lambdas/README.md)

**Files:**

* [convertOkTest.json](Activities/09-Stu_Buggy_Lambdas/Unsolved/convertOkTest.json)

---

### 10. Instructor Do: Review Buggy Lambdas (10 mins)

**Files:**

* [convertOkTest.json](Activities/09-Stu_Buggy_Lambdas/Solved/convertOkTest.json)

* [convertErrNegAmount.json](Activities/09-Stu_Buggy_Lambdas/Solved/convertErrNegAmount.json)

* [convertOldAge.json](Activities/09-Stu_Buggy_Lambdas/Solved/convertOldAge.json)

Start the review activity by adding the `convertErrNegAmount` and `convertOldAge` test events to your `convertUSD` Lambda, run both test and highlight the following:

* The `convertErrNegAmount` behavior is the same as the case when a zero is passed, an `ElicitSlot` type is returned asking the user for an amount grater than zero.

* The `convertOldAge` text case runs as a correct test event, there is no further validation to prevent a very old person to use the bot.

Open a facilitated discussion with student by asking the following question:

* How can you prevent a possible fake date of birth to be given to the bot?

  **Sample Answer:** Let's suppose that the average life expectancy is 85 years old, we can add an additional condition to validate that the age is between 21 and 85 years.

  **Sample Answer:** We can unfairly discriminate an old person to use the service, so, I wouldn't be worried about this kind of validation.

Continue the discussion by asking for volunteers that want to share their experience finding the bugs provoked by her or his partner.

  **Sample Answer:** It was frustrating since error messages returned by Lambda were no clear.

  **Sample Answer:** It was funny to play becoming a bug detective.

  **Sample Answer:** It was a great opportunity to practice by debugging skills.

Close the discussion by answering any reminder question before moving forward.
