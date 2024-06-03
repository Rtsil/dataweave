from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dataweave",
    version="0.1.0",
    author="Tsilavo Tahina Rakotoarisoa",
    author_email="rtsilavotahina@gmail.com",
    description="A package for data manipulation, it has different functions e.g: encode/decode RLE, POLYGON manipulation, etc...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rtsil/dataweave",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy", "opencv-python"
    ],
    entry_points={
        'console_scripts': [
            'mycommand=mypackage.mymodule:main',
        ],
    },
)