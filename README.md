# StringExtractor

StringExtractor is a Python application designed to extract readable ASCII and Unicode strings from files or directories. This tool is particularly useful for data recovery, malware analysis, reverse engineering, or any scenario where you need to retrieve human-readable text from binary files.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Extract Strings from a File](#extract-strings-from-a-file)
  - [Extract Strings from a Directory](#extract-strings-from-a-directory)
  - [Set Minimum String Length](#set-minimum-string-length)
  - [Save Extracted Strings](#save-extracted-strings)
- [Contributing](#contributing)
- [License](#license)

## Features

StringExtractor offers several powerful features to aid in extracting readable text from binary files or entire directories:

- **Extract ASCII and Unicode Strings**:  
  The tool can extract both ASCII (standard text) and Unicode (UTF-16) strings from binary files, making it versatile for analyzing files that may contain hidden or embedded text.

- **Extract Strings from Individual Files**:  
  Users can specify a file path to extract readable text. This is useful for examining binary files such as executables, compiled programs, or other binary formats.

- **Batch Extraction from Directories**:  
  Recursively extract strings from all files within a directory. This feature enables the bulk analysis of multiple files, making it particularly helpful for malware research or file system investigations.

- **Configurable Minimum String Length**:  
  Users can set the minimum string length for extraction, allowing for filtering out short, irrelevant strings and focusing on meaningful content.

- **Save Extracted Strings to a File**:  
  Save extracted strings to an external file for further analysis or documentation. This feature allows easy exporting and archiving of results for later use.

- **User-Friendly Console Interface**:  
  A menu-driven console interface ensures easy navigation and use, even for users unfamiliar with command-line arguments or Python code.

These features make StringExtractor an invaluable tool for tasks such as reverse engineering, digital forensics, malware analysis, and general file inspection.

## Installation

To install StringExtractor, ensure that Python 3.6 or higher is installed on your system. Then, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/b0yx/StringExtractor.git
   ```

2. **Navigate to the project folder**:

   ```bash
   cd StringExtractor
   ```

## Usage

Run the program by executing the following command:

```bash
python StringExtractor.py
```

Upon running, you'll be presented with a menu of options:

```bash
1. Extract Strings from File
2. Extract Strings from Directory
3. Set Minimum String Length (Current: 3)
4. Save Extracted Strings to File
5. Exit
```

### Extract Strings from a File

1. Choose option 1.
2. Input the full file path (e.g., `C:\path\to\your\file.bin`).
3. The tool will display the extracted ASCII and Unicode strings from the file.

### Extract Strings from a Directory

1. Choose option 2.
2. Provide the directory path (e.g., `C:\path\to\your\directory`).
3. The program will extract strings from all files within the directory and display the results.

### Set Minimum String Length

1. Choose option 3.
2. Enter a new minimum string length (the default is 3). This allows you to filter the strings based on their length.

### Save Extracted Strings

1. Choose option 4.
2. Specify whether you want to extract strings from a file or directory.
3. Provide the file or directory path.
4. Enter the output file name where the extracted strings will be saved.

StringExtractor is straightforward yet highly effective for binary analysis. Whether you're performing malware analysis or simply exploring file contents, this tool is designed to streamline the process.

## Contributing

We welcome contributions! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-branch
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add a new feature"
   ```

4. Push to the branch:

   ```bash
   git push origin feature-branch
   ```

5. Open a pull request describing your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
