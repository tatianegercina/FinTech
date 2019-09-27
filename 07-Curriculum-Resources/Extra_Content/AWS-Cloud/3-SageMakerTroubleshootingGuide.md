## SageMaker Troubleshooting Guide

This guide includes some common issues with SageMaker instances.

### Issue: Unresponsive notebook after creation

The first time you execute Python code in JupyterLab, the cell might take longer (up to ~30 seconds?) than usual to execute.

### Issue: Unstable instance

If a SageMaker notebook instance is unstable, you can use the `Actions` menu to `Stop`  and `Start` the instance again, this should effectively restart the compute instance.  
![Notebook Instance actions](../Images/notebook-instance-actions.png)

If the problem persists, you might have to Delete the instance and create a new one to get a fresh start.

### How to: Delete Instance


* From the SageMaker console, use the left pane menu and visit: Notebook -> [Notebook instances](https://console.aws.amazon.com/sagemaker/home?region=us-east-1#/notebook-instances)

* Select the the Notebook Instance (or follow this process for all) on the left circular dot.  
![Notebook Instance list](../Images/notebook-instance-list.png)

* Once selected, click on the right `Actions` menu and select `Stop`.

* Refresh the page and wait for the instance `Status` to change to `Stopped`.  
![Notebook Instance actions](../Images/notebook-instance-actions.png)

* Select the instance again, click on `Actions` and select `Delete` then confirm delete.  
![Notebook Instance delete](../Images/notebook-confirm-delete.png)
