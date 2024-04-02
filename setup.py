"""Installation script for the 'ase' python package."""

from setuptools import setup, find_packages

# Minimum dependencies required prior to installation
INSTALL_REQUIRES = [
    "torch==1.8.1",
    "numpy==1.21.1",
    "termcolor==1.1.0",
    "rl-games==1.1.4",    # 
    "tensorboard==1.15.0 ", #    
]

# Installation operation
setup(
    name="ase",
    version="1.0.0",
    author="Jason Peng",
    packages=find_packages(),
    author_email="",
    description="",
    install_requires=INSTALL_REQUIRES,
)


