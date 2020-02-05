print("Loading .edge file...")
edge_file = open("517.edge")
edge = edge_file.read()

edge_lines = edge.split("\n")
edge_noheader = edge_lines[1:]

print("Adding adjacencies to file...")
adjacencies = {}
for line in edge_noheader:
    edge = line[2:].split(" ")
    a = edge[0]
    if a != '':
        b = edge[1]
        try:
            adjacencies[a]
        except KeyError:
            adjacencies[a] = []
        adjacencies[a].append(b)
        try:
            adjacencies[b]
        except KeyError:
            adjacencies[b] = []
        adjacencies[b].append(a)

print("Converting to file format...")
csv = "vertex,edges\n"
adjacency_list = adjacencies.items()
for pair in adjacency_list:
    edges = pair[1]
    csv += pair[0] + ","
    for i in edges:
        csv += i + ";"
    csv = csv[:len(csv)-1]
    csv += "\n"

print("Writing to new .csv file...")
tgf_file = open("517.csv", "w")
tgf_file.write(csv)
