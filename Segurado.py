from Pessoa import Pessoa
from typing import List
from Beneficiario import Beneficiario
from Corretor import Corretor
from datetime import date
from Endereco import Endereco
from Contato import Contato
from dateutil.relativedelta import relativedelta

class Segurado(Pessoa):
    def __init__(self, primeiro_nome, sobrenome, data_nasc, cpf, rg, endereco, contato, beneficiarios: List[Beneficiario], corretor: List[Corretor], apolice):
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
    
endereco1 = Endereco("Merces", "43", "casa", "123", "RJ", "RJ")
endereco2 = Endereco("Tres Rios", "172", "casa", "22745160", "RJ", "RJ")
Contato1 = Contato("123","123","123","erikagascao@gmail.com")
benef1 = Beneficiario("Erika", "Gascao", date(2000, 1, 1), "112.367.805-97", "798", endereco1, Contato1, "filha")
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "112.367.805-97", "9878",endereco2, Contato1, "esposa")
corret1 = Corretor("Paloma", "Ferraz", Contato1, "15414612345678901", "774")

seg1 = Segurado ("aaa", "Guerrieri", date(1987,11,30), "112.367.805-97", "1254877", endereco2, Contato1, [benef1, benef2], corret1, "apol1")
print("Olá Mundo")

