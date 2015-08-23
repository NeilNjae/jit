import csv
import json

BASENAME = 'test1'
INFILE = BASENAME + '.csv'
JSFILE = BASENAME + '.js'
HTMLFILE = BASENAME + '.html'

infile = csv.DictReader(open(INFILE))
lines = list(infile)

nodes=[]
for line in lines:
    # update edges depending on what's in each node
    node={"id": line["ID"], "name": line["Name"],
    	"data": {"text": line["Text"]},
        "adjacencies": []}
    nodes.append(node)
for line in lines:
    if line["To"]:
        id_from=line["ID"]
        id_to=line["To"]
        for node in nodes:
            if node["id"] == id_to:
                if line["Type"] == 'R':
                    node["adjacencies"].append({"nodeTo": id_from,
                                                "data": {"weight": 1,
                                                         "$color": "#f00",
                                                         '$arg_type': 'refute',
                                                         '$arc_end': 'd'}})
                else:
                    node["adjacencies"].append({"nodeTo": id_from,
                                                "data": {"weight": 1,
                                                         '$arg_type': 'support',
                                                         '$arc_end': 'd'}})
            if node["id"] == id_from:
                if line["Type"] == 'R':
                    node["adjacencies"].append({"nodeTo": id_to,
                                                "data":{"weight": 1,
                                                        "$color": "#f00",
                                                        '$arg_type': 'refute',
                                                        '$arc_end': 's'}})
                else:
                    node["adjacencies"].append({"nodeTo": id_to,
                                                "data": {"weight": 1,
                                                         '$arg_type': 'support',
                                                         '$arc_end': 's'}})

with open(JSFILE, 'w') as f:
    with open('hypertree-preamble.txt') as p:
        f.write(p.read())
    json.dump(nodes, f, indent=4)
    with open('hypertree-postamble.txt') as p:
        f.write(p.read())
        