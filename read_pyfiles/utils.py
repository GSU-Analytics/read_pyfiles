import os
import sys
import yaml

def read_file(file_path):
    """Read the contents of a file and return it."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        return None

def traverse_and_collect(paths, output_file):
    """
    Traverse the folders and Python files in the given paths, read their contents,
    and output everything to a single text file.

    Args:
        paths (list): List of folder and/or file paths.
        output_file (str): Path to the output text file.
    """
    collected_contents = []

    for path in paths:
        if os.path.isfile(path):
            if path.endswith('.py'):
                content = read_file(path)
                if content:
                    collected_contents.append(f"\n# File: {path}\n\n{content}")
        elif os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        content = read_file(file_path)
                        if content:
                            collected_contents.append(f"\n# File: {file_path}\n\n{content}")
        else:
            print(f"Invalid path: {path}", file=sys.stderr)

    try:
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write("\n\n".join(collected_contents))
        print(f"All Python file contents have been written to {output_file}")
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}", file=sys.stderr)

def load_config(config_file="config/read_config.yaml"):
    """
    Load configuration from a YAML file.
    Args:
        config_file (str): Path to the YAML configuration file.
    Returns:
        dict: Configuration data.
    """
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error loading configuration file {config_file}: {e}", file=sys.stderr)
        return {}
