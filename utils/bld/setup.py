from setuptools import setup

setup(
    name='bld',
    version='0.1',
    py_modules=['bld'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        bld=bld:cli
    ''',
)
