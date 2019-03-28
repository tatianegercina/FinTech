# Bld Script

This script will allow you to quickly scaffold an Activities folder.

## Installation

```
pip install -e .
```

## Usage

* Help menu

```shell
bld --help
```


* Build the activity folder

```shell
bld 01-Ins_First_Activity
```

  ![Usage with Paths](Images/unsolve_paths.gif)

* Force overwriting an existing `Unsolved` folder


```
unsolve -i 03-Python/1/Activities -o /path/to/student/repo/03-Python/1 --force
```

  ![Usage with Force](Images/unsolve_force.gif)
