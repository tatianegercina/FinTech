from setuptools import setup

setup(
    name='lint_jupyter',
    version='0.1',
    packages=["lintnb", "nberr"],
    install_requires=[
        'Click',
        'nbformat',
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'lintnb=lintnb.lintnb:cli',
            'nberr=nberr.nberr:cli',
            'nbspell=nbspell.nbspell:cli',
            'nbdiff=nbdiff.nbdiff:cli'
        ]
    },
)
