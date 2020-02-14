def read_file(filepath): 
    with open(filepath) as fp:
        line = fp.readline()
        mn = list(line.split(" ")) 
        line = fp.readline()
        pizzas = list(map(int,list(line.replace('\n', '').split(" "))))
    return int(mn[0]),pizzas
