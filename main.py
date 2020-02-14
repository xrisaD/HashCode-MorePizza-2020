import in_out_files,solve
path_in = "input\\"
path_out = "output\\"
example = "a_example"
small = "b_small"
medium = "c_medium"
quite_big = "d_quite_big"
also_big = "e_also_big"

name = also_big

m, pizzas = in_out_files.read_file(path_in+name+".in")
vector = solve.many_greedy(m,pizzas)

in_out_files.write_file(path_out+name+".out",vector)

