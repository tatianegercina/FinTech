# Creating an Amazon SageMaker Instance

In this guide, you will learn how you can start running Jupyter notebooks in the Cloud using Amazon SageMaker Studio.

Start by logging-in into the [AWS Management Console](https://console.aws.amazon.com/) using your `administrator` IAM use and to follow the next steps.

From the AWS Management Console, type `sagemaker` in the "Find Services" search box and choose `Amazon SageMaker` from the list.

![Launching Amazon SageMaker](Images/launching-sagemaker.png)

AWS currently offers Amazon SageMaker Studio as a generally available preview version from the US East (Ohio) AWS region. Since it's a preview version, some aspects of the user interface (UI) may vary over the time it's released as a final version.

In the Amazon SageMaker homepage, click on the "Amazon SageMaker Studio" at the left menu to continue.

![Opening Amazon SageMaker Studio](Images/open-sagemaker-studio.png)

If you are not in the `US East (Ohio)` AWS region, you will see a warning message asking for switching to that region. Open the AWS regions list, select the `US East (Ohio)` AWS region, and click again in the "Amazon SageMaker Studio" option in the left menu.

![Switching to the US East (Ohio) AWS Region](Images/switching-to-ohio.gif)

Continue by setting the initial configuration for Amazon SageMaker Studio, under the "Get Started" section, choose the "Quick Start" option and leave the default user name.

![Choosing the default user name for Amazon SageMaker Studio](Images/sagemaker-studio-user.png)

Next, in the "Execution role" option, click on the list box and choose "Create a new role"; a pop-up window named "Create an IAM role" will appear, select "Any S3 bucket" under the "S3 buckets you specify" option and click on the "Create role" button to continue.

![Create an execution role](Images/sagemaker-studio-execution-role.gif)

Continue by clicking on the "Submit" button.

![Create an Amazon SageMaker Studio instance](Images/sagemaker-create-instance.png)

Next, the new instance of Amazon SageMaker Studio and the new user will be configured; you will be led to a new page where you may have to wait about five minutes.

![Amazon SageMaker Studio instance creation](Images/sagemaker-studio-instance-in-progress.png)

Once the Amazon SageMaker Studio instance is ready, you will see the following notification message; you may have to wait an additional minute or two until the Studio user is ready, after that, you will see the "Open Studio" link enabled.

![Amazon SageMaker Studio is ready](Images/sagemaker-studio-instance-ready.png)

Continue by clicking on the "Open Studio" link, a new window (or tab) will be opened and you will see the following loading page until the UI of Amazon SageMaker Studio appears. **Note:** This process may take up to five minutes the first time.

![Loading Amazon SageMaker Studio](Images/sagemaker-studio-loading.png)

After the loading process ends, you will see the UI of Amazon SageMaker Studio. You may note that it is practically the same UI as Jupyter lab but with a different colour scheme.

![The Amazon SageMaker Studio UI](Images/sagemaker-studio-ui.png)

Amazon SageMaker Studio can be used in the same way you were working locally with Jupyter lab; the main difference is that Studio is a cloud application that allows access to all the computing power of AWS.

Continue by clicking in the "Launcher" tab. Amazon SageMaker has different built-in images to create notebooks; these images are similar to a Python virtual environment.

Continue by ensuring the "Data Science" image is selected; next, click on the "Python 3" notebook option. A fresh Jupyter notebook will appear, test it by printing a `Hello!!` message.

![Creating a notebook in Amazon SageMaker Studio](Images/sagemaker-studio-create-notebook.gif)

As any Jupyter lab interface, you can run notebooks and custom code in Amazon SageMaker Studio.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
