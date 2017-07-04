from setuptools import setup, find_packages
# To use consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Fetch the long description form the separate README.rst file
with open(path.join(here, 'README.rst'), encoding = 'utf-8') as f:
    long_description = f.read()

version = {}
with open(path.join(here, 'VERSION'), encoding = 'utf-8') as version_file:
    version = version_file.read().strip()
    
setup(
    name = 'UnsplashUbuntu',
    version = version,

    description = 'Wallpaper Changer with multi-monitor support',
    long_description = long_description,

    url = 'https://github.com/PseudoAj/UnsplashUbuntu',

    author = 'PseudoAj',
    author_email = '',

    license = 'GPL v3',

    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: End Users/Desktop',

        'Topic :: Desktop Environment :: Gnome',
        
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],

    keywords = 'wallpaper changer desktop beautiful',

    packages = find_packages(exclude=['contrib', 'docs', 'tests*'])    
)
