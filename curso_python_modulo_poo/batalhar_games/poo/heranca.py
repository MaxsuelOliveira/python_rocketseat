class EsteticaAutomotiva:
    def __init__(self, nome):
        self._nome = nome

    def pintar(self):
        return
    
    def polir(self):
        print(f"O carro {self._nome} foi polido.")
    
    def lavar(self):
        print(f"O carro {self._nome} foi lavado.")

    def trocar_pneus(self):
        print(f"Servico fica no valor de R$ 100,00.")


class EmpresaFilial(EsteticaAutomotiva):
    def pintar(self):
        print(f"O carro {self._nome} foi pintado na cor.")

    def orcamento(self):
        self.trocar_pneus()
        

servico1 = EmpresaFilial(nome="Virtual 2020")
servico1.orcamento()
servico1.pintar()
