print("Loading .edge file...")
edge_file = open("517.edge")
edge = edge_file.read()

edge_lines = edge.split("\n")
edge_noheader = edge_lines[1:]

print("Adding vertices to file...")
tgf = ""
for i in range(1, 518):
    tgf += str(i)
    tgf += "\n"

tgf += "#\n"

print("Adding edges to file...")
for line in edge_noheader:
    tgf += line[2:]
    tgf += "\n"

print("Writing to new .tgf file...")
tgf_file = open("517.tgf", "w")
tgf_file.write(tgf)
