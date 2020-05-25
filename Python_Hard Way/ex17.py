from sys import argv
# exists function returns true if the file exists
from os.path import exists

script, fromFile, toFile = argv

print(f"Copying from {fromFile} to {toFile}")

# we could do these two in one line
inFile = open(fromFile)
inData = inFile.read()

print(f"The input file is {len(inData)} bytes long.")

print(f"Does the output file exist? {exists(toFile)}")
print("Really, hit RETURN to continue, CTRL-C to abort.")
input()

outFile = open(toFile,'w')
outFile.write(inData)

print("All right, all done!")

outFile.close()
inFile.close()