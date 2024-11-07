def feladat1():
    print("I/A:")
    muz_nev =input("\n\tMúzeum neve: ")
    lat_nev = input("\n\tLátogató neve: ")
    ertekeles = int(input("\n\tÉrtékelés(1-20): "))


    if ertekeles <= 0:
        print("\n\tAz értékelés nem lehet negatív vagy 0!")
    elif ertekeles >= 20:
        print("\n\t20 pont feletti értékelés nem elfogadható!")
    else:
        print("\n\tKöszönjük az értékelést!")

