# HD Derive Wallet Install Guide

This guide serves as a step by step process for setting up the `hd-wallet-derive` library used to derive BIP32 addresses and private keys for Bitcoin and other alternative coins or "altcoins".

## Environment Setup

The `hd-wallet-derive` library is written in the PHP language, therefore students will be required to first set up PHP on their machines before installing and then running the `hd-wallet-derive` library.

For those with a Windows operating system, execute the following steps:

* Visit the [XAMPP website](https://www.apachefriends.org/index.html) and download the installer for your appropriate operating system (Windows or Mac); XAMPP is a popular PHP development environment that is easy to install and configure.

For those with a Mac OS X operating system, execute the following steps:

* Mac OS X already comes pre-built with PHP and the Apache Web Server; however, we will need to upgrade the PHP version to 7.3. Therefore, to do so make sure that Homebrew, a package manager for Mac OS, is installed on your Mac OS machine. If not, visit the [Homebrew website](https://brew.sh/) and install Homebrew using the given install command.

  ![homebrew-install](Images/homebrew-install.png)

* Once Homebrew is installed, execute the following command in your terminal. This should install the latest version of PHP (7.3 at this current time).

  ```shell
  brew install php
  ```

* Then, in order to point to the newest version of PHP, export the following path to your `PATH` environment variable. This will allow you to run the command `php` from anywhere in your terminal and point to the Homebrew version that was just installed.

  ```shell
  export PATH=$PATH:/usr/local/bin
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

  ![php-test](Images/php-test.png)

## Installation

Now that the latest version of PHP is installed on our machines, we can now proceed to the installation of the `hd-wallet-derive` library.

Execute the following steps:

* Navigate to the [Github website](https://github.com/dan-da/hd-wallet-derive) for the `hd-wallet-derive` library and scroll down to the installation instructions.

  ![hd-wallet-derive-github](Images/hd-wallet-derive-github.png)

* Next, open a terminal and execute the following commands.

  ```shell
  git clone https://github.com/dan-da/hd-wallet-derive
  cd hd-wallet-derive
  php -r "readfile('https://getcomposer.org/installer');" | php
  php composer.phar install
  ```

* You should now have a folder called `hd-wallet-derive` containing the PHP library.

## Execution

Last step! Execute the `hd-wallet-derive` library to derive derive BIP32 addresses and private keys for Bitcoin and other alternative coins.

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
