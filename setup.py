# -*- coding: utf-8 -*-

# Third
from __init__ import __version__
from setuptools import find_packages, setup


def long_description():
    with open('README.md', encoding='utf8') as f:
        return f.read()


__description__ = 'Civilizations api in vibora'

__author__ = 'Lucas Simon'
__author_email__ = 'lucassrod@gmail.com'

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='civilizations',
    version=__version__,

    author=__author__,
    author_email=__author_email__,

    license='MIT',
    description=__description__,
    long_description=long_description(),
    url='https://github.com:lucassimon/api.git',
    keywords='API, MongoDB',

    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)
