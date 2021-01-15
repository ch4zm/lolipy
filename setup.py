#!/usr/bin/env python
import sys
from io import open

import setuptools

with open('requirements.txt') as f:
    requires = [x for x in f.read().splitlines() if not x.startswith("#") and not x.startswith("git")]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lolipy',
    version='1.0.4',
    author='Ch4zm of Hellmouth',
    author_email='ch4zm.of.hellmouth@gmail.com',
    url="https://github.com/ch4zm/lolipy/",
    description="Fork of leonardr/olipy, a library for artistic text generation",
    license='GPLv3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'lolipy.apollo = lolipy.example:apollo',
            'lolipy.board_games = lolipy.example:board_games',
            'lolipy.corrupt = lolipy.example:corrupt',
            'lolipy.dinosaurs = lolipy.example:dinosaurs',
            'lolipy.ebooks = lolipy.example:ebooks',
            'lolipy.gibberish = lolipy.example:gibberish',
            'lolipy.mashteroids = lolipy.example:mashteroids',
            'lolipy.sonnet = lolipy.example:sonnet',
            'lolipy.typewriter = lolipy.example:typewriter',
            'lolipy.words = lolipy.example:words',
        ]
    },
    package_data = {
        "lolipy": [
            "data/%s/*.json" % ("*/" * x)
            for x in range(10)
        ]
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Text Processing',
        'Topic :: Artistic Software',
    ],
)
