#combo selector
import random
import csv
import itertools
import json
pongballs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
combinations = [16, 15, 14, 13, 11, 9, 8, 6, 5, 4, 3, 1]
teams = ["Nick","Mike","Chris","Jeff","Shawn","Pags","Conor","Andy","Matt","Drew","Ben","Tyler"]
finaltest = {"Nick":[],"Mike":[],"Chris":[],"Jeff":[],"Shawn":[],"Pags":[],"Conor":[],"Andy":[],"Matt":[],"Drew":[],"Ben":[],"Tyler":[]}
count = 0

act_combos = list(itertools.combinations(pongballs, 2))

for c in combinations:
    i = combinations.index(c)
    tm = teams[i]
    for t in range(combinations[i]):
        chosen_combo = random.choice(act_combos)
        act_combos.remove(chosen_combo)

for key, value in finaltest.items():
    print key, len(value)
    count += len(value)

print count
print finaltest

writer = csv.writer(open('test.csv', 'wb'))
for key, value in finaltest.items():
        writer.writerow([key, value])

with open('combos.json', 'w') as fp:
    dump = json.dump(finaltest, indent=2, separators=[',', ':'])
    fp.write(dump)
