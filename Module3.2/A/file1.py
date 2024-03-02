import os

def copy_txt_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Traverse through all subdirectories and files in the source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Check if the file is a text file
            if file.endswith('.txt'):
                # Construct the source and destination file paths
                source_file = os.path.join(root, file)
                destination_file = os.path.join(destination_dir, file)

                # Open the source file for reading and the destination file for writing
                with open(source_file, 'rb') as src_file, open(destination_file, 'wb') as dest_file:
                    # Read the content of the source file and write it to the destination file
                    dest_file.write(src_file.read())
                print(f"Copied '{file}' to '{destination_dir}'")

if __name__ == "__main__":
    # Specify the source directory where text files are located
    source_directory = "../Module2/extracted"

    # Specify the destination directory where text files will be copied
    destination_directory = "Combined_txt"

    # Copy text files from source directory to destination directory
    copy_txt_files(source_directory, destination_directory)
