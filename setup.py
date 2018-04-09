"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(

    name='Kontour',
    version='1.0.3',
    description='Finds common melodic phrases in **kern encoded music.',
    url='https://github.com/Jicol95/Kontour',
    author='Jack Nicol',
    author_email='jack.nicol95@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='development music musicology musicologists theory symbolic pattern detection',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['cycler==0.10.0',
                      'matplotlib==2.1.2',
                      'music21==4.1.0',
                      'numpy==1.14.0',
                      'Pillow==5.0.0',
                      'pygame==1.9.3',
                      'python-dateutil==2.6.1',
                      'pytz==2017.3',
                      'scipy==1.0.0',
                      'six==1.11.0',
                      'suffix-trees==0.2.4.4'],

    scripts=['main.py', 'Score.py', 'Analyse.py'],

    entry_points={
        'console_scripts': ['kontour = main:Main']},
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/Jicol95/Kontour/issues',
        'Say Thanks!': 'Jack.Nicol95@gmail.com',
        'Source': 'https://github.com/Jicol95/Kontour',
    },
)
