import in_out_files,solve
example = "a_example"
small = "b_small"
medium = "c_medium"
quite_big = "d_quite_big"
also_big = "e_also_big"

name = also_big

m, pizzas = in_out_files.read_file(name+".in")
vector = solve.something_different(m,pizzas)

in_out_files.write_file(name+".out",vector)

