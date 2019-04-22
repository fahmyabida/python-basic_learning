import random

# 1.a
persons = ["fahmy", "abida", "asa", "firda", "usi", "melinda", "kusuma", "wardani", "dani", "linda"]
# 1.b
verbs = ["menendang", "mencangkul", "melukai", "menyayangi", "membantu", "menolong", "memasak", "membersihkan", "menata", "mengayuh"]
# 1.c
objects = ["televisi", "kasur", "bola", "sapu", "kaca", "meja", "kursi", "lampu", "bantal", "almari"]

# 2.a
i = 1
for person in persons:
    for verb in verbs:
        for obj in objects:
            print i
            print person + " " + verb + " " + obj
            i = i + 1

# 2.b
comprehension = [ person + " " + verb + " " + obj for person in persons for verb in verbs for obj in objects]
print "array list"
print comprehension

# 2.c
for x in range(10):
    mixPersonsVerbsObjects = random.choice(persons) + " " + random.choice(verbs) + " " + random.choice(objects)
    print mixPersonsVerbsObjects

# 2.d
comprehensionV2 = [random.choice(persons) + " " + random.choice(verbs) + " " + random.choice(objects) for x in range(10)]
print comprehensionV2

# 3.a
for x in range(10):
    randomPersons   = random.choice(persons)
    randomVerbs     = random.choice(verbs)
    randomObjects   = random.choice(objects)
    mixPersonsVerbsObjects = randomPersons + " " + randomVerbs + " " + randomObjects
    if "n" in randomVerbs:
        print "have character 'n' in verb " + str.upper(randomVerbs)
        print mixPersonsVerbsObjects
    else:
        print "NOT have character 'n' in verb " + str.upper(randomVerbs)
        print mixPersonsVerbsObjects