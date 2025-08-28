import os

def modify_content(content):
    """
    Modify the content of the file.
    This example converts text to uppercase and adds line numbers.
    You can customize this function for different modifications.
    """
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        # Add line number and convert to uppercase
        modified_line = f"{i}: {line.upper()}"
        modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

def main():
    print("File Read & Write Program")
    print("=========================")
    
    while True:
        # Get input filename from user
        input_filename = input("\nEnter the name of the file to read (or 'quit' to exit): ").strip()
        
        if input_filename.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Check if file exists
        if not os.path.exists(input_filename):
            print(f"Error: The file '{input_filename}' does not exist.")
            continue
        
        # Check if it's actually a file
        if not os.path.isfile(input_filename):
            print(f"Error: '{input_filename}' is not a file.")
            continue
        
        try:
            # Try to read the file
            with open(input_filename, 'r', encoding='utf-8') as file:
                content = file.read()
            
            print(f"Successfully read '{input_filename}'")
            
            # Modify the content
            modified_content = modify_content(content)
            
            # Create output filename
            name, ext = os.path.splitext(input_filename)
            output_filename = f"{name}_modified{ext}"
            
            # Check if output file already exists
            if os.path.exists(output_filename):
                overwrite = input(f"'{output_filename}' already exists. Overwrite? (y/n): ").lower()
                if overwrite != 'y':
                    print("Operation cancelled.")
                    continue
            
            # Write modified content to new file
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            
            print(f"Successfully created modified file: '{output_filename}'")
            
            # Ask if user wants to see a preview
            preview = input("Would you like to see a preview of the modified file? (y/n): ").lower()
            if preview == 'y':
                print("\nPreview of modified content (first 5 lines):")
                print("-" * 40)
                lines = modified_content.split('\n')[:5]
                for line in lines:
                    print(line)
                if len(modified_content.split('\n')) > 5:
                    print("... (truncated)")
            
        except PermissionError:
            print(f"Error: Permission denied. Cannot read '{input_filename}'.")
        except UnicodeDecodeError:
            print(f"Error: Cannot decode '{input_filename}'. It might be a binary file.")
        except IsADirectoryError:
            print(f"Error: '{input_filename}' is a directory, not a file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()