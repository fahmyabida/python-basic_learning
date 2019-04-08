file1 = open("cars-list.txt")

readContentFromFile1 = file1.read()
print "Read RAW File -->\n", readContentFromFile1
print ""
print "Read with basic substring -->\n", readContentFromFile1[0:6]
print ""
print "Read RAW File but All in lowercase -->\n", readContentFromFile1.lower()
print ""

file2 = open("new-cars-list.txt","w+")
file2.write(readContentFromFile1)
print "file 2 has ben writed with file 1 content"

file1.close()
file2.close()