import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hltv-api-jclge",
    version="0.1.0",
    author="JCLGE",
    license="GNU 3",
    author_email="julien.calenge@epitech.eu",
    description="Unofficial Python API for the Counter-Strike home: HLTV.ORG",
    url="https://github.com/jclge/HLTV.ORG-API",
    packages=setuptools.find_packages(),
    install_requires=[
        'selenium',
        'pyvirtualdisplay',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
