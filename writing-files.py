#count_file = open("C:/Users/GBOLLA/PycharmProjects/Python/venv/write.txt","w")
#count_file.write('This is writing from python to new file created by python')
#count_file.write('This is writing from python to existing file by python and overriding the file')

count_file = open("C:/Users/GBOLLA/PycharmProjects/Python/venv/write.txt","a")
count_file.write('\nAppending to existing file 2nd time')

count_file.close()