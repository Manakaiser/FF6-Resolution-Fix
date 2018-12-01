import sys

FileStream = open(sys.argv[1], 'rb') #we are opening the file given on commandline parameter. rb stands for 'read binary'
OriginalBuffer = FileStream.read() #we are now reading FULL content of the file into OriginalBuffer array
FileStream.close() #we don't need this file anymore locked as stream
OriginalBuffer = list(OriginalBuffer) #we are making a list, because python array is immutable
OriginalBuffer[0] = '\xC0'
OriginalBuffer[1] = '\x03'
OriginalBuffer[4] = '\x80'
OriginalBuffer[5] = '\x02'
FileWrite = open(sys.argv[1], 'wb') #we appended a _swapped to filename and opened in WriteBinary mode
FileWrite.write(''.join([str(i) for i in OriginalBuffer]))
FileWrite.close()