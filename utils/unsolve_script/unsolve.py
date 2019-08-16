
import sys
import click
from pathlib import Path
from shutil import copytree, rmtree


@click.command()
@click.option('--ipath', '-i', default=".", help="Activities Input Path")
@click.option('--opath', '-o', default=".", help="Unsolved Output Path")
@click.option('--force', '-f', is_flag=True, help="Force Overwriting Unsolved")
def cli(ipath, opath, force):

    # Create Paths
    activities_path = Path(ipath)
    unsolved_path = Path(opath)

    # Add folder names to the path if needed
    if activities_path.name != "Activities":
        activities_path = activities_path / "Activities"
    if unsolved_path.name != "Unsolved":
        unsolved_path = unsolved_path / "Unsolved"

    # Error Checking
    if not activities_path.exists():
        print("ERROR: Activities folder not in path")
        sys.exit(3)

    if unsolved_path.exists() and not force:
        print(f'ERROR: Unsolved already exists ({unsolved_path})')
        print('To overwrite the folder, use option `--force`')
        sys.exit(3)

    # Make Unsolved Folder
    rmtree(unsolved_path, ignore_errors=True)
    unsolved_path.mkdir(exist_ok=True)

    # Build activities list
    activities = [a for a in activities_path.iterdir() if a.is_dir()]

    # Copy activities folder from ipath to opath
    for activity in activities:
        copytree(activity, unsolved_path / activity.name)

    # Delete Solved folders
    for entry in unsolved_path.iterdir():
        if Path(entry, "Solved").exists():
            rmtree(entry / "Solved", ignore_errors=True)


if __name__ == '__main__':
    cli()
