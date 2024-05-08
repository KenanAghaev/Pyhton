# Esas class
class Das:
    def __init__(self, reng):
        self.reng = reng

    def hereket(self):
        pass

# Piyada class
class Piyada(Das):
    def __init__(self, reng):
        super().__init__(reng)

    def hereket(self):
        print("Piyada ileri tek bir addim gede biler.")

# Top class
class Top(Das):
    def __init__(self, reng):
        super().__init__(reng)

    def hereket(self):
        print("Top düz xettlerde limitsiz ileri, geri, sağa ve ya sola hereket ede biler.")

# Fil class
class Fil(Das):
    def __init__(self, reng):
        super().__init__(reng)

    def hereket(self):
        print("Fil çapraz xetlerde limitsiz ileri ve ya geri hereket ede biler.")

# At class
class At(Das):
    def __init__(self, reng):
        super().__init__(reng)

    def hereket(self):
        print("At 'L' formasinda hereketler ede biler.")

# Vezir class
class Vezir(Das):
    def __init__(self, reng):
        super().__init__(reng)

    def hereket(self):
        print("Vezir düz ve ya çapraz xettlerde limitsiz ileri, geri, sağa, sola veya çapraz hereket ede biler.")

# Şah class
class Sah(Das):
    def __init__(self, reng):
        super().__init__(reng)

    def hereket(self):
        print("Şah bir addim ileri, geri, sağa, sola veya çapraz hereket ede biler.")




piyada_ag = Piyada("Ag")
top_qara = Top("Qara")
fil_qara = Fil("Qara")
at_ag = At("Ag")
vezir_ag = Vezir("Ag")
sah_qara = Sah("Qara")

# Polymorphism
def taxtada_hereket(tahta):
    for das in tahta:
        print(das.reng + " daş hereket ede biler:")
        das.hereket()
taxtada_hereket([piyada_ag, top_qara, fil_qara, at_ag, vezir_ag, sah_qara])


