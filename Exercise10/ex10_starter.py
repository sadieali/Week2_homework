import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    home_directory = os.environ['HOMEPATH']
else:
    home_directory = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(home_directory, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
# glob searches files for a wildcard pattern
fileNames = (glob.glob(pattern))

# TODO: use os.path.getsize to find each file's size
# each_element represents items in fileNames list
# os.path.getsize is a function which finds the size of the item and stores it in variable fileSizes
# for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)
# in this case, it is incrementing each element in the fileNames list
for each_element in fileNames:
    fileSizes = os.path.getsize(each_element)
# TODO: Add a test to only display files that are not zero length
# != is a value inequality
# if the size of the file is not 0, the size will be printed alongside the name of the file and its name
# else condition not required as nothing needs to happen if file size is 0
    if fileSizes != 0:
        print(fileSizes)
# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename() the leading directory removed and the name is stored in fileBaseName variable
# nested this function so that only files larger than 0 will be printed
        fileBaseName = os.path.basename(each_element)
        print(fileBaseName)
