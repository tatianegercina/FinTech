# -*- coding: utf-8 -*-
"""Jupyter Notebook Error Checker.

This module parses all notebooks using nbformat and looks for errors
in the output cells.

Example:

    $ python nberr path/to/notebooks

Todo:
    * Update README
    * Add to setup.py

"""
import sys
import click
import nbformat
from pathlib import Path
from colorama import init, Fore, Style

# Initialize Colorama (Windows Only)
init()


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
            nb = nbformat.read(notebook, as_version=4)
            errors = [
                output
                for cell in nb.cells
                if "outputs" in cell
                for output in cell["outputs"]
                if output.output_type == "error"
            ]
            if errors:
                nb_path = notebook_path.resolve()
                print(
                    f"{Fore.RED}"
                    f"Found Notebook Error(s) in file {nb_path}:"
                    f"{Style.RESET_ALL}"
                )
                print(errors)
                sys.exit(3)


if __name__ == "__main__":
    cli()
