# Jupyter Linters

This is a collection of CLIs to lint Jupyter Notebooks. These parse the JSON to find the code, markdown, and output cells and creates temporary files from the cells for linting.

lintnb - Runs `pycodestyle` and `cspell` on notebook code and markdown cells.

nbspell - Builds a list of spelling errors for a given directory.

nberr - Checks notebook output cells for errors.

nbdiff - Checks to see if the code in the Unsolved notebooks matches the code in the Solved.

## Installation

```shell
cd utils/jupyter_linters
pip install -e .
```

![Install](Images/install.gif)

- - -

## Help menus


```shell
lintnb --help
Usage: lintnb [OPTIONS] [NOTEBOOK_DIRECTORY]

Options:
  --help  Show this message and exit.
```


```shell
nberr --help
Usage: nberr [OPTIONS] [NOTEBOOK_DIRECTORY]

Options:
  --help  Show this message and exit.
```


```shell
nbspell --help
Usage: nbspell [OPTIONS] [NOTEBOOK_DIRECTORY]

Options:
  --help  Show this message and exit.
```

```shell
nbdiff --help
Usage: nbdiff [OPTIONS] [ACTIVITIES_DIRECTORY]

Options:
  --help  Show this message and exit.
- - -

## Usage

Check local directory

```shell
lintnb
```

![lintnb](Images/lintnb.gif)

```shell
nberr
```

![nberr](Images/nberr.gif)

```shell
nbspell
```

![nbspell](Images/nbspell.gif)

Check specified notebook directory

```shell
lintnb path/to/notebooks
```

```shell
nberr path/to/notebooks
```

```shell
nbspell path/to/notebooks
```

```shell
nbdiff path/to/Activities
```
