from setuptools import setup

setup(
    name='lint_jupyter',
    version='0.1',
    packages=["lintnb", "nberr", 'nbspell', 'nbdiff', 'lintpandas', 'nbfinder'],
    install_requires=[
        'Click',
        'nbformat',
        'colorama',
        'pandas_vet'
    ],
    entry_points={
        'console_scripts': [
            'lintnb=lintnb.lintnb:cli',
            'nberr=nberr.nberr:cli',
            'nbspell=nbspell.nbspell:cli',
            'lintpandas=lintpandas.lintpandas:cli',
            'nbdiff=nbdiff.nbdiff:cli',
            'nbfinder=nbfinder.nbfinder:cli'
        ]
    },
)
