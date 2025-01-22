# read_pyfiles

`read_pyfiles` is a Python package for traversing directories, reading Python files, and outputting their contents to a single text file. It's configurable via a YAML file, making it easy to use in different scenarios.

## Features

- Traverse directories to locate `.py` files.
- Combine file contents into a single output file.
- Configure paths and output file name via a YAML configuration.

## Installation

### Local Installation

To install the package locally, clone the repository and use `pip`:

```bash
git clone https://github.com/GSU-Analytics/read_pyfiles.git
cd read_pyfiles
pip install .
```

### Remote Installation

If the repository is public and includes a `setup.py`, you can install it directly from GitHub:

```bash
pip install git+https://github.com/GSU-Analytics/read_pyfiles.git
```

This will fetch the latest version of the code from the `main` branch and install it.

## Usage

1. Create a configuration file named `read_config.yaml`:

```yaml
output_file: "output.txt"
paths_to_read:
  - "src"
  - "tests"
  - "main.py"
```

2. Run the tool using the command:

```bash
read_pyfiles
```

The output file will contain the combined contents of all `.py` files in the specified paths.

## Development

To set up a development environment:

1. Clone the repository:

```bash
git clone https://github.com/GSU-Analytics/read_pyfiles.git
cd read_pyfiles
```

2. Install the package in editable mode:

```bash
pip install -e .
```

3. Run the tests:

```bash
pytest -vv
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome contributions to improve this package. If you'd like to contribute, please:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a clear description of the changes.

## Contact

For any questions or issues, please open an issue in the [GitHub repository](https://github.com/GSU-Analytics/read_pyfiles).