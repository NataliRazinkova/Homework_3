import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

def copy_file(src, dst):
    shutil.copy2(src, dst)

def process_directory(src_dir, dst_dir):
    extensions = defaultdict(list)

    for root, _, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)
            extension = file.split('.')[-1]
            extensions[extension].append(src_path)

    os.makedirs(dst_dir, exist_ok=True)

    with ThreadPoolExecutor() as executor:
        futures = []
        for extension, file_paths in extensions.items():
            subdir = os.path.join(dst_dir, extension)
            os.makedirs(subdir, exist_ok=True)
            for file_path in file_paths:
                futures.append(executor.submit(copy_file, file_path, subdir))

        for future in futures:
            future.result()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a directory and sort files by extension.')
    parser.add_argument('source_dir', type=str, help='Path to the source directory')
    parser.add_argument('--target_dir', type=str, default='dist', help='Path to the target directory (default: dist)')
    args = parser.parse_args()

    process_directory(args.source_dir, args.target_dir)
