import os #os module contains a function called stat()
with open ('abc.txt','w') as f:
	print(f.tell()) #file automatically gets closed after this line executes due to 'with'
print("Is the file closed?",f.closed)
#This was just to create a file named 'abc.txt' in case such a file does no exist

print()
stats=os.stat('abc.txt')
print(stats) #gives out an object of class 'os.stat_result', which somewhat looks alike tuple.

'''printing stats will give various kinds of information on the file.
But if we take a look at the last three elements, we get the following information-
st_atime = last accessed time
st_mtime = last modified time
st_ctime = last time when metadata got changed'''