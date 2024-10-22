StringExtractor
StringExtractor is a Python application designed to extract readable ASCII and Unicode strings from files or directories. This tool is particularly useful for data recovery, malware analysis, reverse engineering, or any scenario where you need to retrieve human-readable text from binary files.

Table of Contents
Features
Installation
Usage
Extract Strings from a File
Extract Strings from a Directory
Set Minimum String Length
Save Extracted Strings
Features
StringExtractor offers several powerful features to aid in extracting readable text from binary files or entire directories:

Extract ASCII and Unicode Strings

The tool can extract both ASCII (standard text) and Unicode (UTF-16) strings from binary files, making it versatile for analyzing files that may contain hidden or embedded text.
Extract Strings from Individual Files

Users can specify a file path to extract readable text. This is useful for examining binary files such as executables, compiled programs, or other binary formats.
Batch Extraction from Directories

Recursively extract strings from all files within a directory. This feature enables the bulk analysis of multiple files, making it particularly helpful for malware research or file system investigations.
Configurable Minimum String Length

Users can set the minimum string length for extraction. This allows for filtering out short, irrelevant strings, focusing on meaningful content.
Save Extracted Strings to a File

Save extracted strings to an external file for further analysis or documentation. This feature allows easy exporting and archiving of results for later use.
User-Friendly Console Interface

A menu-driven console interface ensures easy navigation and use, even for users unfamiliar with command-line arguments or Python code.
These features make StringExtractor an invaluable tool for tasks such as reverse engineering, digital forensics, malware analysis, and general file inspection.

Installation
To install StringExtractor, ensure that Python 3.6 or higher is installed on your system. Then, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/b0yx/StringExtractor.git
Navigate to the project folder:

bash
Copy code
cd StringExtractor
Usage
Run the program by executing the following command:

bash
Copy code
python StringExtractor.py
Upon running, you'll be presented with a menu of options:

bash
Copy code
1. Extract Strings from File
2. Extract Strings from Directory
3. Set Minimum String Length (Current: 3)
4. Save Extracted Strings to File
5. Exit
Extract Strings from a File
Choose option 1.
Input the full file path (e.g., C:\path\to\your\file.bin).
The tool will display the extracted ASCII and Unicode strings from the file.
Extract Strings from a Directory
Choose option 2.
Provide the directory path (e.g., C:\path\to\your\directory).
The program will extract strings from all files within the directory and display the results.
Set Minimum String Length
Choose option 3.
Enter a new minimum string length (the default is 3). This allows you to filter the strings based on their length.
Save Extracted Strings
Choose option 4.
Specify whether you want to extract strings from a file or directory.
Provide the file or directory path.
Enter the output file name where the extracted strings will be saved.
This StringExtractor tool is straightforward yet highly effective for binary analysis. Whether you're performing malware analysis or simply exploring file contents, this tool is designed to streamline the process.

Contributing
We welcome contributions! If you'd like to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add a new feature").
Push to the branch (git push origin feature-branch).
Open a pull request describing your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.
