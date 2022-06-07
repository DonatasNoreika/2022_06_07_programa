import pandas

metai = int(input("Iveskite metus: "))
if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
    print("Keliamieji metai")
else:
    print("Nekeliamieji metai")

print("Programos pabaiga")
