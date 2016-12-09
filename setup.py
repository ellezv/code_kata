"""The setup for my katas modules."""

from setuptools import setup

setup(
    name="code katas",
    description="An implmentation of various katas from codewars.com",
    version=0.1,
    author="Maelle Vance",
    author_email="maellevance@gmail.com",
    license="MIT",
    py_modules=['sum_positives'],
    package_dir={'': 'src'},
    install_requires=['tox'],
    extras_require={
        "test": ["pytest", "pytest-watch", "pytest-cov"]
    },
)
