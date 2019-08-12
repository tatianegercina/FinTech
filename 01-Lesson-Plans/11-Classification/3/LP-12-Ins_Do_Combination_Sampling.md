## 12. Instructor Do: Combination Sampling

One of the downsides of oversampling with SMOTE is that, because it doesn't see the overall distribution of the data, it can create new points from the data that are heavily influenced by outliers and therefor very noisy. As we've mentioned before, undersampling is not always an option due to small sample sizes. One way of dealing with these challenges is using a combination sampling strategy.

**Files:**

[combination_sampling.ipynb](Activities/06-Ins_Do_Combination_Sampling/Solved/combination_sampling.ipynb)

Advance through the slides to the combination sampling slide. 

* The downsides of SMOTE can be overcome with an additional step.

* The ENN in SMOTEENN stands for the editted nearest neighbor rule, which looks at the labels for the sampled data and removes instances that are surrounded by data points of the other class. This prunes data points that are noisy (or at least indistinct).

Pause for questions, then open the solved notebook and go through the code.

* The generated data is imbalanced, but also notice that there is significant overlap between the two classes, which makes classification difficult. 

* This quality of the data is also reflected in the SMOTE-sampled data, even though the two classes are balanced. 

![comb_1](Images/comb_1.PNG)

* Now compare the SMOTE-sampled data to the SMOTEENN sampled data, which is significantly more differentiated and removes some of the outliers from each class.

![comb_2](Images/comb_2.PNG)

Walk through the rest of the code and pause for questions before moving on to the next activity. 
