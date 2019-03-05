# Now let's boost our Python execution to the next level!
# Sometimes it's cumbersome having to navigate, create folders, and execute Python applications manually,
# so let's use the power of shell scripts (a wrapper around unix commands) to do the heavylifting for us!

# Let's first do some prep work. Create a new folder on your Desktop.
# Note: we are adding the '-p' parameter to the mkdir command
# to alleviate the 'File Exists' error when re-running this shell script multiple times 
mkdir -p ~/Desktop/AutomatedPython

# Now, let's make a copy of your first Python application and move it to the newly created folder
cp hello_world.py ~/Desktop/AutomatedPython/automated_python.py

# Then, navigate to the newly created folder so we can execute the Python application
cd ~/Desktop/AutomatedPython

# Lastly, execute the python application
python automated_python.py
