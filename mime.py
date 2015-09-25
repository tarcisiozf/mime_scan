#!/usr/bin/python
import sys
import os
from mimetypes import MimeTypes

# Terminal arguments
argv = sys.argv

# Set params from arguments
params = {}
params['dir'] = argv[1]
params['allowed'] = argv[2]

# Get file list
files_list = []

for root, dirs, files in os.walk(params['dir']):
	for file_name in files:
		files_list.append(root + '/' + file_name)

# Get allowed mime types
allowed_content = open(params['allowed']).read()
allowed_list = allowed_content.split('\n');

# Walk in the folder
mime = MimeTypes()

for file_name in files_list:
	# Get the mime type of a file
	file_mime = mime.guess_type(file_name)[0]

	# Remove the file if the mime type is not allowed
	if file_mime not in allowed_list:
		os.remove(file_name)
		print [file_name, file_mime]
