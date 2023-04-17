from Pessoa import Pessoa
from datetime import date

class Beneficiario(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, tipo):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._tipo = tipo
        if date.today() < self._data_nasc:
            raise print("data de nascimento não pode ser futura")

    def __repr__(self):
        return self.__str__()