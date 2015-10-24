import os
import sys
filenames = os.listdir(sys.argv[1])
#filetype = 'credentials.csv'
ext = '.pem'

for filename in filenames:
    if ext in filename:
        sys.stderr.write ('File exists : %s\n'%filename)
        sys.exit(1)