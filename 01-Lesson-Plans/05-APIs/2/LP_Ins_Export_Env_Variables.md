### 6. Instructor Do: Export Environment Variables (5 mins) (Critical)

In the previous activity, students learned how to create and call **environment variables** in Python. In this activity, they will learn how to create a `keys.sh` file to export **environment variables** so they can be used in Python, as well as other applications and programs.

**Files:**

* [solution.py](Activities/06-Ins_Solved/solution.py)

Communicate to students that there is a limitation with creating **environment variables** in Python. Using the `os.environ` mapping object only creates the variable within Python. This allows the variable to be used in Python, but other programs and applications won't be able to.

Environment variables are best created and then **exported** so that they can be used by multiple applications and programs.

* Exporting an **environment variable** makes it accessible to all applications and programs. Each application and program **inherits** the variable, which allows developers to make calls using `os.environ.get` to access the data stored in the variable.

Open the [solution]() file, and conduct a dry walkthrough:

* The best way to **export** environment variables is to create a `keys.sh` file. The `keys.sh` **shell script** will contain commands that will create and export environment variables. The `keys.sh` approach is faster than exporting the variables individually.



* Once the `keys.sh` file has been created, it has to be executed. Execution can occur manually, or it can be scheduled.

  ```shell
  sh keys.sh
  ```

* Open the terminal and execute an `echo` command. After the **environment variables** have been **exported**, the variables can be accessed by applications and programs. An example would be the terminal.

  ```shell
  echo $QUANDL_API_KEY
  ```
