class EsteticaAutomotiva:
    def __init__(self, nome):
        self._nome = nome
        self._valores_manutencao = [
            {   
                "servico" : "Troca de oleo.",
                "valor" : 150
            },
            {  
                "servico" : "Troca de freios",
                "valor" : 280
            },
            
            { 
                "servico" : "Troca de freios",
                "valor" : 150
            },
            
            {
                "servico" : "Balanceamento",
                "valor" : 300
            },
        ]

    def pintar(self):
        return
    
    def polir(self):
        print(f"O carro {self._nome} foi polido.")
    
    def lavar(self):
        print(f"O carro {self._nome} foi lavado.")

    def trocar_pneus(self):
        print(f"Servico fica no valor de R$ 100,00.")

class EmpresaFilial(EsteticaAutomotiva):
    def modelo(self):
        print(f"O carro é um {self._nome}")
        
    def pintar(self):
        print(f"O carro {self._nome} foi pintado na cor.")

    def orcamento(self):
        self.trocar_pneus()

    def manutencao(self):
        print("Manutencao estimada em : ")
        for servico in self._valores_manutencao:
            print("{} - R${}".format(servico["servico"],servico["valor"]))
        
# servico1 = EmpresaFilial(nome="Virtual 2020")
# servico1.modelo()
# servico1.manutencao()

# Encapsulamento de de dados.
class ContaEmpresa:
    def __init__(self, saldo):
        self.__saldo = saldo
        
    def depostiar(self, valor):
        if valor > 0 :
            self.__saldo += valor
        else :
            print("O valor nao pode ser negativo")
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -=valor
        else :
            print("Saldo insuficiente.")
            
            
    def consultar_saldo(self):
        return self.__saldo
    
contaEmpresaFilial1 = ContaEmpresa(saldo=1000)
print("Saldo : {}".format(contaEmpresaFilial1.consultar_saldo()))
contaEmpresaFilial1.depostiar(500)
print("Saldo : {}".format(contaEmpresaFilial1.consultar_saldo()))
contaEmpresaFilial1.sacar(200)
print("Saldo : {}".format(contaEmpresaFilial1.consultar_saldo()))
