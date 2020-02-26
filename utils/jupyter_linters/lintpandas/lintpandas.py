# -*- coding: utf-8 -*-
"""Jupyter Notebook Linter.

This module parses all notebooks and runs linters on the code and
markdown cells. A temporary file called `deleteme` is generated from
the notebook's code and markdown cells. This needs to be added to the
gitignore as a backup, but the file should be removed at the end.

Example:

    $ python lintnb path/to/notebooks

Todo:
    * Update README
    * Add to setup.py

"""
import ast
import click
import nbformat
from pandas_vet import VetPlugin
from pathlib import Path
from colorama import init, Fore, Style

def check_code(source, filepath):
    """Lint Notebook Code Cells."""
    # Execute the linter
    try:
        tree = ast.parse(source)
        result = list(VetPlugin(tree).run())
        if result:
            print(
                f"{Fore.YELLOW}"
                f"Found Notebook Error(s) in file {filepath}:"
                f"{Fore.RED}"
                f"\n{result[0]}\n"
                f"{Style.RESET_ALL}"
            )

    except SyntaxError as e:
        print(e)
        print("Source: ", f"\n```python\n{source}\n```")


@click.command()
@click.argument("notebook_directory", default=".")
def cli(notebook_directory):

    # Create Paths
    notebook_path = Path(notebook_directory)
    # Find all notebooks
    # Exclude notebooks ending in `-checkpoints`
    notebooks = notebook_path.glob("**/*[!-checkpoints].ipynb")

    for notebook_path in notebooks:

        # Open each notebook and parse the code cells
        with open(notebook_path, "r") as notebook:
            print(f"Linting: {notebook_path}")
            nb = nbformat.read(notebook, as_version=nbformat.NO_CONVERT)
            for cell in nb.cells:
                if cell.cell_type == "code":
                    check_code(cell.source, notebook_path)


if __name__ == "__main__":
    # Init Colorama and the CLI
    init()
    cli()
