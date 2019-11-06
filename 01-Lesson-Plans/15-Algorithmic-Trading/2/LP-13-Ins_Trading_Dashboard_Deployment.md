### 13. Instructor Do: Trading Dashboard Deployment

In this section, students will become familiar with the expansive CCXT library, which provides an API for over 120 cryptocurrency exchanges. In particular, students will work with the Kraken API and extract both historical and current price data.

**File:** [ccxt_demo.ipynb](Activities/03-Ins_Going_Live/Solved/ccxt_demo.ipynb)

Open the solution file and review the following:

MyBinder
Binder allows you to create custom computing environments that can be shared and used by many remote users. MyBinder is a public, free hosting option, with limited compute and memory resources, which will allow you to deploy your simple app quickly and easily.

Here we will take you through the configuration to quickly set up a GitHub repository with notebooks containing Panel apps for deployment on MyBinder.org. As an example refer to the Clifford demo repository.

Create a GitHub repository and add the notebook or script you want to serve (in the example repository this is the clifford.ipynb file)

Add an environment.yml which declares a conda environment with the dependencies required to run the app (refer to the conda documentation to see how to declare your dependencies).

Next, add a panelserverextension.py file to the repository containing a function which will launch the Panel server. Ensure you update the name of the notebook or script that you want to launch:

from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the clifford.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "clifford.ipynb", "--allow-websocket-origin=*"])
Now add a postBuild file to the repository which activates the server extension:
# enable nbserverproxy
jupyter serverextension enable --sys-prefix nbserverproxy
# install the panel server extension so that
# panel launches at startup
mv panelserverextension.py ${NB_PYTHON_PREFIX}/lib/python*/site-packages/
# enable panel extension
jupyter serverextension enable --sys-prefix panelserverextension
Go to mybinder.org, enter the URL of your GitHub repository and hit Launch

mybinder.org will give you a link to the deployment, e.g. for the example app it is https://mybinder.org/v2/gh/panel-demos/clifford-interact/master. To visit the app simply append ?urlpath=/proxy/5006/clifford where you should replace clifford with the name of the notebook or script you are serving.

Heroku
Heroku makes deployment of arbitrary apps including Panel apps and dashboards very easy and provides a free tier to get you started. This makes it a great starting point for users not too familiar with web development and deployment.

To get started working with Heroku signup for a free account and download and install the CLI. Once you are set up follow the instructions to log into the CLI.

Create a new Git repo (or to follow along clone the minimal-heroku-demo GitHub repo)

Add a Jupyter notebook or Python script which declares a Panel app or dashboard to the repository.

Define a requirements.txt containing all the requirements for your app (including Panel itself). For the sample app the requirements are as minimal as:

panel
hvplot
scikit-learn
Define a Procfile which declares the command Heroku should run to serve the app. In the sample app the following command serves the iris_kmeans.ipynb example. The websocket origin should match the name of the app on Heroku app-name.herokuapp.com which you will declare in the next step:
web: panel serve --address="0.0.0.0" --port=$PORT iris_kmeans.ipynb --allow-websocket-origin=app-name.herokuapp.com
Create a Heroku app using the CLI ensuring that the name matches the URL we declared in the previous step:
heroku create app-name
Push the app to heroku and wait until it is deployed.

Visit the app at app-name.herokuapp.com

Once you have deployed the app you might find that if your app is visited by more than one user at a time it will become unresponsive. In this case you can use the Heroku CLI to scale your deployment.
