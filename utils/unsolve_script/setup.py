from setuptools import setup

setup(
    name='unsolve',
    version='0.1',
    py_modules=['unsolve'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        unsolve=unsolve:cli
    ''',
)
