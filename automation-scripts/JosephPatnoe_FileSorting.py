# Joseph Patnoe
# CIS188

"""
A script that moves all files within files.zip to folders respective of
their file type. This prints a directory listing of each folder and how many 
items are in each one.

"""
# Import Modules
import os
import shutil
from zipfile import ZipFile

# Unzip the file
with ZipFile('files.zip', 'r') as zip_ref:
    zip_ref.extractall('files')

# Directories to create
pdf_dir = 'pdf'
images_dir = 'images'

# Create directories if they do not exist
if not os.path.exists(pdf_dir):
    os.makedirs(pdf_dir)

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Walk through all files and directories in the extracted folder
for root, _, files in os.walk('files'):
    for file in files:
        if file.endswith('.pdf'):
            
# Move PDFs to the pdf directory
            source = os.path.join(root, file)
            destination = os.path.join(pdf_dir, file)
            shutil.move(source, destination)
        elif file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):

# Move images to the images directory
            source = os.path.join(root, file)
            destination = os.path.join(images_dir, file)
            shutil.move(source, destination)

# Print directory listing and count
print("Files in 'pdf' directory:")
pdf_files = os.listdir(pdf_dir)
for file in pdf_files:
    print(file)
print(f"Total PDF files: {len(pdf_files)}")

print("\nFiles in 'images' directory:")
image_files = os.listdir(images_dir)
for file in image_files:
    print(file)
print(f"Total image files: {len(image_files)}")
