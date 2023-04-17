from Pessoa import Pessoa
from typing import List
from Beneficiario import Beneficiario
from Corretor import Corretor
from datetime import date
from dateutil.relativedelta import relativedelta
from Apolice import Apolice

class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios: List[Beneficiario], corretor: List[Corretor], apolice: List[Apolice]):
        super().__init__(primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato)
        self._beneficiarios = beneficiarios
        if len(self._beneficiarios) > 10:
            return print("Rever os beneficiários")
        
        self._corretor = corretor
        self._apolice = apolice
        if relativedelta(date.today(), self._data_nasc).years < 18:
            raise print("idade precisa ser maior do que 18")
        
        
    def __str__(self):
        lista = [str(p) for p in self._beneficiarios]
        return f"{lista}"

    def calcula_premio(self):
        return sum(x._valor_premio for x in self._apolice) 
        
