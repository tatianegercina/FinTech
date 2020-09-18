# HD Derive Wallet Install Guide

This guide serves as a step by step process for setting up the [`hd-wallet-derive` library](https://github.com/dan-da/hd-wallet-derive) used to derive `BIP32` addresses and private keys for Bitcoin and other alternative coins or "altcoins."

## Environment Setup

The `hd-wallet-derive` library is written in the PHP language; therefore, you will be required to first set up PHP on your machines before installing and then running the `hd-wallet-derive` library.

**Note:** For the Windows installation, we will be using the XAMPP package, while for the Mac OS X installation, we will have two options; you can update the pre-build PHP version up to `v7.3` or you can use Homebrew.

## Screencast Videos

If you need additional help in the installation process, you can follow the step by step video guides in the following links.

### Microsoft Windows Users

* [Installing PHP Version 7.3 for Windows](https://youtu.be/IvcZZaIEL_4)

* [HD Derive Wallet Install for Windows](https://youtu.be/A_tqm4j4vsY)

### Mac OS X Users

* [Installing PHP Version 7.3 for MAC - Option 1](https://youtu.be/Q3RA7PiW9Ws)

* [Installing PHP Using the Homebrew Package Manger for Mac - Option 2](https://youtu.be/SNRQSwlOKbs)

* [HD Derive Wallet Install for Mac](https://youtu.be/c-Qc3Pss6oM)


### Environment Setup in Microsoft Windows Operating System

For those with a **Windows operating system**, execute the following steps:

* Windows machines do not come with a pre-built PHP and Apache Web Server, and therefore will require both. Luckily, some installers bundle these two together! Visit the [XAMPP website](https://www.apachefriends.org/index.html) and download the installer for Windows; the XAMPP is a popular PHP development environment that is easy to install and configure.

 ![XAMPP-website](Images/XAMPP-website.png)

* Use the XAMPP package to install PHP and its associated dependencies. Keep the defaults for now unless there is a dependency conflict.

 ![XAMPP-install](Images/XAMPP-install.PNG)

* Then, once the XAMPP package is installed, navigate to the folder where the PHP binaries are located. This should be at `C:\xampp\php`.

 ![xampp-path](Images/xampp-path.PNG)

* Edit the `php.ini` file (`C:\xampp\php\php.ini`) using Notepad and add the following line at the end of the file:

 ```shell
 extension=php_gmp.dll
 ```

* This will enable a necessary PHP extension that `hd-wallet-derive` relies on.

* Next, you need to update the System Environment Variables and add the path containing the PHP binaries (`C:\xampp\php`) to the `PATH` environment variable.

* For this particular step, we will use the Windows Command Prompt as Administrator. In the Cortana search field, type in CMD; you will see the Command Prompt application in the search results, choose the "Run as administrator" option to continue.

 ![Open CMD as Admin](Images/cmd-as-admin.png)

* You will be asked if you want the Command Prompt to make changes in your system, click on the "Yes" button to continue.

 ![Open CMD as Admin - 2](Images/cmd-as-admin-2.png)

* You will be able to run commands as administrator if you see the title `Administrator: Command Prompt` in the window. In the administrator's prompt, it’ll say `Administrator`, while other prompts will not.

 ![Open CMD as Admin - 3](Images/cmd-as-admin-3.png)

* Now type the following command to update the `PATH` system variable.

 ```shell
 setx /M PATH "%PATH%;C:\xampp\php"
 ```

* If everything was successful, you will see a confirmation message.

 ![Open CMD as Admin - 4](Images/cmd-as-admin-4.png)

* Test that the newest version of PHP is working. Close all the terminal windows (`git-bash` and Windows Command Prompt), open a new `git-bash` terminal windows, and execute the following command.

 ```shell
 php -version
 ```

* If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!

 ![Open CMD as Admin - 5](Images/cmd-as-admin-5.png)

 * If you do not see something similar to the above output when running ` php -version`, then your environement varibles may not be set correctly. Perform the steps in the below troubleshooting section to make sure that your environment variables are correctly set.

#### Windows Environment Troubleshooting

> WARNING: If you run into the errror `The data being saved is truncated to 1024 characters` then you most likely need to perform the below steps.

1. Click the Windows search and search for `System Properties`, then launch the application.

2. Next at the bottom of the dialog click `Environment variables`.

3. Then under `System Variables` find the `Path` variable and click `edit`.

4. Now click `New` and enter your XAMP path, e.g.  `C:\xampp\php`.

5. Finish by clicking `OK` on each window.

![System Properties Add environment Variable](Images/windows-set-environment_variables.png)


### Environment Setup in OS X Operating System

For those with a **Mac OS X operating system**, there are two options to install PHP, you can update the OS X pre-built PHP version up to `v7.3`, or you can use the Homebrew package manager. Both methods work great. Your choice will depend on whether or not you want or have the right to use Homebrew in your computer; some corporate computers have policies that restrict the usage of third-party package managers like Homebrew.

#### Option 1: Installing PHP by Updating the Pre-Built PHP in Mac OS X

To update the pre-built version of PHP in OS X, execute the following steps:

* Mac OS X already comes pre-built with PHP and the Apache Web Server; however, we will need to upgrade the PHP version to 7.3.

* Open the terminal and execute the following command to download and install PHP version 7.3.

 ```shell
 curl -s https://php-osx.liip.ch/install.sh | bash -s 7.3
 ```

* You will be asked to type your password to install the software package.

 ![PHP OS X install - 1](Images/php-os-x-1.png)

* **Important:** If you are on macOS Catalina and up (10.15+), your default shell is now `zsh`, instead of `bash` as in previous versions. No worries, however, since `zsh` can handle the same tasks. If you have yet to upgrade to Catalina, you will be using `bash` as your default shell, which will affect the commands you need to run below. Make sure you are running the commands appropriate for your system!

* Once the installation finishes, execute the command appropriate for your system:

  * macOS Catalina and above (`zsh` shell):

    ```shell
    nano ~/.zshrc
    ```

  * Versions prior to macOS Catalina (`bash` shell):

    ```shell
    nano ~/.bash_profile
    ```

* The `nano` text editor will be opened, scroll down to the end of the file and add the following commands to point to the newest version of PHP globally in your system.

 ```shell
 # PHP Path Config
 export PATH=/usr/local/php5/bin:$PATH
 export PATH
 ```

 ![PHP OS X install - 2](Images/php-os-x-2.png)

* Save the changes by pressing the `CONTROL + O` keys combination. Next, exit `nano` by pressing the `CONTROL + X` keys combination.

* **Close and reopen the terminal**. Next, verify that PHP version 7.3 is the current version in your system by executing the following command:

 ```shell
 php -version
 ```

* If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!

 ![PHP OS X install - 3](Images/php-os-x-3.png)

#### Option 2: Installing PHP Using the Homebrew Package Manager

To install PHP in Mac OS X using Homebrew, execute the following steps:

* Mac OS X already comes pre-built with PHP and the Apache Web Server; however, we will need to upgrade the PHP version to 7.3. Therefore, to do so, make sure that Homebrew, a package manager for Mac OS, is installed on your Mac OS machine. If not, visit the [Homebrew website](https://brew.sh/) and install Homebrew using the given install command.

 ![homebrew-install](Images/homebrew-install.png)

* Once Homebrew is installed, execute the following command in your terminal. This should install the latest version of PHP (7.3 at this current time).

 ```shell
 brew install php@7.3
 ```

* **Important:** If you are on macOS Catalina and up (10.15+), your default shell is now `zsh`, instead of `bash` as in previous versions. No worries, however, since `zsh` can handle the same tasks. If you have yet to upgrade to Catalina, you will be using `bash` as your default shell, which will affect the commands you need to run below. Make sure you are running the commands appropriate for your system!

* Execute the command appropriate for your system:

  * macOS Catalina and above (`zsh` shell):

    ```shell
    echo "export PATH=/usr/local/opt/php@7.3/bin:$PATH" >> ~/.zshrc
    ```

  * Versions prior to macOS Catalina (`bash` shell):

    ```shell
    echo "export PATH=/usr/local/opt/php@7.3/bin:$PATH" >> ~/.bash_profile
    ```

* Close and reopen the terminal. Next, verify that PHP version 7.3 is the current version in your system by executing the following command:

 ```shell
 php -version
 ```

* If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!

 ![PHP OS X install - 3](Images/php-os-x-3.png)

## hd-wallet-derive Installation

Now that the latest version of PHP is installed on our machines, we can now proceed to the installation of the `hd-wallet-derive` library.

Execute the following steps:

* Navigate to the [Github website](https://github.com/dan-da/hd-wallet-derive) for the `hd-wallet-derive` library and scroll down to the installation instructions.

 ![hd-wallet-derive-github](Images/hd-wallet-derive-github.png)

* Next, open a terminal and execute the following commands. If you are using Windows, you will need to open the `git-bash` GUI via `C:\Program Files\Git\bin\bash.exe` directly to enable something called `tty` mode that makes the terminal more compatible with Unix systems. Once installed, you may move back to using the usual `git-bash` terminal.

> **Warning**: When cloning the project be conscious of what folder you are cloning the files into. It would probably be best to clone it into your `Blockchain-Tools` folder.

 ```shell
 git clone https://github.com/dan-da/hd-wallet-derive
 cd hd-wallet-derive
 php -r "readfile('https://getcomposer.org/installer');" | php
 php -d pcre.jit=0 composer.phar install
 ```

* You should now have a folder called `hd-wallet-derive` containing the PHP library.

## hd-wallet-derive Execution

Last step! Execute the `hd-wallet-derive` library to derive `BIP32` addresses and private keys for Bitcoin and other alternative coins.

* Navigate to your `hd-wallet-derive` folder.

 ![hd-wallet-derive-folder](Images/hd-wallet-derive-folder.png)

* Then execute the following commands (these are examples from the GitHub website).

 ```shell
 ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c
 ```

 ```shell
 ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change
 ```

 ![hd-wallet-derive-execute](Images/hd-wallet-derive-execute.png)

* Congratulations! The `hd-wallet-derive` library should now be working and good to go!

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
