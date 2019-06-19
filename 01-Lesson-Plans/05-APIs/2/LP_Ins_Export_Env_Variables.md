### 6. Instructor Do: Export Environment Variables (5 mins) (Critical)

In the previous activity, students learned how to create and call **environment variables** in Python. In this activity, they will learn how to create a `keys.sh` file to **export** **environment variables** so they can be used in Python, as well as other applications and programs.

**Files:**

* [keys.sh](Activities/06-Ins_Export_Env_Variables/Solved/keys.sh)
* [keys.sh](Activities/06-Ins_Export_Env_Variables/Unsolved/keys.sh)

Open the 5.2 slides, and address the following discussion points:

* **Exporting** an **environment variable** exposes it to all applications and programs sharing the same parent process. Each application and program **inherits** the variable, which allows developers to make calls using `os.environ.get` to access the data stored in the variable.

* The best way to **export** **environment variables** is to create a `keys.sh` file. The `keys.sh` **shell script** will contain commands that will create and **export** **environment variables**. The `keys.sh` approach is faster than exporting the variables individually.

Open the [starter-file](Activities/06-Ins_Export_Env_Variables/Unsolved/keys.sh), and perform a live demo of creating and **exporting** **environment variables** with the `keys.sh` file.

* Enter the following command into `keys.sh` file.

  ```shell
  export QUANDL_API_KEY="zBR2ZoJGSxqe77s_YsAv"
  ```

* Once the `keys.sh` file has been created, it has to be **executed**. Execution can occur manually, or it can be scheduled.

  ```shell
  . ./keys.sh
  ```

* Execute an `echo` command to output the value of variable to the screen.

  ```shell
  echo $QUANDL_API_KEY
  ```

  ![echo_env_variable.PNG](Images\echo_env_variable.PNG)

Ask if there are any questions, and then move on to the next activity.
