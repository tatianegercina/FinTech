# Eavesdropping on the Server

Every time someone uses the internet or a network, a client sends a message to a server, and that server responds. Explore the relationship between `client` and `server` in more detail by navigating the web with an internet browser and eavesdropping in on the communications sent between `client` and `server`. Review the data that is sent between the client and server with an internet browser's developer console.

The process of launching the developer console for an internet browser is different for each browser.

Links to documentation for Firefox, Chrome, and Safari can be found [here](https://support.airtable.com/hc/en-us/articles/232313848-How-to-open-the-developer-console).

## Instructions

Navigate to the websites below with the developer console open to review the exchanges between the client (browser) and server (websites visited).

1. Open an internet browser, and launch the developer console. Consult the following links for help with getting the developer console open. Instruction is provided for each browser.

    * [Open Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/open)

    * [Firefox Browser Console](https://developer.mozilla.org/en-US/docs/Tools/Browser_Console)

    * [Open the Console developer tool in Microsoft Edge](https://docs.microsoft.com/en-us/microsoft-edge/devtools-guide/console)

2. On the developer console, select `network`.

    ![network_console](Images/network_console.gif)

3. Navigate to `https://www.un.org/`.

4. Review the output in the developer console. Compare the `POST` requests with the `GET` requests.

    **Note:** In Google Chrome, you need to right-click on the column names and choose the `Method` option to visualize the `POST` and `GET` requests.

    ![network_traffic](Images/network_traffic.gif)

5. Scroll to the top of the console and identify the first request sent to the server. This was the first message sent by the client to the server when the site was accessed.

6. Return to Google with the console open and search Google with the phrase `FinTech`.

7. Review the output in the developer console.

8. Visit `https://finance.yahoo.com/` and search for a ticker. Review the developer console as you submit the request.

9. Continue to navigate the internet with the developer console open. Take note of the type of requests that are sent for each site visited (how many POST vs. GET). Also, take into consideration the differences in API URLs.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
