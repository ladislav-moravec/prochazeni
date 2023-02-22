from hra import Hra
hra = Hra()
prikaz = ""
print("\nJak hrát: Příkaz zmůže vypadat například \"jdi na server\" hru ukončíš slovek \"konec\"\n\n")
while prikaz.lower() != "konec":
    print(hra.vrat_aktualni_lokaci())
    print("Zadej příkaz: ", end="")
    prikaz = input()
    hra.zpracuj_prikaz(prikaz)
