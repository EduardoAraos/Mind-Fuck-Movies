import random
f = open(r"./MFML.csv", "r", encoding="utf8")
movies = f.read().splitlines()
print(random.choice(movies))
