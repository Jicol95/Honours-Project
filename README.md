[![PyPI version](https://badge.fury.io/py/Kontour.svg)](https://badge.fury.io/py/Kontour)
# Kontour
Finds common melodic phrases in kern encoded music.
# Installation
To install run

`python3 setup.py install`


You can also grab it directly from pip

`pip3 install Kontour`

# Usage

main [-h] -f FILENAME [-s SEQUENCE] [-ms] [-pdf]

Finds common melodic phrases in kern encoded music.

optional arguments:

  -h, --help            show this help message and exit

  -f FILENAME, --filename FILENAME Takes one argument, the name of the file


Export Options:

  Allows the user to specify how to view the results.

  -ms, --musescore      Indicates if the user want to view the results in MuseScore.

  -pdf, --lillypond     Indicates that the user wants to export the results to pdf using LillyPond.


Search Options:

  Different search options.

  -s SEQUENCE, --sequence SEQUENCE
                        User can enter a sequnce to search for using the alphabet {+,-,0}.


# License
Apache License 2.0

See LICENSE.md for details
