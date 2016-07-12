
import random
import json

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

with open ('combos.json') as f:
    chosen_combos = json.load(f)


#teams = [chosen_combos.keys()]

#print "this is the list", teams
#teams.remove("matt")
#print "amended", teams

while chosen_combos:
    first_combo = random.choice(num_list)
    num_list.remove(first_combo)
    second_combo = random.choice(num_list)
    num_list.append(first_combo)
    combo_front = "{}|{}".format(str(first_combo),str(second_combo))
    combo_back = "{}|{}".format(str(second_combo),str(first_combo))
    print combo_front, combo_back
    for key, value in chosen_combos.items():
        if combo_front in value:
            chosen_one = key
            print "Selected:", chosen_one
            del chosen_combos[chosen_one]
            if combo_back in value:
                chosen_one = key
                print "Selected:", chosen_one
                del chosen_combos[chosen_one]
            else:
                continue
    print chosen_combos.keys()
        #teams.remove(chosen_one)
    #print "Remaining teams", teams



        #teams.remove(chosen_one)
        #print "These are remaining:", teams
