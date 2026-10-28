  Python File Analyzer

1. Tool Name

Python File Analyzer

2. Objective

This Python tool analyzes a file and displays its name, size, and SHA-256 hash.

3. Features

• Accepts a file path as input

• Checks whether the file exists

• Displays file name and size

• Calculates the SHA-256 hash

• Handles basic file errors

• Supports the --help option

4. Requirements

• Python 3

• Linux or Kali Linux

• Permission to read the selected file

5. How to Run

python3 tool.py test.txt

Display help:

python3 tool.py --help

Test a missing file:

python3 tool.py missing.txt

6. Example Usage

Run the tool with a filename, such as test.txt.

7. Example Output

The tool displays the file name, file size in bytes, and calculated SHA-256 hash.

8. Challenges Faced

• Understanding file paths

• Reading files in binary mode

• Calculating SHA-256 hashes

• Handling missing files

9. Future Improvements

• Detect file types

• Save analysis results to a report

• Compare hashes against known trusted values

• Improve error reporting

10. Conclusion

This project helped me learn Python functions, file handling, command-line arguments, error handling, and cryptographic hashing.
