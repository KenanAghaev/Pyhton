class BankKarti:
    def __init__(self, kart, balans=0):
        self.kart = kart
        self.balans = balans

    def balans_goster(self):
        return self.balans

    def balans_artir(self, miqdar):
        self.balans += miqdar
        return f"{miqdar} AZN balansnize elave edildi. Yeni balansiniz: {self.balans} AZN"

    def pul_cek(self, miqdar):
        if self.balans >= miqdar:
            self.balans -= miqdar
            return f"{miqdar} AZN çekildi. Yeni balansniz: {self.balans} AZN"
        else:
            return "balans kifayet deyil!"

class KreditKarti(BankKarti):
    def __init__(self, kart, kredit_miqdari=0):
        super().__init__(kart)
        self.kredit_miqdari = kredit_miqdari

    def kredit_al(self, miqdar):
        self.kredit_miqdari += miqdar
        return f"{miqdar} AZN kredit cekildi. Umumi kredit miqdariniz: {self.kredit_miqdari} AZN"

    def kredit_aylik_odenis(self):
        return self.kredit_miqdari / 12

bank_karti = BankKarti("1234567890123456")
print(bank_karti.balans_goster()) 
print(bank_karti.balans_artir(1000)) 
print(bank_karti.pul_cek(500))  
print(bank_karti.pul_cek(700)) 


kredit_karti = KreditKarti("9876543210987654")
print(kredit_karti.kredit_al(5000)) 
print("{:.2f}".format(kredit_karti.kredit_aylik_odenis()))