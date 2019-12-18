# HD Derive Wallet Install Guide

This guide serves as a step by step process for setting up the [`hd-wallet-derive` library](https://github.com/dan-da/hd-wallet-derive) used to derive `BIP32` addresses and private keys for Bitcoin and other alternative coins or "altcoins".

## Environment Setup

The `hd-wallet-derive` library is written in the PHP language; therefore you will be required to first set up PHP on your machines before installing and then running the `hd-wallet-derive` library.

**Note:** For the Windows installation, we will be using the XAMPP package, while for the Mac OS X installation, we will have two options; you can update the pre-build PHP version up to `v7.3` or you can use Homebrew.

### Environment Setup in Microsoft Windows Operating System

For those with a **Windows operating system**, execute the following steps:

* Windows machines do not come with a pre-built PHP and Apache Web Server, and therefore will require both. Luckily, there are installers that bundle these two together! Visit the [XAMPP website](https://www.apachefriends.org/index.html) and download the installer for Windows; the XAMPP is a popular PHP development environment that is easy to install and configure.

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

* Next, navigate to the System Environment Variables in the Control Panel and edit the `Path` environment variable; add the path containing the PHP binaries (`C:\xampp\php`) to the end of the `Path` environment variable.

  ![start-menu-environment-search](Images/start-menu-environment-search.PNG)

  ![environment-menu](Images/environment-menu.PNG)

  ![environment-variables](Images/environment-variables.PNG)

  ![environment-path-edit](Images/environment-path-edit.PNG)

* Test that the newest version of PHP is working by first creating a test PHP script called `phpinfo.php` with the following code.

  ```php
  <?php

  // Show all information, defaults to INFO_ALL
  phpinfo();

  ?>
  ```

* Next, execute the following command from the `git-bash` (close any `git-bash` terminal window opened and open a new one if this is your case).

  ```shell
  php -S localhost:8000 phpinfo.php
  ```

* The terminal should output the following and spin up a web server to showcase the results of the test `phpinfo` script. If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!

  ![php-terminal-windows](Images/php-terminal-windows.PNG)

* Open your web browser and navigate to [`http://localhost:8000/`](http://localhost:8000/); you should see the following page with the current PHP configuration in your system.

  ![phpinfo-test](Images/phpinfo-test.PNG)

### Environment Setup in OS X Operating System

For those with a **Mac OS X operating system**, there are two options to install PHP, you can update the OS X pre-built PHP version up to `v7.3`, or you can use the Homebrew package manager. Both methods work great, your choice will depend on weather or not you want or have the rights to use Homebrew in your computer; some corporate computers have policies that restrict the usage of third-party package managers like Homebrew.

#### Option 1: Installing PHP by Updating the Pre-Built PHP in Mac OS X

To update the pre-built version of PHP in OS X execute the following steps:

* Mac OS X already comes pre-built with PHP and the Apache Web Server; however, we will need to upgrade the PHP version to 7.3.

* Open the terminal and execute the following command to download and install PHP version 7.3.

  ```shell
  curl -s https://php-osx.liip.ch/install.sh | bash -s 7.3
  ```

* You will be asked to type your password to install the software package.

  ![PHP OS X install - 1](Images/php-os-x-1.png)

* Once the installation finishes, execute the following command in the terminal to edit your `.bash_profile` in the `nano` text editor.

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

* Execute the following command to reload your `bash_profile`.

  ```shell
  source ~/.bash_profile
  ```

* Close and reopen the terminal. Next, verify that PHP version 7.3 is the current version in your system by executing the following command:

  ```shell
  php -version
  ```

  ![PHP OS X install - 3](Images/php-os-x-3.png)

* Test that the newest version of PHP is working correctly by first creating a test PHP script called `phpinfo.php` with the following code.

  ```php
  <?php

  // Show all information, defaults to INFO_ALL
  phpinfo();

  ?>
  ```

* Next, execute the following command from the terminal.

  ```shell
  php -S localhost:8000 phpinfo.php
  ```

* The terminal should output the following and spin up a web server to showcase the results of the test `phpinfo` script. If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!

  ![php-terminal](Images/php-terminal.png)

* Open your web browser and navigate to [`http://localhost:8000/`](http://localhost:8000/); you should see the following page with the current PHP configuration in your system.

  ![php-test](Images/php-test.png)

#### Option 2: Installing PHP Using the Homebrew Package Manager

To install PHP in Mac OS X using Homebrew execute the following steps:

* Mac OS X already comes pre-built with PHP and the Apache Web Server; however, we will need to upgrade the PHP version to 7.3. Therefore, to do so, make sure that Homebrew, a package manager for Mac OS, is installed on your Mac OS machine. If not, visit the [Homebrew website](https://brew.sh/) and install Homebrew using the given install command.

  ![homebrew-install](Images/homebrew-install.png)

* Once Homebrew is installed, execute the following command in your terminal. This should install the latest version of PHP (7.3 at this current time).

  ```shell
  brew install php@7.3
  ```

* Then, in order to point to the newest version of PHP, export the following path to your `PATH` environment variable. This will allow you to run the command `php` from anywhere in your terminal and point to the Homebrew version that was just installed.

  ```shell
  export PATH=/usr/local/opt/php@7.3/bin:$PATH
  ```

* Append this to your `.bash_profile` by running the following (or manually edit the file):

  ```shell
  echo "export PATH=/usr/local/opt/php@7.3/bin:$PATH" >> ~/.bash_profile
  ```

* Next, test that the newest version of PHP is working correctly by first creating a test PHP script called `phpinfo.php` and then executing the following command.

  ```php
  <?php

  // Show all information, defaults to INFO_ALL
  phpinfo();

  ?>
  ```

  ```shell
  php -S localhost:8000 phpinfo.php
  ```

* The terminal should output the following and spin up a web server to showcase the results of the test `phpinfo` script. If you see the following output, then congratulations! Your machine is now updated to the newest version of PHP!

  ![php-terminal](Images/php-terminal.png)

* Open your web browser and navigate to [`http://localhost:8000/`](http://localhost:8000/); you should see the following page with the current PHP configuration in your system.

  ![php-test](Images/php-test.png)

## hd-wallet-derive Installation

Now that the latest version of PHP is installed on our machines, we can now proceed to the installation of the `hd-wallet-derive` library.

Execute the following steps:

* Navigate to the [Github website](https://github.com/dan-da/hd-wallet-derive) for the `hd-wallet-derive` library and scroll down to the installation instructions.

  ![hd-wallet-derive-github](Images/hd-wallet-derive-github.png)

* Next, open a terminal and execute the following commands. If you are using Windows, you will need to open the `git-bash` GUI via `C:\Program Files\Git\bin\bash.exe` directly to enable something called `tty` mode that makes the terminal more compatible with Unix systems. Once installed, you may move back to using the usual `git-bash` terminal.

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
