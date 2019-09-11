import random
import json
import copy


def import_json(name):
    x = json.load(open(name,'r'))
    return x

def main():
    names = import_json('names.json')
    for name in names:
        name['count'] = 2
    
    caller = []
    for i,name in enumerate(names):
        caller.append(copy.deepcopy(name))
        caller[i].update(persons = [])
        for x in range(2):
            working = False
            while(not working):
                person = random.choice(names)
                if person['name'] == caller[i]['name']:
                    working = False
                elif person['count'] == 0:
                    working = False
                else:
                    if x == 1:
                        if caller[i]['persons'][0]['name'] == person['name']:
                            working = False
                        else:
                            caller[i]['persons'].append(copy.deepcopy(person))
                            working = True
                            person['count'] = person['count'] - 1 
                    else:
                        caller[i]['persons'].append(copy.deepcopy(person))
                        working = True
                        person['count'] = person['count'] - 1 

    for name in caller:
        print("Your Name: " + name['name'])
        for person in name['persons']:
            print("Name: " + person['name'] + '\nPhone: ' + person['phone'])
        print('\n\n')

if __name__ == "__main__":
    main()
