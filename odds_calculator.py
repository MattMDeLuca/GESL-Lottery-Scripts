#odds calculator
import json

with open('combos.json') as f:
    team_combos = json.load(f)

while True:
    pick = raw_input("Enter team chosen: ")
    del team_combos[pick]
    total_combos = 0
    for v in team_combos.values():
        combos = len(v)
        total_combos = total_combos + combos
    for k, v in team_combos.items():
        combos_1 = len(v)
        perct = (float(combos_1)/total_combos)*100
        print k, combos_1, "{:.4}%".format(str(perct))
    if pick == "done":
        break
