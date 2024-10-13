# StringExtractor

StringExtractor is a Python application designed to extract readable ASCII and Unicode strings from files or directories. This tool is particularly useful for data recovery, malware analysis, or any situation where you need to retrieve text data from binary files.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features
The StringExtractor program offers several key features that make it useful for extracting human-readable strings from binary files or entire directories. Here are its main features:
  1. Extract ASCII and Unicode Strings:
     The program can extract both ASCII (standard text) and Unicode (UTF-16) strings from binary files, making it versatile for analyzing files that may       contain hidden or embedded text.
  2. Extract Strings from Individual Files:
     Users can input the path of a specific file to extract readable text, making it useful for examining binary data, such as executables, compiled           programs, or other binary formats.
  3. Batch Extraction from a Directory:
     The program can recursively extract strings from all files in a directory, enabling the analysis of multiple files at once, which is particularly         helpful for bulk analysis or malware research.
  4. Configurable Minimum String Length:
     Users can set the minimum string length for extraction, filtering out shorter sequences and focusing on more meaningful content. This feature             enhances control over the type of output generated.
  5. Save Extracted Strings to a File:
      Users can save the extracted strings to an external text file for further analysis or documentation, allowing for easy export and archiving of     
      results.
  6. User-Friendly Console Interface:
      The program has an intuitive, menu-driven console interface, making it easy to navigate and use without needing to modify code or handle complex           command-line arguments.
     
  These features make the program a simple yet powerful tool for analyzing binary files or directories for hidden or readable text, useful in tasks like reverse engineering, digital forensics, or general file inspection.

## Installation
To install StringExtractor, ensure you have Python installed on your system (version 3.6 or higher). Then, clone the repository and navigate to the project folder:

## bash:
git clone https://github.com/b0yx/StringExtractor.git

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
        
        
