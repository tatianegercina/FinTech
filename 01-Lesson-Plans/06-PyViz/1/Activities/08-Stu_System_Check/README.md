# System Check

Before we can begin navigating the PyViz ecosystem, we have to make sure everyone has PyViz installed and ready to go. For this activity, you will team up with a partner and confirm that he or she has PyViz installed.

If you run into any problems, reach out to a TA for help. They will be circulating to confirm each person in the groups has PyViz installed and is ready to get started with coding.

## Instructions

1. Find a partner.

2. Use the **Git terminal** to execute the following command on your partner's machine.

    ```shell
    conda list | grep pyviz
    ```

    ```
    panel                     0.6.0                      py_0    pyviz
    param                     1.9.1                      py_0    pyviz
    pyct                      0.4.6                      py_0    pyviz
    pyct-core                 0.4.6                      py_0    pyviz
    pyviz_comms               0.7.2                      py_0    pyviz
    ```

3. Reach out to a TA if the output does not look similar to the below output. While the version numbers do not need to match, the package names should. **Pyviz_comms** and **Panel** are especially important.

    ![pyviz_check_output.PNG](Images/pyviz_check_output.PNG)
