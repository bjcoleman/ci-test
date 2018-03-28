
from setuptools import setup, find_packages

setup(
    name="citest",
    packages=find_packages('src'),
    package_dir={'': 'src'},
)