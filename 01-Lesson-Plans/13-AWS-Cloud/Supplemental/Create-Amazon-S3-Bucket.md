# Creating an Amazon S3 Bucket

In this guide, you will learn how to create private and public Amazon S3 buckets.

Log-in into the AWS Management Console using your `administrator` IAM user before starting this activity. In the "Find Services" search box type `s3` and select `S3` from the services list.

![Launching Amazon S3 from the AWS Management Console](Images/amazon-s3-launch.png)

Amazon S3 stores the files in a container that is called "Bucket". You can have as many buckets as you want, but you must be cautious when defining the access permissions since you can have public and private buckets.

When you create a bucket, you can choose the AWS Region where you want to store your data. Depending on the region, different user data privacy legislation may apply. You can have public or private buckets in Amazon S3.

To create a private bucket follow the next steps:

* Click on the "Crete bucket" button.

  ![Creating a new Amazon S3 bucket](Images/amazon-s3-create-new-bucket.png)

* In the "Create bucket" page, first you need to define a name for your bucket. Bucket's names are unique across all the Amazon S3 space, so AWS checks the uniqueness of the name you typed before creating it.

* We will start by creating a private bucket to store the prediction results for our ML models.

* As the "Bucket name" type the `sm-models` followed by the current timestamp, for example, `sm-models-20200330-1244`. You should select the `US East (Ohio)` AWS Region since the Amazon S3 buckets, and the Amazon SageMaker Studio instance should be in the same region.

  ![Setting the Amazon S3 bucket's name and region](Images/amazon-s3-name-region.png)

* To define a private bucket, you should check the "Block all public access" option. Click on the "Create bucket" button to continue.

  ![Setting private access to the Amazon S3 bucket](Images/amazon-s3-private-access.png)

* Now, on the Amazon S3 console, note that your new bucket has been created, and it has `Not Public` access.

* Adding files to a bucket is easy. Click on the name of your new bucket, next click on the "Upload" button and add the file you want to store in the bucket. Continue by clicking on the "Upload" button and you are done.

  ![Uploading a file to the private Amazon S3 bucket](Images/amazon-s3-private-file-upload.gif)

* If you click on the file name, you will see the file's properties.

  ![Private file properties in Amazon S3](Images/amazon-s3-private-file-properties.gif)

* If you click on the "Object URL," you may note that you can't see the image you uploaded, this is because this object is private.

  ![Opening a private object URL](Images/amazon-s3-private-file-url.gif)

Now let's create a public bucket. You need to return to the Amazon S3 console and click on the "Amazon S3" link.

  ![Moving back to the Amazon S3 console](Images/amazon-s3-back-to-home.png)

Follow the next steps to create a public bucket:

* From the Amazon S3 Console, click on the "Create bucket" button.

* We will name the public bucket as `public-share` followed by the current timestamp, for example, `public-share-20200330-1326`. For this bucket, we will choose the `Canada (Central)` AWS Region.

  ![Setting the name and region for the public Amazon S3 bucket](Images/amazon-s3-public-bucket-name-region.png)

* In the "Bucket settings for Block Public Access" section, uncheck the "Block all public access" option and be sure that all the options below are unchecked.

  ![Setting public access to the Amazon S3 bucket](Images/amazon-s3-setting-public-access.png)

* Note that you will see a warning message stating that you are about to make the buckets and its object available to the public. Check the acknowledge notice and click on the "Create bucket" button to continue.

* It's safe to have a public bucket, but you have to be careful about the files you share as public since they will be available to any person on the Internet.

Continue by uploading a file to the new public bucket, in this demo a happy face is used.

![Uploading a file to the public Amazon S3 bucket](Images/amazon-s3-upload-public-file.gif)

The file you uploaded is not public yet; first you need to set the particular access for that file public for everyone.

Click on the file name; next, click on the "Permissions" tab. Under the "Public access" section, choose "Everyone" and check the "Read object" property; save the changes and go back to the "Overview" tab to open the object's URL to see a cute happy face.

![Setting access to everyone to a particular file](Images/amazon-s3-set-everyone-access.gif)

A public Amazon S3 bucket, may contain private or public files depending on the particular permissions you set to the objects or the AWS IAM policies you define.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
