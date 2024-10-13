import os
import re

# Global variable for minimum length
MinimumLengthSize = 3  # Default value

def Menu():
    print("---------------------------------------------------------------------")
    print("""
    1. Extract Strings from File
    2. Extract Strings from Directory
    3. Set Minimum String Length (Current: {})
    4. Save Extracted Strings to File
    5. Exit
    """.format(MinimumLengthSize))
    print("---------------------------------------------------------------------")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        FileExtractor()
    elif choice == "2":
        DirectoryExtractor()
    elif choice == "3":
        set_minimum_length()
    elif choice == "4":
        SaveStringsToExternalFile()
    elif choice == "5":
        exit(0)
    else:
        print("Invalid Choice. Please Try Again.")

def extract_ascii_strings(data, min_length=3):
    pattern = rb'[\x20-\x7E]{' + str(min_length).encode() + b',}'
    return re.findall(pattern, data)

def extract_unicode_strings(data, min_length=3):
    pattern = rb'(?:[\x20-\x7E]\x00){' + str(min_length).encode() + b',}'
    matches = re.findall(pattern, data)
    return [m.decode('utf-16le') for m in matches]

def extract_strings(file_path):
    try:
        with open(file_path, "rb") as f:
            binary_data = f.read()
            ascii_strings = extract_ascii_strings(binary_data, MinimumLengthSize)
            unicode_strings = extract_unicode_strings(binary_data, MinimumLengthSize)
            return ascii_strings, unicode_strings
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return [], []

def FileExtractor():
    file_path = input("Enter File Path: ")
    ascii_strings, unicode_strings = extract_strings(file_path)

    print("Extracted ASCII Strings:")
    for s in ascii_strings:
        print(s.decode('ascii', errors='ignore'))

    print("\nExtracted Unicode Strings:")
    for s in unicode_strings:
        print(s)

def set_minimum_length():
    global MinimumLengthSize
    size_input = input("What minimum length size would you like to set? (default is 4): press Enter to set the default .... ")

    if size_input == "":
        MinimumLengthSize = 4
    else:
        try:
            MinimumLengthSize = int(size_input)
        except ValueError:
            print("Invalid input. Setting minimum length to default (4).")
            MinimumLengthSize = 4

def DirectoryExtractor():
    directory_path = input("Enter the path of Directory ....")
    
    print("Extracting strings from files in directory:")
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            ascii_strings, unicode_strings = extract_strings(file_path)

            print(f"\nExtracted ASCII Strings from {file_name}:")
            for s in ascii_strings:
                print(s.decode('ascii', errors='ignore'))

            print(f"\nExtracted Unicode Strings from {file_name}:")
            for s in unicode_strings:
                print(s)

def SaveStringsToExternalFile():
    extracted_strings = []
    
    # Prompt user for extraction choice
    choice = input("""Choose an extraction method:
    1- Directory Extract
    2- File Extract
    Enter your choice: """)
    
    # Handle directory extraction
    if choice == '1':
        current_directory = input("Enter the directory to extract strings from: ")
        if not os.path.isdir(current_directory):
            print("Invalid directory. Please try again.")
            return
        
        for file_name in os.listdir(current_directory):
            file_path = os.path.join(current_directory, file_name)
            if os.path.isfile(file_path):
                ascii_strings, _ = extract_strings(file_path)
                extracted_strings.extend([s.decode('ascii', errors='ignore') for s in ascii_strings])
    
    # Handle single file extraction
    elif choice == '2':
        file_path = input("Enter the file path to extract strings from: ")
        if not os.path.isfile(file_path):
            print("File not found. Please check the file path.")
            return
        
        ascii_strings, _ = extract_strings(file_path)
        extracted_strings.extend([s.decode('ascii', errors='ignore') for s in ascii_strings])
    
    # Invalid choice handling
    else:
        print("Please choose a valid option.")
        return

    # Prompt for output file name
    output_file_name = input("Enter output file name (e.g., output.txt): ")

    # Save extracted strings to the specified output file
    try:
        with open(output_file_name, 'w') as f:
            for string in extracted_strings:
                f.write(string + '\n')  # Write each string on a new line
        print(f"Extracted strings saved to {output_file_name}")
    except Exception as e:
        print(f"Error saving strings to file: {e}")

# Main program loop
while True:
    Menu()
