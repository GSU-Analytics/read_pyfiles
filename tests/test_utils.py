import os
import pytest
from read_pyfiles.utils import read_file, traverse_and_collect, load_config

@pytest.fixture
def sample_files(tmp_path):
    """Fixture to create sample Python files and directories."""
    folder = tmp_path / "sample"
    folder.mkdir()

    file1 = folder / "file1.py"
    file1.write_text("print('Hello from file1')")

    file2 = folder / "file2.py"
    file2.write_text("print('Hello from file2')")

    subfolder = folder / "subfolder"
    subfolder.mkdir()

    file3 = subfolder / "file3.py"
    file3.write_text("print('Hello from file3')")

    return folder

def test_read_file(sample_files):
    file1 = sample_files / "file1.py"
    content = read_file(file1)
    assert content == "print('Hello from file1')"

    non_existent_file = sample_files / "nonexistent.py"
    content = read_file(non_existent_file)
    assert content is None

def test_traverse_and_collect(sample_files, tmp_path):
    output_file = tmp_path / "output.txt"
    traverse_and_collect([sample_files], output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        output_content = f.read()

    assert "print('Hello from file1')" in output_content
    assert "print('Hello from file2')" in output_content
    assert "print('Hello from file3')" in output_content

def test_load_config(tmp_path):
    config_file = tmp_path / "read_config.yaml"
    config_file.write_text("""
    output_file: "output.txt"
    paths_to_read:
      - "src"
      - "tests"
    """)

    config = load_config(config_file)
    assert config["output_file"] == "output.txt"
    assert config["paths_to_read"] == ["src", "tests"]

def test_load_config_invalid_file():
    config = load_config("nonexistent.yaml")
    assert config == {}
