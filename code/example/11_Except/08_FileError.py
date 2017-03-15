#!/usr/bin/python3
'''
Open File Error 
1. Create a file a named mydata2.txt
2. Write some data with open in try.
3. Catch FileNotFoundError
4. Else print contents.
5. Finally: open nonexisted file mydata3.xtx
'''
try:
	myFile = open ("myData2.txt", encoding="utf-8")

except FileNotFoundError as ex:
	print ("File not found")
	print (ex.args)

else:
	print ("File: ", myFile.read())
	myFile.close()

finally:
	print ("Finished")