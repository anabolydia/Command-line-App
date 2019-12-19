from setuptools import setup

setup(
    name='newsApp',
    version='0.1',
    py_modules=['newsApp'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        newsApp=newsApp:main
    ''',
)