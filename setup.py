from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="life",
    version="0.0.1",
    author="Azmi SAHIN",
    author_email="azmisahin@outlook.com",
    description="Modeling the life cycle in the evolutionary process",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: CC0 1.0 Universal",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/azmisahin-ai/life",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        #
    ],
)
