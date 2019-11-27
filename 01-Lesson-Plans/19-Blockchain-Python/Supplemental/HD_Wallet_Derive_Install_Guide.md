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

* The terminal should output the following and spin up a web server to showcase the results of the test `phpinfo` script.

  ![php-terminal](Images/php-terminal.png)

  ![php-test](Images/php-test.png)

## Installation

## Execution

---

© 2019 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
