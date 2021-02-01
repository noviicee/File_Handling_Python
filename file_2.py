import os
from datetime import *
#importing os, datetime

stats=os.stat('abc.txt')
print("File size in bytes=",stats.st_size)
print("File's last accessed time:",datetime.fromtimestamp(stats.st_atime))
print("File's last modified time:",datetime.fromtimestamp(stats.st_mtime))
#We get the time in Human-Understandable form; 24hr format.