## 9. Instructor Do: Undersampling

Continue in the powerpoint slides to the undersampling slide.

* If we have imbalanced classes, we can purposefully use more of the minority class for training - this is oversampling. However, we can also take fewer instances of the majority class than would be indicated by a proportional sampling method - this is called undersampling. 

* In undersampling, we take only as many instances of the majority class as there are instances in the minority class training set. 

* Undersampling is only practical when there is enough data in the training set that a model can be suitably estimated with the reduced number of total training data.

* However, undersampling does have the advantage that all data in the training set are actual observed data, and potential model biases that come from replicating training data or creating synthetic data will not exist, as they might with oversampling. 

* Just like oversampling, there are numerous methods for undersampling. We will go over random undersampling and cluster-centroid undersampling. 

* In random undersampling, the algorithm randomly choose majority class instances to take out of the training set until the number of instances of the majority class is equal to the number of instances in the minority class training set. 

* In cluster centroid undersampling, the algorithm first creates n clusters in the majority class training data using the K-means clustering strategy, where n is equal to the number of minority class training instances, and then takes the centroids of those clusters to be the majority class training set. This is meant to ensure that the sampled data is "representative" of the majority set, as compared to a random set. 

Pause for students' questions before moving on to the next activity. 