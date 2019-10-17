# Voice Gender Recognition

Banks are always looking to innovate in authentication methods to protect their clients' privacy and ensure data security. [Voice signature](https://whatis.techtarget.com/definition/voice-signature) is a method used in phone baking to authenticate clients by their voice and approve transactions; part of the voice authentication process is to identify the gender of the client as a first step to prevent fraud.

In this activity, you will create a neural network to predict the gender of a voice using the acoustic properties of the voice and speech.

## The Dataset

The dataset that is going to be used in this activity was created to identify a voice as male or female based upon acoustic properties of the voice and speech.

The dataset consists of `3,168` recorded voice samples, collected from male and female speakers. The voice samples were pre-processed by acoustic analysis in R using the `seewave` and `tuneR` packages, with an analyzed frequency range of `0hz` to `280hz` (human vocal range).

The following acoustic properties of each voice are measured and included within the CSV:

* meanfreq: mean frequency (in kHz)
* sd: standard deviation of frequency
* median: median frequency (in kHz)
* Q25: first quantile (in kHz)
* Q75: third quantile (in kHz)
* IQR: interquantile range (in kHz)
* skew: skewness (see note in specprop description)
* kurt: kurtosis (see note in specprop description)
* sp.ent: spectral entropy
* sfm: spectral flatness
* mode: mode frequency
* centroid: frequency centroid (see specprop)
* peakf: peak frequency (frequency with highest energy)
* meanfun: average of fundamental frequency measured across acoustic signal
* minfun: minimum fundamental frequency measured across acoustic signal
* maxfun: maximum fundamental frequency measured across acoustic signal
* meandom: average of dominant frequency measured across acoustic signal
* mindom: minimum of dominant frequency measured across acoustic signal
* maxdom: maximum of dominant frequency measured across acoustic signal
* dfrange: range of dominant frequency measured across acoustic signal
* modindx: modulation index. Calculated as the accumulated absolute difference between adjacent measurements of fundamental frequencies divided by the frequency range
* label: male or female

## Instructions

### Data Preprocessing

Load the data in a Pandas DataFrame called `voice_df` and perform the following tasks:

1. Create the features set `X` by copying all the columns from the `voice_df` DataFrame, except the `label` column.

2. Create the target vector `y` by copying the values of the `label` column from the `voice_df` DataFrame.

3. Create the testing and training sets using the `train_test_split` method from `sklearn`.

4. Scale the features' training and testing data using the `StandardScaler()` module from `sklearn`.

5. Encode the target's training and testing data using the `OneHotEncoding` module from `sklearn`.

### Create a Neural Network Model

Create a neural network model as follows:

1. In the first layer, define `21` input nodes (for each one of the voice recordings features), include one hidden layer with `100` nodes, and use the `relu` activation function.

2. Define the output layer with two nodes and `softmax` as the activation function.

    * Note that despite the values of the `label` column could be encoded as a binary output (e.g. `0` - male and `1` - female), you encoded this column using one-hot encoding, that's why you've to define two nodes in the output layer, since you will have two categories as possible outputs of the neural network model.

3. Compile the model using the `adam` optimizer and the `categorical_crossentropy` loss function.

    * The `categorical_crossentropy` loss function is intended for classification problems.

4. Display the summary of your model to visualize its final structure.

5. Fit the model using `60` epochs.

6. Evaluate the model using the `Evaluate` method.

### Final Conclusions

Write down your conclusions about the model you created, can it be used to identify clients' gender as part of the voice signature authentication process in phone banking?
