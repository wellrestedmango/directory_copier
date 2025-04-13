import os
import glob
import shutil
import re
import hashlib
import argparse
from argparse import ArgumentParser

#taking in the path to crawl and the path to save de-duped files to
parser = ArgumentParser(prog="main")
parser.add_argument('-src', help='This is the source directory')
parser.add_argument('-dst', help="this is the destination directory")
args = parser.parse_args()

#setting up variables I want to track
unique_md5_sums = []
unique_files = 0
duplicate_files = 0

#taking in arguments
src_dir = args.src
dst_dir = args.dst


#transverse the directory
for p in glob.glob('**', recursive=True, root_dir=src_dir):
    #only choosing to open pdfs for me - alter the regex to change this behavior
    if os.path.isfile(os.path.join(src_dir, p)) and re.search('.(pdf)$', p):
        file_path = os.path.join(src_dir, p)
        #open each file that matches the regex test 
        with open(file_path, 'rb') as file_obj:
            #I was only interested in unique files. Remove md5 check to copy all files
            file_content = file_obj.read()
            md5_hash = hashlib.md5(file_content).hexdigest()
            if md5_hash in unique_md5_sums:
                print(f'{p} is a dupe')
                duplicate_files += 1
                pass
            else:
                unique_md5_sums.append(md5_hash)
                os.makedirs(os.path.join(dst_dir, os.path.dirname(p)), exist_ok=True)
                shutil.copy(os.path.join(src_dir, p), os.path.join(dst_dir, p))
                unique_files += 1

#printing stats of interest
print(f'there are {unique_files} unique files')
print(f'there are {duplicate_files} duplicate files')
