import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iFCon",
    version="2.0",
    author="Borohydride",
    author_email="3171132517@qq.com",
    description="A package for calculating the interfacial energy of a system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iFCon/iFCon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['iFCon.py'],
)