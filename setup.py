from setuptools import setup, find_packages

setup(
    name="read_pyfiles",
    version="0.1",
    description="A package to traverse directories, read Python files, and output their contents.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="ikerson@gsu.edu",
    url="https://github.com/GSU-Analytics/read_pyfiles",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "PyYAML>=6.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "read_pyfiles=read_pyfiles.main:main",
        ],
    },
)
