import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pet-project-api-pkg-bloomsamyk",
    version="0.0.1",
    author="Bloomsamyk",
    author_email="bloomsamyk@gmail.com",
    description="Pet project API package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bloomsamyk/pet-project-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)