import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
fileNames = (glob.glob(pattern))

# TODO: use os.path.getsize to find each file's size
# each_element represents items in fileNames list
# os.path.getsize is a function which finds the size of the item and stores it in variable fileSizes
for each_element in fileNames:
    fileSizes = os.path.getsize(each_element)
# TODO: Add a test to only display files that are not zero length
# if the size of the file is not 0, the size will be printed alongside the name of the file and its name
# else condition not required as nothing needs to happen if file size is 0
    if fileSizes != 0:
        print(fileSizes)
# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename() the leading directory removed and the name is stored in fileBaseName variable
        fileBaseName = os.path.basename(each_element)
        print(fileBaseName)