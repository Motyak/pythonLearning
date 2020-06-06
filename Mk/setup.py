import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Mk-Motyak", 
    version="0.0.1",
    author="Motyak",
    author_email="m0tyak_@live.fr",
    description="My package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Motyak/pythonLearning",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)