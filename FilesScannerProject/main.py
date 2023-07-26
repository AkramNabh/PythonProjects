import os

def find_large_files(starting_directory, min_size):
    for root, _, files in os.walk(starting_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size >= min_size:
                print(f"{file_path} - {file_size} bytes")

# Call the function with the main folder and the minimum size (in bytes)
find_large_files("/Repositories/GravaFun/Grava-Fun/GravaFun - excutables", 100 * 1024 * 1024)  # 100 MB in bytes
