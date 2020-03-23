# Creating Your First IAM Admin User and Group

As a [best practice][1], you should not use your AWS account root user for any task where it is not required. Instead, it is better to create a new IAM user for each person that requires administrator access.

To view the tasks that require you to sign in as the root user, see [AWS Tasks that Require Account Root User][2].

This procedure describes how to use the _AWS Management Console_ to create an IAM user for yourself, and add that user to a group that has administrative permissions from an attached managed policy.

Open the [AWS Management Console](https://console.aws.amazon.com) using your _root_ user and create a new user on IAM as follows.

* Look for the IAM service on the _Find Services_ search box, type `iam` and click on `IAM` service.

  ![Create an administrator IAM user - Step 1](Images/iam-user-1.png)

* In the left pane menu, choose the _Users_ option and click on the _Add user_ button.

  ![Create an administrator IAM user - Step 2](Images/iam-user-2.png)

* On the _Add user_ page, provide your new user name in the _User name_ input box, then fill out the details of the new `administrator` by filling in the selections as seen below.  Afterword, click on the _Next: Permissions_ button to continue.

  * **User name:** `administrator`
  * **Access type:** Select the _Programmatic access_ and _AWS Management Console access_ boxes.
  * **Console password:** Choose _Custom password_ and type your own password.
  * **Require password reset:** Unselect this box.

  ![Create an administrator IAM user - Step 3](Images/iam-user-3.png)

* On the _Set permissions_ page, choose _Add user to group_ and click on the _Create group_ button.

  ![Create an administrator IAM user - Step 4](Images/iam-user-4.png)

* In the _Create group_ dialog box, type `Administrators` on the _Group name_ textbox.

* Choose _Filter policies_, and then choose _AWS managed - job function_ to filter the table contents.

  ![Create an administrator IAM user - Step 5](Images/iam-user-5.png)

* In the policy list, select the checkbox for _AdministratorAccess_. Then choose the _Create group_ button.

  ![Create an administrator IAM user - Step 6](Images/iam-user-6.png)

* After creating the group, select the checkbox for your new group. Choose Refresh if necessary to see the group on the list.

  ![Create an administrator IAM user - Step 7](Images/iam-user-7.png)

* Click on the _Next: Tags_ button to continue.

* On the _Next: Tags_ page, leave the defaults and click on the _Next: Review_ button to continue.

  ![Create an administrator IAM user - Step 8](Images/iam-user-8.png)

* Review the list of group memberships to be added to the new user. When you are ready to proceed, click on the _Create user_ button.

  ![Create an administrator IAM user - Step 9](Images/iam-user-9.png)

* Once the user is created, download the user's credentials by clicking on the _Download .csv_ button. Keep those credentials safe.

  ![Create an administrator IAM user - Step 10](Images/iam-user-10.png)

Enable access to billing data for the IAM admin user as follows:

* On the navigation bar, choose your account name, and then choose My Account.

  ![Create an administrator IAM user - Step 11](Images/iam-user-11.png)

* Scroll down to the _IAM User and Role Access to Billing Information_ section, and click on the _Edit_ option.

  ![Create an administrator IAM user - Step 12](Images/iam-user-12.png)

* Select the checkbox to _Activate IAM Access_ and choose _Update_.

  ![Create an administrator IAM user - Step 13](Images/iam-user-13.png)

Sign-out from your session, open the `CSV` file with the new `administrator` user credentials and login into the AWS Management Console using the user's URL and password.

Congratulations! You have created your own admin user.

You can use this same process to create more groups and users and to give your users access to your AWS account resources. To learn about using policies that restrict user permissions to specific AWS resources, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) and [Example IAM Identity-Based Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_examples.html). To add additional users to the group after it is created, see [Adding and Removing Users in an IAM Group](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_add-remove-users.html).

[1]: https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html
[2]: https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
