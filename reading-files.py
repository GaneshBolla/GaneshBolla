count_file = open("C:/Users/GBOLLA/PycharmProjects/Python/venv/file-python.txt","r")
#print(count_file.readable())
#print('Reading 1st & 2nd lines from file')
#print(count_file.readline()) this will print 1st line
#print(count_file.readline())  # this will print 2nd line

#print('Print index row from a file')
#print(count_file.readlines()) ## in this output if readline() is calling out put of that will not come in this step

# For Loop of a file.
for lines in count_file.readlines():
    print(lines)

count_file.close()