from setuptools import setup, find_packages

setup(
    name="kreamharvester",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "seleniumbase",
        "parameterized",
        "pytest"
    ],
) 