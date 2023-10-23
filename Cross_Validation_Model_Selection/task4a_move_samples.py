import os
import shutil
import hashlib
import csv

def process_sample_directory(sample_dir, samples_csv, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the MD5 hashes from the "samples.csv" dataset
    sample_hashes = set()
    with open(samples_csv, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            md5_hash = row["MD5"]
            sample_hashes.add(md5_hash)

    # Function to calculate the MD5 hash of a file
    def calculate_md5(file_path):
        md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()

    # Iterate through the files in the sample directory
    for filename in os.listdir(sample_dir):
        file_path = os.path.join(sample_dir, filename)

        # Calculate the MD5 hash of the file
        file_hash = calculate_md5(file_path)

        # Check if the hash matches a sample hash
        if file_hash in sample_hashes:
            # Copy the file to the output folder
            shutil.copy(file_path, os.path.join(output_folder, filename))
            print(f"Copied {filename} to the 'samples' folder.")

if __name__ == "__main__":
    # Path to the directory containing the malware and benignware samples
    sample_dir1 = "/home/user/Desktop/benignware/"
    sample_dir2 = "/home/user/Desktop/malware/"  # Replace with the second path

    # Path to the "samples.csv" dataset
    samples_csv = "samples.csv"

    # Path to the folder where matching samples will be copied
    output_folder = "/home/sufian/Desktop/Lab5/samples/"

    # Process the first sample directory
    process_sample_directory(sample_dir1, samples_csv, output_folder)

    # Process the second sample directory
    process_sample_directory(sample_dir2, samples_csv, output_folder)
