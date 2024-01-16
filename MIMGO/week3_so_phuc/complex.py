class SoPhuc:
    def __init__(self, phanthuc, phanao):
        self.phanthuc = phanthuc
        self.phanao = phanao

    def show(self):
        if self.phanao < 0:
            print(self.phanthuc, "-", abs(self.phanao), "* i")
        else:
            print(self.phanthuc, "+", self.phanao, "* i")

    def add(self, sophuc2):
        self.phanthuc += sophuc2.phanthuc
        self.phanao += sophuc2.phanao
        return self

    def sub(self, sophuc2):
        self.phanthuc -= sophuc2.phanthuc
        self.phanao -= sophuc2.phanao
        return self

    def mul(self, sophuc2):
        phanthuc_new = self.phanthuc * sophuc2.phanthuc - self.phanao * sophuc2.phanao
        phanao_new = self.phanthuc * sophuc2.phanao + self.phanao * sophuc2.phanthuc
        self.phanthuc = phanthuc_new
        self.phanao = phanao_new
        return self


# com1 = SoPhuc(1, 2)
# com2 = SoPhuc(3, 4)
# com1.add(com2).show()
# com1.sub(com2).show()
# com1.mul(com2).show()