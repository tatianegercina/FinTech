### 9. Students Do: Building the Accident Report System (20 min)

In this activity, students will build the same Accident Report System, leveraging IPFS and event filters.

Send out the instructions and the starter code, and have TAs circulate the room, ensuring that students are following the instructions properly.

**Instructions:**

* [README.md](Activities/09-Stu_Accident_Report_System/README.md)

**Files:**

* [crypto.py](Activities/09-Stu_Accident_Report_System/Unsolved/crypto.py)

* [accident.py](Activities/09-Stu_Accident_Report_System/Unsolved/accident.py)

* [.env](Activities/09-Stu_Accident_Report_System/Unsolved/.env)

If students are having difficulties, make sure of the following:

* The student has installed the `python-dotenv` package. This can be done by running the following command:

```bash
pip install python-dotenv
```

* The `header` object is properly configured, and that the Pinata API secrets are saved to the `.env` file properly.

* The `.env` file contains the proper values (all should be filled in).

* The ABI is copied from Remix and pasted into the `CryptoFax.json` file.

* Students are `cd`'d into the same directory as the rest of the `.env`, `CryptoFax.json`, `crypto.py`, and `accident.py` files.

* Ganache is running and the `WEB3_PROVIDER_URI` points to it.

### 10. Instructor Do: Review Accident Report System (10 min)

**Files:**

* [crypto.py](Activities/09-Stu_Accident_Report_System/Solved/crypto.py)

* [accident.py](Activities/09-Stu_Accident_Report_System/Solved/accident.py)

Open `crypto.py` and explain the following:

* This file is used to establish functions dealing with the Pinata API and creating the function for returning the `cryptofax` contract object.

* The `requests` library is used to `POST` some JSON data to Pinata, and return the corresponding IPFS URI.

Open up `accident.py` and explain the following:

* The `createAccidentReport` function collects all of the user input, including the `time`, `description`, and `token_id`, converts it to valid JSON, then pins it to IPFS.

* The `reportAccident` function takes in the final `token_id` and `report_uri` and sends it as a transaction to the `CryptoFax` contract's `reportAccident` function, which emits an `Accident` event that we can filter for later.

* The `getAccidentReports` function simply filters for all `Accident` events on the contract that match the `token_id`, from the genesis block to now.

* The `main` function checks the command line arguments, and decides which path to take. If the `sys.argv[1]` argument is `report`, meaning we ran `python accident.py report` in our terminal, then we create and print an accident report.

* If `sys.argv[1]` is `get`, we follow the `getAccidentReports` flow. By running a command like `python accident.py get 1`, we can parse out the `sys.argv[2]` to be the `token_id` and use that for our event filter.

Ask for any remaining questions before moving on.

---

### 11. BREAK (15 min)

---

### 12. Instructor Do: Intro to Project 3 (15 min)

Greet the class and explain that today is the first day of their final project!

Congratulate the class on having made it this far!

Explain that, over the next two class weeks, students will work in groups to complete capstone project for FinTech.

Explain that students can choose any topic from any section of the course as their capstone project. Point out that this allows them to align their capstone project with their specific career goals, and that the final project does not have to focus on Blockchain.

Tell students that they will also be able to choose their own teams of 2-6 students for this final project. Students are also able to request placement on a team by the instructional staff.

Explain that the rest of class will be dedicated to working on their final projects.

### 13. Student Do: Project Work! (Remaining Class Time)

Students will work on their final projects for the remainder of the class.

---

### End Class

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
