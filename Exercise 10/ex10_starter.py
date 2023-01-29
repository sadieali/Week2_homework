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
for each_element in fileNames:
    fileSizes = os.path.getsize(each_element)
# TODO: Add a test to only display files that are not zero length
    if fileSizes != 0:
        print(fileSizes)
# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
        fileShortName = os.path.basename(each_element)
        print(fileShortName)
