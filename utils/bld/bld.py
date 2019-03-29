
import sys
import click
from pathlib import Path
from shutil import copytree, rmtree


# @click.option('--name', prompt='01-Ins_First_Activity', help='The Activity Folder Name.')
@click.command()
@click.argument('name')
def cli(name):

    # Create Paths
    root = Path(name)
    solved = root / "Solved"
    unsolved = root / "Unsolved"
    images = root / "Images"
    resources = root / "Resources"
    readme = root / "README.md"
    solved_keep = solved / ".gitkeep"
    unsolved_keep = unsolved / ".gitkeep"
    images_keep = images / ".gitkeep"
    resources_keep = resources / ".gitkeep"

    if (root.exists() or solved.exists() or unsolved.exists() or
        images.exists() or resources.exists() or readme.exists()):
        print("File or Folder Exists!")
        sys.exit(-3)

    root.mkdir()
    solved.mkdir()
    unsolved.mkdir()
    images.mkdir()
    resources.mkdir()
    readme.touch()
    solved_keep.touch()
    unsolved_keep.touch()
    images_keep.touch()
    resources_keep.touch()



if __name__ == '__main__':
    cli()
