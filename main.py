import in_out_files,solve
m, pizzas = in_out_files.read_file("b_small.in")
x = solve.brute_force(m,pizzas)
print(x)
