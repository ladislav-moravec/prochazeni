class Lokace:
    # Třáda reprezentuje lokaci

    sever   = None # Lokace na severu
    jih     = None # Lokace na jihu
    zapad   = None # Lokace na zapade
    vychod  = None # Lokace na vychode

    nazev   = None # Název lokace
    popis   = None # Dlouhý popis lokace

    def __init__(self, nazev, popis):
        self.nazev = nazev
        self.popis = popis

    def __str__(self):
        vystup =    ( self.nazev + "\n"
                    + self.popis + "\n\n")
        smery = ""
        if self.sever:
            smery += "sever "
        if self.jih:
            smery += "jih "
        if self.zapad:
            smery += "západ "
        if self.vychod:
            smery += "východ "
        vystup += "Můžeš jít na {0}\n".format(smery)
        return vystup
