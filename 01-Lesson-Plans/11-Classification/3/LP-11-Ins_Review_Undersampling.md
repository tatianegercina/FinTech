## 11. Instructor Review: Undersampling

**Files:**

[undersampling.ipynb](Activities/05-Stu_Do_Undersampling/Solved/undersampling.ipynb)

Open the solved notebook and go through the code. Since the structure of this activity is very similar to the oversampling activity, you should focus on the evaluation metrics obtained from the two undersampling methods. 

* The results from random undersampling seem to be worse than those from oversampling across the board. This might signal that the additional data provided by oversampling was necessary to train a good model. 

![unders_1](Images/unders_1.PNG)

* Results from cluster centroid undersampling are even worse than those from random undersampling. This difference is most likely due to random variation. 

![unders_2](Images/unders_2.PNG)

Ask students which sampling method they prefer for this data given the evaluation results they have seen. Is there ever an argument for using a sampling methdology that results in worse evaluation metrics?

* Holding all else equal, we would want to use the sampling methdology that results in the best evaluation metrics. However, we have not tried alternative models which might provide better fits for this dataset. If the training set seems large enough to use undersampling, we might want to try different models, such as tree-based or ensemble classifiers, before determining that oversampling is the better methodology. 