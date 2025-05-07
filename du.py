class Package:
    def __init__(self, odosielatel, primatel, vaha, status):
        self.odosielatel = odosielatel
        self.primatel = primatel
        self.vaha = vaha
        self.status = status

    def balik_info(self):
        return f"Balík pre: {self.primatel} | Od: {self.odosielatel} | Váha: {self.vaha}kg | Stav: {self.status}"

    @property
    def delivered(self):
        return self.status == "Doručený"

    @delivered.setter
    def delivered(self, value):
        if value:
            self.status = "Doručený"
        else:
            self.status = "Na ceste"

balik1 = Package("Peter Novák", "Anna Kováčová", 2.5, "Na ceste")
balik2 = Package("Ján Hríb", "Lucia Bieliková", 1.2, "Prijatý")

print(balik1.balik_info())
print(balik2.balik_info())

balik1.delivered = True
print(f"Po zmene stavu: {balik1.balik_info()}")

balik2.delivered = False
print(f"Po zmene stavu: {balik2.balik_info()}")