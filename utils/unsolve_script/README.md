# Unsolve Script

This script will allow you to remove all solved activities from an Activities folder.

## Installation

```
pip install -e .
```

![Installation](Images/unsolve_install.gif)

## Usage

* Help menu


```
unsolve --help

Usage: unsolve [OPTIONS]

Options:
  -i, --ipath TEXT  Activities Input Path
  -o, --opath TEXT  Unsolved Output Path
  -f, --force       Force Overwriting Unsolved
  --help            Show this message and exit.
```

* Creates an `Unsolved` folder directly in the unit day folder


```
cd 01-Lesson-Plans/03-Python/1
unsolve
```

  ![Basic Usage](Images/unsolve_usage.gif)

* Specify input and output path


```
unsolve -i 03-Python/1/Activities -o /path/to/student/repo/03-Python/1
```

  ![Usage with Paths](Images/unsolve_paths.gif)

* Force overwriting an existing `Unsolved` folder


```
unsolve -i 03-Python/1/Activities -o /path/to/student/repo/03-Python/1 --force
```

  ![Usage with Force](Images/unsolve_force.gif)
