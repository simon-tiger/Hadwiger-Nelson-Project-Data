print("Loading .csv file...")
csv_file = open("517.csv")
csv = csv_file.read()

print("Parsing .csv file...")
csv_lines = csv.split("\n")
csv_noheader = csv_lines[1:]

adjacencies = {}
for linestr in csv_noheader:
    line = linestr.split(",")
    vertex = line[0]
    if vertex != "":
        edges = line[1].split(";")
        adjacencies[vertex] = edges

print("Coloring graph...")
colors = [-1 for i in range(517)]
current = 1
S = set()
Q = [current]

while len(Q) != 0:
    current = Q[0]
    del Q[0]
    S.add(current)
    edges = adjacencies[str(current)]
    for i in edges:
        if int(i) not in S:
            Q.append(int(i))

    color = -1
    ok = False
    while not ok:
        color += 1
        ok = True
        for j in edges:
            if colors[int(j) - 1] == color:
                ok = False
    colors[current - 1] = color

print("Converting to file format...")
new_csv = "vertex,color\n"
for i in range(len(colors)):
    color = colors[i]
    new_csv += str(i+1) + "," + str(color) + "\n"

print("Writing to new .csv file...")
new_csv_file = open("colors.csv", "w")
new_csv_file.write(new_csv)
