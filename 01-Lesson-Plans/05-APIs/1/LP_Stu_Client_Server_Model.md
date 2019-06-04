### 4. Students Do: Eavesdropping on the Server (10 mins)

This activity drives home the discussion on the client server model by having students surf the web with the browser's developer console open. Students will visit websites like Facebook and Yahoo, as well as complete a Google search, and they will read the standard output from the console to get a better idea of what data is sent between client and server as students navigate sites. This will communicate to students that every click and API call brokers a connection between client and server and data is transmitted between the two.

**Instructions:**

* [README.md](Activities/04-Stu_Client_Server/README.md)

### 5. Instructor Do: Review Client-Server Model (5 mins)

**Files:**

* [eavesdropping.md](Activities/04-Stu_Client_Server/Solved/eavesdropping.md)

Open the solution and walkthrough the following:

* Firefox, Chrome, and Safari all offer developer consoles that allow users to see requests being exchanged between clients and servers.

  ![first_response.png](Activities/04-Stu_Client_Server/Images/first_response.png)

* Requests sent from a client to a server are commonly either `GET` or `POST`. `GET` requests retrieve data from a server. `POST` requests submit data to a server.

  ![console_comm.png](Activities/04-Stu_Client_Server/Images/console_comm.png)

* Both types of requests are submitted using URLs. These URLs can be customized to specify what should be retrieved with the `GET` function and what should be submitted with the `POST` request. For example, searching on Google submits a `GET` request, and the search term/query is transmitted to the Google servers with the `GET` request.

  ![console_search.png](Activities/04-Stu_Client_Server/Images/console_search.png)

Ask students some of the following review questions:

* Website images are saved on website servers. When an image loads, what type of request is sent from the client to the server?

  > "`GET` request"

* Explain the client-server model from the perspective of emails.

  > "Servers provided by companies like Google, Yahoo, Microsoft, etc. are used to store and distribute email messages. Email applications and internet browsers are clients that are used to specify who emails are sent to and the body of emails. Clients are used to submit email content to servers, and then servers distribute the message to the corresponding email targets."

* If time remains, round robin and ask some students to give details about the data they saw transmitted. This will allow students to compare what they say with what others saw. It will also help students understand some of the common data exchanges, such as user credentials and search queries.

Ask for any remaining questions before moving on.
