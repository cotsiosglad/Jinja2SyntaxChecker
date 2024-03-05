from jinja2 import Environment, TemplateSyntaxError
import os
import sys


def find_j2_files(path):
    jinjaFiles = []

    # If path is a file, return it directly
    if os.path.isfile(path):
        return [path]

    # If path is a directory, find .j2 files recursively
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for filefound in files:
                if filefound.endswith('.j2'):
                    jinjaFiles.append(os.path.join(root, filefound))
        return jinjaFiles

    # If the path is neither a file nor a directory, return an empty list
    return []


if __name__ == "__main__":
    # Check if the user provided the file or directory path as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python Jinja2Linter.py /path/to/your/directory/or/file")
        sys.exit(1)
    path = sys.argv[1]
    if not os.path.exists(path):
        print("Error: Path does not exist.")
        sys.exit(1)

    j2_files = find_j2_files(path)

    if not j2_files:
        print("No .j2 files found.")
        sys.exit(0)

    print("Found .j2 files:")
    for file in j2_files:
        print(file)
    print("------------------------")

    for file in j2_files:
        with open(file, "r") as f:
            env = Environment()
            errors = []
            try:
                template_file = f.read()
                template = env.from_string(template_file)
                print(f"{file} succeeded with no errors")
            except TemplateSyntaxError as e:
                errors.append(f"Template syntax error on {file}, line {e.lineno}: {e}")

        # Print all errors after processing all files
        if errors:
            print("\n".join(errors))
