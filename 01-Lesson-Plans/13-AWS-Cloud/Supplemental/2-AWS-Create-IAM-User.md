# Creating Your First IAM Admin User and Group

As a [best practice][1], do not use the AWS account root user for any task where it's not required. Instead, create a new IAM user for each person that requires administrator access. Then make those users administrators by placing the users into an "Administrators" group to which you attach the AdministratorAccess managed policy.

Thereafter, the users in the administrators group should set up the groups, users, and so on, for the AWS account. All future interaction should be through the AWS account's users and their own keys instead of the root user. However, to perform some account and service management tasks, you must log in using the root user credentials. To view the tasks that require you to sign in as the root user, see [AWS Tasks that Require Account Root User][2].

## Creating an Administrator IAM User and Group (Console)

This procedure describes how to use the AWS Management Console to create an IAM user for yourself and add that user to a group that has administrative permissions from an attached managed policy.

**To create an administrator user for yourself and add the user to an administrators group (console)**

1. Use your AWS account email address and password to sign in as the [_AWS account root user_][3] to the IAM console.

    **Note:** We strongly recommend that you adhere to the best practice of using the **`Administrator`** IAM user below and securely lock away the root user credentials. Sign in as the root user only to perform a few [account and service management tasks][2].

2. Enable access to billing data for the IAM admin user that you will create.

    a. On the navigation bar, choose your account name, and then choose **My Account**.

    b. Next to **IAM User and Role Access to Billing Information**, choose **Edit**.

    c. Select the check box to **Activate IAM Access** and choose **Update**.

    d. On the navigation bar, choose **Services** and then **IAM** to return to the IAM dashboard.

3. In the navigation pane, choose **Users** and then choose **Add user**.

4. For **User name**, type **`Administrator`**.

5. Select the check box next to **AWS Management Console access**, select **Custom password**, and then type your new password in the text box. By default, AWS forces the new user to create a new password when first signing in. You can optionally clear the check box next to **User must create a new password at next sign-in** to allow the new user to reset their password after they sign in.

6. Choose **Next: Permissions**.

7. On the **Set permissions** page, choose **Add user to group**.

8. Choose **Create group**.

9. In the **Create group** dialog box, for **Group name** type **`Administrators`**.

10. Choose **Filter policies**, and then choose **AWS managed - job function** to filter the table contents.

11. In the policy list, select the check box for **AdministratorAccess**. Then choose **Create group**.

12. Back in the list of groups, select the check box for your new group. Choose **Refresh** if necessary to see the group in the list.

13. Choose **Next: Tags**.

14. Choose **Next: Review** to see the list of group memberships to be added to the new user. When you are ready to proceed, choose **Create user**.

You can use this same process to create more groups and users and to give your users access to your AWS account resources. To learn about using policies that restrict user permissions to specific AWS resources, see [Access Management][5] and [Example IAM Identity-Based Policies][6]. To add additional users to the group after it's created, see [Adding and Removing Users in an IAM Group][7].

[1]: https://docs.aws.amazon.com/best-practices.html#lock-away-credentials
[2]: https://docs.aws.amazon.com/general/latest/gr/aws_tasks-that-require-root.html
[3]: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html
[4]: https://docs.aws.amazon.com/id_tags.html
[5]: https://docs.aws.amazon.com/access.html
[6]: https://docs.aws.amazon.com/access_policies_examples.html
[7]: https://docs.aws.amazon.com/id_groups_manage_add-remove-users.html

Source: <https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html>
