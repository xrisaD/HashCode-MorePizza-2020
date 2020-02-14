def read_file(filepath): 
    with open(filepath) as fp:
        line = fp.readline()
        mn = list(line.split(" ")) 
        line = fp.readline()
        slices = list(line.split(" "))
    return mn[0],slices
