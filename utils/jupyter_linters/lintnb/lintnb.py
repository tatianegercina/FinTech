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
import re
import click
import nbformat
import subprocess
from pathlib import Path
from colorama import init, Fore, Style

# Initialize Colorama (Windows Only)
init()

# Regex to highlight spelling issues
cspell_regex = re.compile(r"(Unknown word: )(.*?)\n", re.S)


def check_code(linter_commands):
    """Lint Notebook Code Cells."""
    # Execute the linter
    try:
        completed = subprocess.run(
            linter_commands, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
    except subprocess.CalledProcessError as err:
        print("Error: ", err)
    else:
        print(
            cspell_regex.sub(
                f"\g<1>{Fore.RED}\g<2>\n{Style.RESET_ALL}",
                completed.stdout.decode("utf-8"),
            )
        )


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
            code_cells = [i.source for i in nb.cells if i.cell_type == "code"]
            code_cells_str = "\n".join(code_cells).strip()
            md_cells = [i.source for i in nb.cells if i.cell_type == "markdown"]
            md_cells_str = "\n".join(md_cells).strip()

            # Output the code cells to a temp file for linting
            tmp_path = Path(f"deleteme")
            tmp_path.write_text(code_cells_str)

            print(f"Linting file: {notebook_path.resolve()}")

            # Run pycodeStyle for code cells
            linter_commands = ["pycodestyle", "--show-source", "--ignore=E302,W292", tmp_path]
            check_code(linter_commands)

            # Run cspell for code cells
            linter_commands = ["cspell", "-u", tmp_path]
            check_code(linter_commands)

            # Output the markdown cells to a temp file for linting
            tmp_path.write_text(md_cells_str)

            # Run cspell for markdown cells
            linter_commands = ["cspell", "-u", tmp_path]
            check_code(linter_commands)

            # Clean up temp file
            tmp_path.unlink()


if __name__ == "__main__":
    cli()
