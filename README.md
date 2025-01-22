# read_pyfiles

`read_pyfiles` is a Python package for traversing directories, reading Python files, and outputting their contents to a single text file. It's configurable via a YAML file, making it easy to use in different scenarios.

## Features

- Traverse directories to locate `.py` files.
- Combine file contents into a single output file.
- Configure paths and output file name via a YAML configuration.

## Installation

You can install the package locally:

```bash
pip install .
```

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
git clone https://github.com/yourusername/read_pyfiles.git
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
```

---

### Additional Notes:
1. **`setup.py`**:
   - Replace `"your.email@example.com"` and `"https://github.com/yourusername/read_pyfiles"` with your email and GitHub URL.
   - If you're publishing on PyPI, ensure your GitHub repository is public and has a proper license.

2. **`README.md`**:
   - Adjust the description to match your use case.
   - Include additional sections as needed (e.g., Examples, FAQs).