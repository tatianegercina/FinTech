# FinTech Tools Setup

## Anaconda

All of the FinTech assignments are developed using a Conda environment with the Anaconda bundle installed. 

Download and install the latest from Anaconda for Python 3.7 or greater
https://www.anaconda.com/distribution/

Create a new Conda environment using Python 3.7 and the anaconda package
```shell
conda create -n dev python=3.7 anaconda
```

Install the dev environment kernel for Jupyter Lab
```shell
python -m ipykernel install --user --name dev
```

Install the node environment
```shell
conda install -c conda-forge nodejs
```

## Visual Studio Code

We use a handful of extensions and configuration to help us stay consistent with code standards and markdown linting. 

Install Extensions
```shell
code --install-extension ms-python.python
code --install-extension DavidAnson.vscode-markdownlint
code --install-extension streetsidesoftware.code-spell-checker
code --install-extension EditorConfig.EditorConfig
```

Enabling editorconfig will pick up the whitespace settings while working in the repo. 

Recommended vscode settings (these can be added to the settings.json file or mannually through the settings interface)
```
"editor.renderWhitespace": "all",
"files.trimTrailingWhitespace": true,
"files.insertFinalNewline": true,
"files.trimFinalNewlines": true,
"editor.rulers": [
    80,
    120
],
"[python]": {
  "editor.detectIndentation": false,
  "editor.tabSize": 4,
  "editor.defaultFormatter": "ms-python.python"
},
"python.linting.enabled": true,
"python.linting.pylintEnabled": true,
"python.formatting.provider": "black"
```
