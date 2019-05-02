# -*- coding: utf-8 -*-
"""Jupyter Notebook Spell Checker.

This module parses all notebooks and runs cspell on the code and
markdown cells. Any misspelled words are added to a set of words.
This set of words is printed at the very end. It is recommended to
run this code per unit and update the unit-level spelling dictionary.

Example:

    $ python nbspell path/to/unit

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
cspell_regex = re.compile(r"(Unknown word: )(?P<word>.*?)\n", re.S)

# Store all unknown words
cspell_set = set()


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
        # Find any misspelled words and add to the set
        matches = cspell_regex.search(completed.stdout.decode("utf-8"))
        if matches:
            cspell_set.add(matches.group("word"))


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

    # Show the final set of misspelled words
    print(cspell_set)


if __name__ == "__main__":
    cli()
