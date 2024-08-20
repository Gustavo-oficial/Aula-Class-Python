from datetime import date

class Pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        return rendimento
    
class PessoaFisica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cpf="", rg="", dataNascimento=None):
        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()

        super().__init__(nome, rendimento, endereco)

        self.rg = rg
        self.cpf = cpf
        self.dataNascimento = dataNascimento

        def calcular_imposto(self, rendimento: float) -> float:
            if rendimento <= 1500:
                return 0
            elif 1500 < rendimento <= 3500:
                return (rendimento / 100) * 2
            elif 3500 < rendimento <= 6000:
                return (rendimento / 100) * 3.5
            else:
                return (rendimento / 100) * 5

class PessoaJuridica(Pessoa):
    def __init__(self, nome="", rendimento=0.0, endereco=None, cnpj=""):
        if endereco is None:
            endereco = Endereco()

        super().__init__(nome, rendimento, endereco)

        self.cnpj = cnpj

class Endereco:
    def __init__(self, logradouro="", numero="", endereco_Comercial=""):
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial