# Deleting AWS Resources

In this guide, you will learn how to delete your AWS resources so that no billing charges are incurred for it after class.

Log-in into the AWS Management Console using your `administrator` IAM user, open the Amazon SageMaker console and choose the "Endpoints" option in the left pane menu.

![Checking for existing endpoints](Images/aws-delete-sm-endpoints.png)

You should not have any endpoint in the "Endpoints" list, if any, select each endpoint and delete it from the "Actions" menu.

Every time you create a model, its configurations are stored, and we may want to delete them to avoid additional charges.

Click on "Endpoint configurations" in the left pane menu; you will see that there are several configurations.

Delete all the endpoint configurations by selecting each one and choosing the "Delete" option from the "Actions" menu.

![Deleting endpoint configuration](Images/amazon-sagemaker-delete-endpoint-conf.gif)

Lastly, go to the Amazon S3 console to remove the buckets created as follows:

* Select the bucket you want to delete, next, click on the "Delete" button.

  ![Deleting Amazon S3 bucket](Images/delete-amazon-s3-bucket.png)

* Since the bucket is not empty, you should delete all the objects first. Click on the "empty bucket configuration" link to continue.

  ![Deleting Amazon S3 objects from a bucket](Images/amazon-s3-empty-bucket-conf.png)

* Next, you need to confirm that you want to empty your bucket. Write the name of your bucket and click on the "Empty" button to continue.

  ![Empty bucket confirmation](Images/amazon-s3-empty-confirm.png)

* Once the bucket is empty, you will see a confirmation message. Click on the "Exit" button to return to the buckets list.

  ![Empty bucket confirmation message](Images/amazon-s3-empty-confirmation.png)

* To permanently delete your bucket, select it again and click on the delete button.

  ![Deleting Amazon S3 bucket](Images/delete-amazon-s3-bucket.png)

* Next, you need to confirm the bucket deletion by writing the name of the bucket. Click on the "Delete bucket" button to continue.

  ![Deleting Amazon S3 bucket confirmation](Images/amazon-s3-delete-confirm.png)

* Once the bucket is deleted, you will see a confirmation message.

  ![Deleted bucket confirmation message](Images/amazon-s3-delete-confirmation-msg.png)

You have to delete all the buckets manually. Since the AWS Free Tier offers twelve months of Amazon S3 storage, you can keep them if you want for one year.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
