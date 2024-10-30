"""szamlalo = 1
while szamlalo < 11:
    print(szamlalo)
    szamlalo += 1
    if szamlalo == 5:
        break
else:
    print("végigfutott a ciklus")

print("vége a programnak")


szamlalo = 0
while szamlalo < 11:
    szamlalo += 1
    if szamlalo == 5:
        continue
    print(szamlalo)

print('vége')
"""


def negyzet(alap):
    kerulet = 4 * alap
    terulet = alap * alap
    return kerulet, terulet


eredmeny = negyzet(3)
print(eredmeny[0])
print(eredmeny[1])
