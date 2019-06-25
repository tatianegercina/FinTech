### 5. Instructor Do: Environment Variables (5 mins) (Critical)

This activity involves students learn, by way of an instructor live demo, how to store **API keys** in **environment variables**, as well as how to call and use the **environment variables** in Python code. Teaching students how to store **API keys** as **environment variables** will help ensure **API keys** are not hard-coded in Python scripts.

**Files:**

* [env_variables.ipynb](Activities/05-Ins_Env_Variables/Solved/env_variables.ipynb)

Introduce students to the concept of **environment variables** by asking the following question:

* Imagine you signed up for 10 APIs, and each API gave you a key. It'd be extremely difficult to commit each key to memory, so you need to find some way to save the **keys**. What are some possible approaches?

  **Answer** One approach would include tracking the **keys** in an Excel document. The document could be password protected to preserve confidentiality.

  **Answer** Variables could be created, and the **keys** could be stored in the variables.

Navigate to the 5.2 slides, and touch point on each of the below discussion points.

* **Environment variables** are variables just like Python variables; however, instead of being created in a Python application, they're created on a user's actual computer. **Environment variables** are operating system level variables that are accessible by all programs and applications.

* **Environment variables** are given a name, and they can hold any string value. It is important to note that **environment variables** can only hold strings.

* Like with Python variables, data within **environment variables** can be accessed by making a call to the variable.

* An easy, convenient, and secure way to store any data that needs to be accessed across programs and applications is to use **environment variables**. This includes API **keys**, as well as user credentials, and program installation paths (i.e. Python).

Open the [starter-file](Activities/05-Ins_Env_Variables/Unsolved/env_variables.ipynb), and conduct a live demo of how to create **environment variables** in Python.

* **Environment variables** can be created in Python by using the **os** library. This can be imported into Python like all other libraries and packages.

  ```python
  import os
  ```

* **Environment variables** are created and stored using the `os.environ` mapping object. **os.environ** works much like a dict structure. Both a **key** and a **value** are needed upon declaration. The common naming convention for **environment variable** names is **all caps**. Emphasize to students that **environment variables** must be stored as strings.

  ```python
  os.environ["QUANDL_API_KEY"] = "ENTER YOUR KEY HERE"
  ```

* Underscore to students that why it is possible to create **environment variables** in Python, they need to be careful when saving confidential/sensitive data. Confidential/sensitive data should never be hard-coded in a script.

* Once an **environment variable** is declared, it can be called using the `os.environ.get` function. The input to the `os.environ.get` function is the name of the **environment variable**. The output should then be stored as a Python variable to be used at a later time.

  ```python
  api_key = os.getenv("QUANDL_API_KEY")
  print(api_key)
  ```

  ![env_var_print.PNG](Images/env_var_print.PNG)

* If an **environment variable** does not exist, Python will return **None** as the value. An empty **environment variable** will cause an API call to fail. If an API doesn't seem to be working right, double check your **environment variable** using a `print` statement. This will indicate if the **environment variable** is empty (**None**) or has a value.

  ```python
  api_key = os.getenv("MY_QUANDL_API_KEY")
  print(api_key)
  ```

  ```
  None
  ```

* Emphasize to students that they need to make sure that the **environment variable** `print` statement is not pushed into Git, or any other repository, as it would expose their **API keys** to anyone who has access to the repository!

Ask students if there are any questions before continuing.
