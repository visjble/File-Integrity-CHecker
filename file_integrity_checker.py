import os, time, sys
import hashlib
import psutil

# Initialize the process variable outside the function
process = psutil.Process(os.getpid())

def md5(fname):
    hash_md5 = hashlib.md5()
    try:
        with open(fname, "rb") as f:
            chunk_size = 4096
            while chunk := f.read(chunk_size):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except PermissionError:
        print(f"Permission denied for file {fname}", flush=True)
    except FileNotFoundError:
        print(f"File not found: {fname}", flush=True)
    except IOError as e:
        print(f"I/O error({e.errno}) for file {fname}: {e.strerror}", flush=True)
    except Exception as e:  # A generic catch-all for any other exceptions
        print(f"Error processing file {fname}: {e}", flush=True)
    return None

def get_memory_usage():
    memory_info = process.memory_info()
    memory_used_mb = memory_info.rss / 1024 / 1024  # Convert bytes to MB
    return memory_used_mb


def walk_and_check_hashes(directory, hash_file_path):
    hash_set = set()
    files_processed = 0
    total_files = 0
    found_match = False  # Variable to track if any hash matches are found

        # Print initial memory usage
    initial_usage = get_memory_usage()
    print(f"Initial memory usage: {initial_usage:.2f} MB")


    start_time = time.time()  # Capture the start time


    # Load the hashes from the hash file
    try:
        with open(hash_file_path, 'r') as hash_file:
            for line in hash_file:
                hash_set.add(line.strip())
    except Exception as e:
        print(f"Error loading hash file: {e}", flush=True)
        return

    # First, count all files to be scanned
    for root, dirs, files in os.walk(directory):
        total_files += len(files)

    print(f"Total files to be scanned: {total_files}")

    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for name in files:
            # Check memory usage before processing each file
            current_usage = get_memory_usage()
            if current_usage > MEMORY_THRESHOLD_MB:  # Define MEMORY_THRESHOLD_MB as appropriate
                print(f"\nWarning: High memory usage detected - {current_usage:.2f} MB")

            file_path = os.path.join(root, name)
            file_hash = md5(file_path)

            if file_hash in hash_set:
                print(f"\033[91mHash match found for {file_path}\033[0m", flush=True)
                found_match = True  # Update found_match to True if a match is found

            files_processed += 1
            if files_processed % 10 == 0:  # Print every 10 files
                print(f"\rProcessed {files_processed} files...", flush=True)

    end_time = time.time()  # Capture the end time
    elapsed_time = end_time - start_time  # Calculate the elapsed time

    # After processing all files, print the final messages
    print(f"\nFinished processing. Total files processed: {files_processed}")
    print(f"Number of hashes used for comparison: {len(hash_set)}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

    if not found_match:  # Check if no matches were found
        print("No matching hashes found.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: <script> <directory_to_scan> <hash_file_path>")
    else:
        directory_to_scan = sys.argv[1]
        hash_file_path = sys.argv[2]
        MEMORY_THRESHOLD_MB = 300  # Set an appropriate memory usage threshold in MB
        walk_and_check_hashes(directory_to_scan, hash_file_path)

# LEGEND
# https://virusshare.com/hashes
    #     directory_to_scan = "/home/q/Documents/libri/infosec"
    # hash_file_path = "/home/q/Documents/cyber_security/hashes/unpacked"
