
from setuptools import setup, find_packages

setup(
    name="ci-test",
    packages=find_packages('src'),
    package_dir={'': 'src'},
)