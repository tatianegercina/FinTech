# Creating an Administrator User on AWS Identity and Access Management

Amazon Web Services provides a service called Identity and Access Management (IAM) to create and manage users. In this guide, you will learn how to create an `administrator` user using the AWS IAM service.

Having an `administrator` IAM user is a standard best practice is to avoid using the principal or root user to manage an AWS account and add some extra security when working on AWS.

This new user may look redundant with the root user, however, if the access credentials of this new `administrator` user get compromised, you can block it or recreate the password to secure your services without compromising your root user.

Usually a new user should be created for each person that requires administrative access to the services managed by an AWS root account, especially in corporate environments.

Follow the next steps to create an `administrator` IAM user:

* Open the [AWS Management Console](https://console.aws.amazon.com) using your root user.

* Continue by looking for the IAM service on the Find Services search box, type `iam`, and click on IAM service.

  ![Create an administrator IAM user - Step 1](Images/iam-user-1.png)

* In the IAM start page, you may note that this service is marked as `Global` in the upper right corner, this means that IAM users can access AWS resources in any AWS Region. In the left pane menu, choose the "Users" option to continue.

  ![Create an administrator IAM user - Step 2](Images/iam-user-2.png)

* In the Users start page, click on the "Add user" button to continue.

  ![Create an administrator IAM user - Step 3](Images/iam-user-2_bis.png)

* On the _Add user_ page, fill out the details of the new `administrator` user and click on the "Next: Permissions" button to continue.

  * **User name:** `administrator`
  * **Access type:** Select the "Programmatic access" and "AWS Management Console access" boxes.
  * **Console password:** Choose "Custom password" and type a password you may remember.
  * **Require password reset:** Uncheck this box.

  ![Create an administrator IAM user - Step 3](Images/iam-user-3.png)

* On the "Set permissions" page, choose "Add user to group" and click on the "Create group" button.

  ![Create an administrator IAM user - Step 4](Images/iam-user-4.png)

* In the "Create group" dialogue box, type `Administrators` on the "Group name" textbox.

  ![Create an administrator IAM user - Step 4](Images/iam-user-4_bis.png)

* Click on "Filter policies" and then choose "AWS managed - job function" to filter the policies table content.

  ![Create an administrator IAM user - Step 5](Images/iam-user-5.png)

* In the policy list, select the checkbox for AdministratorAccess. Then choose the _Create group_ button.

  ![Create an administrator IAM user - Step 6](Images/iam-user-6.png)

* After creating the group, select the checkbox for your new group. Choose Refresh if necessary to see the group on the list.

  ![Create an administrator IAM user - Step 7](Images/iam-user-7.png)

* Click on the "Next: Tags" button to continue.

  ![Create an administrator IAM user - Step 7](Images/iam-user-7_bis.png)

* On the "Add Tags" page, leave the defaults and click on the "Next: Review" button to continue.

  ![Create an administrator IAM user - Step 8](Images/iam-user-8.png)

* Review the list of group memberships to be added to the new user. When you are ready to proceed, click on the "Create user" button.

  ![Create an administrator IAM user - Step 9](Images/iam-user-9.png)

* Once the user is created, download the user's credentials by clicking on the "Download .csv" button. Keep these credentials safe.

  ![Create an administrator IAM user - Step 10](Images/iam-user-10.png)

Now you should enable access to billing data for the new IAM administrator user, proceed as follows:

* On the navigation bar, click on your account name and then choose "My Account."

  ![Create an administrator IAM user - Step 11](Images/iam-user-11.png)

* On the next page, scroll down to the "IAM User and Role Access to Billing Information" section, and click on the _Edit_ option.

  ![Create an administrator IAM user - Step 12](Images/iam-user-12.png)

* Check the option "Activate IAM Access" and click on the "Update" button to finish.

  ![Create an administrator IAM user - Step 13](Images/iam-user-13.png)

Now, sign out from your current session with the root user to start using your new `administrator` user.

![Create an administrator IAM user - Step 14](Images/iam-user-14.png)

Open the `CSV` file with the new `administrator` user credentials you downloaded before and proceed as follows:

* In the `CSV` file, you will find a custom login link that you need to use to access the AWS Management Console with your `administrator` user.

  ![Create an administrator IAM user - Step 15](Images/iam-user-15.png)

* Copy the custom login link and paste it on your browser to open the custom login page. Type `administrator` as the "IAM user name" and the password you choose before. Click on the "Sign in" button to continue.

  ![Create an administrator IAM user - Step 16](Images/iam-user-16.png)

* Now you are logged-in into the AWS Management Console with your brand new IAM user. You may note that the IAM user name appears in the upper right corner, followed by your AWS account ID.

  ![Create an administrator IAM user - Step 17](Images/iam-user-17.png)

From now on, you should avoid using your "root user" and work with this new `administrator` user instead.

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
