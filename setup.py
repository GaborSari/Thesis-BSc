import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Object Tracker",
    version="1.0.0",
    author="Gabor Sari",
    author_email="Sari.Gabor@stud.u-szeged.hu,nagya@inf.u-szeged.hu",
    description="SZTE Bsc Thesis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)