# directory_copier
Goes through a directory and copies unique files to a new location while keeping file structure. Can edit regex to get desired file types/patterns

For this project I wanted to go through a large file system, and only copy unique pdfs while keeping the stucture of the filesystem they were found in. This code can easily be altered to copy all items, or to copy different file types.

Takes in the filepath of the root directory of interest as -src and copies to the filepath specified by -dst.
