import sys
from read_pyfiles.utils import traverse_and_collect, load_config

def main():
    """Main function to execute the script logic."""
    config = load_config()

    paths_to_traverse = config.get("paths_to_read", [])
    output_file = config.get("output_file", "output.txt")

    if not paths_to_traverse:
        print("No paths to traverse specified in the configuration file.", file=sys.stderr)
        sys.exit(1)

    traverse_and_collect(paths_to_traverse, output_file)

if __name__ == "__main__":
    main()