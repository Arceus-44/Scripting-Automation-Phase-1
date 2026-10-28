import os
import hashlib
import argparse

# Function to analyze a file
def analyze_file(file_path):
    if not os.path.isfile(file_path):
        print("[ERROR] File not found!")
        return

    try:
        # Get file information
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        # Calculate SHA-256 hash
        sha256 = hashlib.sha256()

        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha256.update(chunk)

        # Display results
        print("\n===== FILE ANALYZER =====")
        print("File Name:", file_name)
        print("File Size:", file_size, "bytes")
        print("SHA-256:", sha256.hexdigest())
        print("=========================")

    except OSError as error:
        print("[ERROR]", error)


# Main function
def main():
    parser = argparse.ArgumentParser(
        description="Python File Analyzer Tool"
    )

    parser.add_argument(
        "file",
        help="Path of the file to analyze"
    )

    args = parser.parse_args()
    analyze_file(args.file)


if __name__ == "__main__":
    main()
