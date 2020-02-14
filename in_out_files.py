import numpy as np
def read_file(filepath): 
    with open(filepath) as fp:
        line = fp.readline()
        mn = list(line.split(" ")) 
        line = fp.readline()
        pizzas = list(map(int,list(line.replace('\n', '').split(" "))))
    return int(mn[0]),pizzas
def write_file(name,vector):
    f = open(name, "w")
    index = np.nonzero(vector)
    res_index = list(index[0])
    string = str(len(res_index)) + "\n"
    list_to_string = ' '.join([str(elem) for elem in res_index])
    string += list_to_string
    print(string)
    f.write(string)
    f.close()
