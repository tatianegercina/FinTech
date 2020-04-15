# -*- coding: utf-8 -*-
import click
import nbformat
from pathlib import Path

@click.command()
@click.argument("notebook_directory", default=".")
@click.option('--pattern', default="os.getenv", help='A code snippet/pattern to find in the source code.')
@click.option('--verbose', is_flag=True, help='enable to show the source code match.')
def cli(notebook_directory, pattern, verbose):

    # Create Paths
    notebook_path = Path(notebook_directory)
    # Find all notebooks
    # Exclude notebooks ending in `-checkpoints`
    notebooks = notebook_path.glob("**/*[!-checkpoints].ipynb")

    for notebook_path in notebooks:

        # Open each notebook and parse the code cells
        with open(notebook_path, "r") as notebook:
            nb = nbformat.read(notebook, as_version=nbformat.NO_CONVERT)
            for cell in nb.cells:
                if cell.cell_type == "code":
                    if pattern in cell.source:
                        print(f"Found pattern in: {notebook_path}")
                        if verbose:
                            print(cell.source)


if __name__ == "__main__":
    # Init the CLI
    cli()
