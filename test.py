__author__ = 'henrikmnm'

constraints = {"WA":{"SA": [('red', 'green'), ('blue', 'green')]}}

domains = {"WA": ['red', 'green', 'blue'], "SA": ['red', 'green', 'blue']}

var = "WA"
var2 = "SA"

constraints = constraints[var][var2]

for x in domains[var]:

    mustchange = True

    for y in domains[var2]:

        if (x ,y) in constraints:
            mustchange = False

        if mustchange:
            domains[var].remove(x)

print domains[var]


