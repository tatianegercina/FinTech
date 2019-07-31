# Terminal Commands #

## Directories ##

* `List Directory`

  > ls

  Displays the content of the current directory.

  > ls -la

  Lists the detailed contents of the current directory, including hidden files.

* `Print Working Directory`

  > pwd

  Displays the path to the directory you're currently in.

* `Change Directory`

  > cd \<directory>

  Opens the \<directory> folder. This folder must be present in your current directory.

  > cd ..

  Navigates to the parent directory whih is indicated by `..`. This command essentially exits the current folder and brings you to the folder that contains it.

  > cd ~

  Navigates to the root directory.

* `Make Directory`

  > mkdir \<directory>

  Makes a new folder with the name \<directory>. 

* `Remove Directory`

  > rm -r \<directory>

  Deletes the folder \<directory> and all the files within it.

* `Copy Directory`

  > cp -r \<directory1> \<directory2>

  Copies \<directory1> and its contents into \<directory2>. If there is already a folder named \<directory1> within \<directory2>, the contents of the folder that was already present will be overwritten by the \<directory1> you're copying into the folder.

* `Move Directory`

  > mv \<directory1> \<directory2>

  Moves \<directory1> into \<directory2>. This will not work if there is already a folder in \<directory1> with the name \<directory2>.

  > mv \<directory> ..

  Moves \<directory> into the parent directory. `..` always refers to the parent directory. 

## Files ##

* `Create File`

  > touch \<file>

  Creates a new \<file> in the current directory. Remember to include the file extension. If there is already a file with the name \<file>, it will just update the last modified time of the file.

* `Delete File`

  > rm \<file>

  Deletes the file with the name \<file>.

* `Copy File`

  > cp \<file> \<directory>

  Copies the \<file> into the \<directory> folder. If there is already a file named \<file>, the file that is already present will be overwritten by the new \<file> you're copying in.

* `Rename File`

  > mv \<old-name> \<new-name>

  Renames a file named \<old-name> into \<new-name>. 

* `Move File`

  > mv \<file> \<directory>

  Moves a file named \<file> into the \<directory> folder. If there is already a file named \<file>, the file that is already present will be overwritten by the new \<file> you're moving in.

## Utility 

* `Clear Screen`

  > clear

  Clears the terminal screen so you don't have to sift through the previous inputs.

* `Previous Command`

  > ↑

  Uses the up arrow to navigate to previous commands you've used in terminal.

* `Tab Completion`

  > [Tab ↹]

 Uses the Tab key to autocomplete the current file or directory you're typing in. If there are multiple files or directories with similar names, the autocomplete operation will complete up to the point where the names diverge. You can use tab completion again afterward if you've narrowed down which name you're trying to type.

* `Closing a process`

  PC
  > [Ctrl] + c

  Mac
  > [Control] + c

Ends the current process that's running in your terminal. This could be the `manual` or `node` or any of the many things that may take up the terminal window.

 - - - 

 © 2019 Trilogy Education Services