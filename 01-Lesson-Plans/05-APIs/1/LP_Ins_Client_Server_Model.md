### 3. Instructor Do: Client Server Model (5 mins)

Now that students know what APIs are and how to execute them, it's time they learn what goes on in the back-end when an API request is sent. Students will learn the various components of the `client-server model` through instructor demonstration.

Part of the demonstration will include showing students the client-server model by `pinging` Yahoo Finance. Make sure to have a terminal open and ready for the demo.

**Files:**

* [solution.py](Activities/01-Ins_Really_Important/Solved/solution.py)

Navigate to the 5.1 slides for the `client-server model`, and highlight the following:

* Explain the `client-server model` architecture. Indicate that the model encompasses the relationship between clients and servers.

* Define the `client-server` model as structure that outlines the relationship and flow of communication between two components: a `client` and a `server`.

* A `client` is any tool or application that is used to connect to or communicate with a server. This includes internet browsers, mobile devices, and command line terminals, just to name a few. `Clients` submit requests to servers, and clients receive responses from servers.

* A `server` is a computer program or device/hardware. `Servers` run some form of application and are tasked with interacting and providing functionality to `clients`. `Servers` receive requests from `clients`, and `servers` send responses back to clients.

* Communicate that the `client-server model` is what handles all traffic and requests sent to a server. This includes websites, APIs, and databases. The `client-server model` architecture ensures that requests calls/tasks made to servers are handled appropriately and effectively. When students check Yahoo Finance or login to Facebook.com, they're enacting the client-server model.

Demonstrate the `client-server` model by using the terminal to `ping` Yahoo finance.

* Open a terminal.

* Use the `ping` command to send a request to Yahoo Finance. Explain to students that the `ping` is a utility used to test connectivity to a server.

  ```shell
  ping finance.yahoo.com
  ```

* Explain the output from the `ping` command. Underscore that with every execution of the `client-server` model, data is transmitted over a network. This data is called `packets`. An example of data contained inside of `packets` are user credentials for a website (i.e. Amazon). When transmission is successful, the number of `packets sent` will match the number of `packets received`.

  ![client_server_ping.png](Images/client_server_ping.png)

Ask students the following questions:

* In this scenario, what is the `client` and what is the `server`?

  > "The terminal is the `client` and Yahoo Finance's server(s) are the `server`."

* Was the request sent to Yahoo Finance via the Terminal a successful execution of the `client-server model` based on packets sent and received?

  > "Yes, all packets that were sent to the server were received."

Ask students if there are any questions before moving on.
