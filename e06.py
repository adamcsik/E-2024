proba = 0
while True:
    erdemjegy = input("Milyen jegyet kér: ")
    try:
        erdemjegy = int(erdemjegy)
    except Exception as e:
        print(e)
        print("Nem számjegyet adott meg!")
        continue
    else:
        print("Örülök, hogy megtalálta a számjegyeket!")
    finally:
        proba += 1
    if erdemjegy == 5:
        break

print(proba, ". próbálkozásra sikerült!")
