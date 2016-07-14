import os, sys, re

dirpath = raw_input("Give me the folder path?")

for file in os.listdir(dirpath):
    #newname = file.replace("Season ","S")
    #newname = newname.replace("Episode ", "E")
    newname = re.sub(r'Season\ ([0-9]+)\ Episode\ ([0-9]+)', r'S\1E\2', file)
    print "The old name is :" + file
    print "the new name is :" + newname

    os.rename(dirpath+os.sep+file, dirpath+os.sep+newname)
    print "done"

