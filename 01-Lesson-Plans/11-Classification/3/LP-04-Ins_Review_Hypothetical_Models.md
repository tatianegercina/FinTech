## 4. Instructor Do: Review Hypothetical Models

Open the slides and walk through each scenario with the students. 

Ask a volunteer to talk the class through each scenario before outlining our answers below.

* In the first case, if we define spam emails as positives, false positives are more costly than false negatives (a spam email getting through is not the end of the world, while an important email that gets flagged as spam might be disasterous for the user). Precision and specificity are important to consider for this reason. Spam emails probably make up a relatively small (but not tiny) proportion of all emails. Because of this, a high accuracy or F1 score might be misleading. 

* False positives and false negatives should probably be weighted fairly evenly in this situation, but true positives are likely to be a small proportion of true negatives. In this situation, high accuracy may still be misleading, but all other evaluation metrics should be examined for different models to understand the relative strenghts and weaknesses of each. 

* For the third example, there doesn't seem to be any obvious reason why false negatives or positives should be weighted more than the other. Assuming a random, representative sample, we would expect the two classes to be roughly equal in size. Therefore, accuracy or the F1 score would likely be a effective summary metric to compare models. 

* In the fourth example, if we define rain as positive, false negatives are likely to be more costly than false positives. This makes recall a metric of special interest. Since the classes are likely to be imbalanced, but not overwhelmingly so (in most climates, a sizable minority days probably have rain). The F1 score is likely a useful measure to compare metrics. 

* For the final example, false negatives are likely to be viewed as more costly than false positives, as VCs invest with the knowledge that the majority of companies will fail but get large returns from those that don't. Recall is likely to be the metric of most interest in this case. 

Tell the class that though we highlighted particular metrics for each of these examples, it is always beneficial to look at the confusion matrix and all the metrics to understand the strengths and weaknesses of any particular model, even if some may be more useful than others for any given data. 