### Instructor do: Payments Case Study - Stripe

* As students are coming back from break, let them know that we're going to deep-dive into a case study as an example of what we'd like to see in their final report for the homework this week.

* For this case study, we have decided to cover the payment processing known as Stripe, Inc. Not only does it allow us to discuss the ubiquitous world of online payments, Stripe is also an examplar of how a company can generate significant profits by lowing barriers of entry for other businesses.

* When we go to a website, we often take for granted how easy it is to pay for goods and services. Behind the scenes, there has to be a payment processor that walks through the entire ACH (Automated clearing house) submittal process with an operator, verifies payment info, verifies the transaction, communicate with both the bank and the credit card issuer to greenlight the transaction, and notify the end-user of a success or failure. In addition, that system also needs to verify the handshakes between all of those systems and institutions, make sure that every step along the way is secure, and ensure that it is resistant to errors in transmission.

* Oh, and did we also mention it has to be fast? Users tend to become _exceptionally_ anxious if it takes more than 3 seconds to load a page, and studies show that more than half of your users will leave if you don't meet that bar.

* As a programmer facing all of these technical issues, it would be _super_ awesome if someone were to swoop in and take 90% of the work for this off your hands. Enter Stripe.

* Stripe is a payment processing company founded in 2011 that provides a tiny, 8-line set of code that takes the load off of building a payment system into most android, iOS, and web applications. For this service, Stripe charges a relatively small fee on processed payments.

* By integrating Stripe, a developer can dramatically increase their development speeds, while *trust*ing that Stripe will handle much of the security and performance of payments. Anyone building a modern application will likely lean on Stripe as a go-to solution for the first implementation of their application, which has had great financial benefits for Stripe and their target users (developers).

* Stripe is by no means the only pony in town for this service though! Companies such as Plaid, PayPal (through Braintree), Square, and more have developed their own, similar solutions. 