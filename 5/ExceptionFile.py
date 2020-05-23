try:
    fh = open("testfile", "r")
    str = fh.read()
    numlist = str.split()
    print(numlist)
    for i in numlist:
        if int(i) < 0:
             raise Exception(int(i))
except Exception as e:
    print("error in level argument", e.args[0])
finally:
    fh.close()
    print ("Operation completed")