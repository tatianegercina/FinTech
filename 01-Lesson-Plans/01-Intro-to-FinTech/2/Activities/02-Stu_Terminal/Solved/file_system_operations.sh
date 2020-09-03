# This bash shell script performs the following file system operations.

# Check current directory.
pwd

# Navigate to your Desktop.
cd ~/Desktop

# Confirm your current working directory is at the Desktop.
pwd

# Create a folder called `Pets`.
mkdir Pets

# Navigate into the folder.
cd Pets

# Inside `Pets`, create two folders: `Dogs` and `Cats`.
mkdir Dogs
mkdir Cats

# Navigate into `Cats`.
cd Cats

# Create an empty file named `name.txt`.
touch name.txt

# Edit the file `name.txt` with VS Code.
code name.txt

# Read the file `name.txt` and output the results to the console.
cat name.txt

# Navigate back one level (to the root of the `Cats` folder).
cd ..

# Copy the file `name.txt` into `Dogs`.
cp Cats/name.txt Dogs/

# Delete the folder `Cats` and its contents.
rm -r Cats

# Rename the folder `Dogs` to `Lucky`.
mv Dogs Lucky

# List the contents of the root of the `Pets` folder.
ls