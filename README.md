# StringExtractor

StringExtractor is a Python application designed to extract readable ASCII and Unicode strings from files or directories. This tool is particularly useful for data recovery, malware analysis, or any situation where you need to retrieve text data from binary files.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features
- Extracts ASCII and Unicode strings from individual files or entire directories.
- Allows users to set a minimum string length for extraction.
- Saves extracted strings to an external file for easy access.

## Installation
To install StringExtractor, ensure you have Python installed on your system (version 3.6 or higher). Then, clone the repository and navigate to the project folder:

## bash:
git clone https://github.com/<username>/StringExtractor.git

## Usage
- Run the Program:
  python StringExtractor.py
- Select an Option:
  1. Extract Strings from File
  2. Extract Strings from Directory
  3. Set Minimum String Length (Current: 3)
  4. Save Extracted Strings to File
  5. Exit
  
- Enter the number corresponding to your choice and press Enter.

- Extracting Strings:
    * Extract From a File:
        Choose option 1.
        Input the full file path with name of the file (e.g., C:\path\to\your\file.bin).
        The extracted ASCII and Unicode strings will be displayed.

    * From a Directory:
        Choose option 2.
        Provide the directory path (e.g., C:\path\to\your\directory).
        The program will extract and display strings from each file in the directory.
  Set Minimum String Length:

- Choose option 3.
    Enter a new minimum length for string extraction or press Enter to keep the default (currently set to 3).
    Save Extracted Strings:

- Choose option 4.
    Select whether to extract from a directory or a single file.
    Provide the necessary paths.
    Specify the output file name where the extracted strings will be saved.
        
        
