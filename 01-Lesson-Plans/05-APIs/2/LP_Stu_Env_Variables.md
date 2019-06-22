### 7. Students Do: Under Lock and Key (20 mins)

The previous modules focused on the instructor demoing how to use and store API **keys** with **environment variables**. Students now engage in a bridge activity that involves retrieving a **Quandl** API **key**, and submitting a **Quandl** API request with the **key** stored as an **environment variables**. This will be the students' first opportunity for hands-on practice with API **keys** and **environment variables**.

Working with environment variables can be a little tricky, especially if they are not declared and exported correctly. Make sure both TAs and yourself are circulating during this activity to help resolve any technical/environmental issues students may face.

If students finish early, use the extra time to review the final two guided review questions from the next activity.

**Files:**

* [env_variables.ipynb](Activities/07-Stu_Env_Variables/Unsolved/env_variables.ipynb)

* [keys.sh](Activities/07-Stu_Env_Variables/Solved/keys.sh)

**Instructions:**

* [README.md](Activities/07-Stu_Env_Variables/README.md)

- - -

### 8. Instructor Do: Activity Review (5 mins)

**Files:**

* [keys.sh](Activities/07-Stu_Env_Variables/Solved/keys.sh)

* [env_variables.ipynb](Activities/07-Stu_Env_Variables/Solved/env_variables.ipynb)

Kick off the activity review session by asking students to summarize the process of creating and using **environment variables** with APIs. Engage the students with the following questions:

* After acquiring an **API key**, what's the first thing that should be done?

  **Answer** The **key** should be stored as an **environment variable** using a `keys.sh` file.

* Once an **environment variable** has been exported, what should happen next?

  **Answer** The `keys.sh` file should be executed. When executing, the `source` command should be used.

* What should be done after the `keys.sh` file has been executed and **sourced**?

  **Answer** The **environment variable** should be called in Python using the `os.environ.get` function.

* Is there ever a time where an API **key** should be hard-coded within a Python script?

  **Answer** No. The best practice for keeping **API keys** secure is to store them in **environment variables**. This practice should always be used.

Open the [solution](Activities/07-Stu_Env_Variables/Solved/env_variables.ipynb), and end the review session with a quick dry walkthrough of the solution.

* The `export` command is used to create **environment variables**. Once created, the **environment variables** are then shared with all child processes. For example, when the `keys.sh` file is executed, the export command will ensure the `QUANDL_API_KEY` variable is accessible by all processes running in the terminal that executed the `keys.sh` file.

  ```shell
  export QUANDL_API_KEY="ENTER YOUR KEY HERE"
  ```

* Once a `key.sh` file is created, it has to be executed in order for the `export` commands to execute. Supplying `source` command before the `key.sh` file will **source** the variables and load the `keys.sh` file/`export` command.

  ![source_keys.PNG](Images/source_keys.PNG)

* **Environment variables** can be accessed in Python with the **os** library. The library has to be imported before it can be used. The **os** library has an `os.getenv` function that can be used to retrieve **environment variables** from the operating system. Once retrieved, the value can be saved as a Python variable (i.e. `api_key`).

* Once stored as a Python variable, the **environment variable** value can be leveraged for processing. In this case, the `QUANDL_API_KEY` is stored as Python variable **api_key** and then concatenated with the **request url**. The concatenated **request url** will then be used to submit a request to the **Quandl** API.

  ```python
  request_url = "https://www.quandl.com/api/v3/datasets/WIKI/AMD.json?api_key="

  # Concatenate request_url and api_key. Store as new variable
  request_url_rfd = request_url + api_key
  ```

If time remains, ask two final, guided questions:

* If a user were to **export** **environment variable** `QUANDL_API_KEY` using a Git Bash terminal but then launched Jupyter Lab in a different terminal window, would Jupyter Lab be able to retrieve the **environment variable**?

  **Answer** No. **Environment variables** are sourced to current and child processes. Because a new terminal window is used to launch Jupyter Lab, the **environment variable** `QUANDL_API_KEY` will be out of scope.

* If **environment variables** are inherited through parent-child processes, what happens when a parent process is terminated?

  **Answer** The **environment variable** is deleted and no longer available for use.

Ask for any remaining questions before moving on.
