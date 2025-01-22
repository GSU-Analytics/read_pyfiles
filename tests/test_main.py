import pytest
from read_pyfiles.main import main

@pytest.fixture
def mock_config_file(tmp_path, monkeypatch):
    """Create a mock configuration file and set its path."""
    config_file = tmp_path / "read_config.yaml"
    config_file.write_text("""
    output_file: "output_test.txt"
    paths_to_read:
      - "tests"
    """)

    # Monkeypatch the load_config function in the main module
    def mock_load_config():
        import yaml
        with open(config_file, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)

    monkeypatch.setattr("read_pyfiles.main.load_config", mock_load_config)

    return config_file

def test_main_with_mock_config(mock_config_file, tmp_path, monkeypatch, capsys):
    """Test the main function with a mock configuration."""
    # Monkeypatch sys.exit to avoid actual termination
    monkeypatch.setattr("sys.exit", lambda x: None)

    # Run the main function
    main()

    # Check the output
    captured = capsys.readouterr()
    assert "All Python file contents have been written to" in captured.out