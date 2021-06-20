from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Avigilon Control Center API for Python'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
        name="accapi", 
        version=VERSION,
        author="Jakub Bartkowiak",
        author_email="gralinpl@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=[],      
        keywords=['python', 'acc', 'avigilon'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
)