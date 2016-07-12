#odds calculator
import json

with open('combos.json') as f:
    team_combos = json.load(f)

while True:
    print
    pick = raw_input("Enter team chosen: ")
    if pick == "done":
        break
    print

    del team_combos[pick]
    total_combos = 0

    for v in team_combos.values():
        combos = len(v)
        total_combos += combos

    for k, v in team_combos.items():
        combos_1 = len(v)
        percent = (float(combos_1) / total_combos) * 100
        print k.ljust(7), str(combos_1).ljust(3), "{:.4}%".format(str(percent))
