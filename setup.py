# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='poets',
    version='0.0.1',
    description='Prints random poet name',
    long_description=readme,
    author='Egor Zhuk',
    url='https://github.com/EgorZhuk/poets',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    keywords='names poet poets name',
    entry_points={
        'console_scripts': [
            'poets=poets.__main__:main',
        ],
    }
)
