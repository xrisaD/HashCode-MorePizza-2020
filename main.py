import in_out_files,solve
example = "b_small" "a_example"
small = "b_small"
big
name = example
m, pizzas = in_out_files.read_file(name+".in")
vector = solve.brute_force(m,pizzas)
print(vector)
in_out_files.write_file(name+".out",vector)
