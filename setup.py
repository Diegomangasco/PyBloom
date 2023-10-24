# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:14:13 2023

@author: Diegomangasco
"""

from setuptools import setup, find_packages

setup(
    name="PyBloom",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["math", "mmh3", "bitarray"],
    author="Diegomangasco",
    author_email="diego.gasco99@gmail.com",
    description="Bloom Filter library",
    long_description="This library implements the Bloom Filter data structure",
    url="https://github.com/Diegomangasco/PyBloom",
    license="MIT",
)

