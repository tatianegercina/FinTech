# -*- coding: utf-8 -*-
"""Jupyter Notebook Diff for Unsolved and Solved.

This module parses all notebooks in an Activity folder and compares the
Unsolved notebook source code to the Solved. If the Unsolved code is not found
in the Solved folder then an error is thrown. The assumption is that the
Unsolved notebooks should only contain comments or starter code from the Solved.
Comments are stripped from the code and not compared.

Example:

    $ python nbdiff path/to/Activities

Todo:
    * Update README
    * Add to setup.py

"""
import click
import nbformat
from pathlib import Path

from io import StringIO
import tokenize


def remove_comments_and_docstrings(source):
    """
    Returns 'source' minus comments and docstrings.

    modified from https://stackoverflow.com/a/2962727
    """
    io_obj = StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        # The following two conditionals preserve indentation.
        # This is necessary because we're not using tokenize.untokenize()
        # (because it spits out code with copious amounts of oddly-placed
        # whitespace).
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        # Remove comments:
        if token_type == tokenize.COMMENT:
            pass
        # This series of conditionals removes docstrings:
        elif token_type == tokenize.STRING:
            if prev_toktype != tokenize.INDENT:
                # This is likely a docstring; double-check we're not inside an operator:
                if prev_toktype != tokenize.NEWLINE:
                    # Note regarding NEWLINE vs NL: The tokenize module
                    # differentiates between newlines that start a new statement
                    # and newlines inside of operators such as parens, brackes,
                    # and curly braces.  Newlines inside of operators are
                    # NEWLINE and newlines that start new code are NL.
                    # Catch whole-module docstrings:
                    if start_col > 0:
                        # Unlabelled indentation means we're inside an operator
                        out += token_string
                    # Note regarding the INDENT token: The tokenize module does
                    # not label indentation inside of an operator (parens,
                    # brackets, and curly braces) as actual indentation.
                    # For example:
                    # def foo():
                    #     "The spaces before this docstring are tokenize.INDENT"
                    #     test = [
                    #         "The spaces before this string do not get a token"
                    #     ]
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    return out


@click.command()
@click.argument("activities_directory", default=".")
def cli(activities_directory):

    # Create Paths
    activities_path = Path(activities_directory)

    # Build activities list
    activities = [a for a in activities_path.iterdir() if a.is_dir()]

    # Iterate through each activity
    for activity in activities:
        solved_path = activity / "Solved"
        unsolved_path = activity / "Unsolved"
        unsolved_notebooks = unsolved_path.glob("**/*.ipynb")
        solved_notebooks = solved_path.glob("**/*.ipynb")

        # Grab all of the unsolved code
        unsolved_code = set()
        for notebook_path in unsolved_notebooks:
            with open(notebook_path, "r") as notebook:
                nb = nbformat.read(notebook, as_version=4)
                for cell in nb.cells:
                    if cell.cell_type == "code" and cell.source:
                        cleaned = remove_comments_and_docstrings(cell.source)
                        if cleaned.strip():
                            unsolved_code.add(cleaned)

        # Grab all of the solved code
        solved_code = set()
        for notebook_path in solved_notebooks:
            with open(notebook_path, "r") as notebook:
                nb = nbformat.read(notebook, as_version=4)
                for cell in nb.cells:
                    if cell.cell_type == "code" and cell.source:
                        cleaned = remove_comments_and_docstrings(cell.source)
                        if cleaned.strip():
                            solved_code.add(cleaned)

        if not unsolved_code <= solved_code:
            print("Error, code cells in the unsolved activity doesn't match the solved")
            print(activity.resolve())
            print(unsolved_code - solved_code)


if __name__ == '__main__':
    cli()
