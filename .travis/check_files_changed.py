# -*- coding: utf-8 -*-
"""Check Changed Files.

This module will run linters on any files that changed in the commit.

"""
import shlex
import subprocess
from pathlib import Path

# Store changed files for each file type
markdown_files_changed = []
python_files_changed = []
javascript_files_changed = []

# Main Git CMD to find the changes changed
git_diff = shlex.split("git diff --diff-filter=d --name-only master")

# Running Git CMD to get the files changed
# Removing formatting on the end of the string with rstrip
# Spliting string to list with split based on \n
all_files_changed = (
    subprocess.check_output(git_diff, encoding="utf-8").rstrip().split("\n")
)

# Sorting the list of all files changed into list based on extension
for file_changed in all_files_changed:

    if file_changed.endswith(".md"):
        markdown_files_changed.append(file_changed)
    if file_changed.endswith(".py"):
        python_files_changed.append(file_changed)
    if file_changed.endswith(".js"):
        javascript_files_changed.append(file_changed)

# Markdown link reporter path
markdown_link_path = Path("./node_modules/.bin/md-report")

# Making sure that markdown link reporter exists
if markdown_link_path.exists():

    # Running markdown link reporter
    run_md_report = subprocess.run(
        shlex.split(
            f"{markdown_link_path}"), stdout=subprocess.PIPE
    )
    print(f"stdout: {run_md_report.stdout.decode('utf-8')}")
    print(f"returncode: {run_md_report.returncode}")
else:
    print(
        "markdown-link-reporter is not found. "
        "Might need to do a npm install or yarn install"
    )

# Cspell path
cspell_path = Path("./node_modules/.bin/cspell")

# Making sure that cspell path exists
if cspell_path.exists():

    for file_changed in all_files_changed:
        # Running cspell
        test = subprocess.run(
            shlex.split(
                f"{cspell_path} -u {file_changed}"), stdout=subprocess.PIPE
        )
        print(f"stdout: {test.stdout.decode('utf-8')}")
        print(f"returncode: {test.returncode}")
else:
    print("cspell is not found. Might need to do a npm install or yarn install")

# Eslint path
eslint_path = Path("./node_modules/.bin/eslint")

# Making sure that eslint path exists
if eslint_path.exists():

    for file_changed in javascript_files_changed:
        # Running eslint
        test = subprocess.run(
            shlex.split(f"{eslint_path} -c .eslintrc.json {file_changed}"),
            stdout=subprocess.PIPE,
        )
        print(f"stdout: {test.stdout.decode('utf-8')}")
        print(f"returncode: {test.returncode}")
else:
    print("eslint is not found. Might need to do a npm install or yarn install")

for file_changed in python_files_changed:
    # Running pycodestyle
    test = subprocess.run(
        shlex.split(
            f"pycodestyle --show-source {file_changed}"), stdout=subprocess.PIPE
    )
    print(f"stdout: {test.stdout.decode('utf-8')}")
    print(f"returncode: {test.returncode}")
