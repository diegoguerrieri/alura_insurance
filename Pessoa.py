from Endereco import Endereco
from datetime import date, timedelta
from numpy import timedelta64
import regex as reg
from Contato import Contato
from Estado import Estado


class Pessoa():
    def __init__(self, primeiro_nome, sobrenome, data_nasc: date, cpf, rg, endereco: Endereco, contato: Contato):
        self._primeiro_nome = primeiro_nome
        if len(primeiro_nome) < 2 or primeiro_nome == '':
            raise ("primeiro_nome deve conter no mínimo 2 carcteres")
        
        
        self._sobrenome = sobrenome
        if len(sobrenome) < 2 or self._sobrenome == '':
            raise ("sobrenome deve conter no mínimo 2 carcteres")
        
        self._data_nasc = data_nasc
                
        self._cpf = cpf
        formato_cpf = reg.compile('\d{3}\.\d{3}\.\d{3}\-\d{2}')
        if formato_cpf.search(self._cpf) is None:
            raise ("Rever o formato do CPF")
        
        self._rg = rg
        if self._rg is None or self._rg == '':
            raise ("RG não pode ser nulo")
        
        self._endereco = endereco
        dict= {'rua': endereco._rua,'numero': endereco._numero,'cep':endereco._cep, 'cidade': endereco._cidade}
        for ender in dict:
            if dict[ender] is None or dict[ender].strip() == '':
                raise print("Endereço incompleto")
        
        try:
            Estado[endereco._estado]
        except:
            print("Digite um estado válido")
            raise
                   
        
        self._contato = contato
        formato_email = reg.compile('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
        if formato_email.search(contato._email) is None:
            raise ("Email incorreto")
        
        
    def nome_completo(self):
        return f"{self._primeiro_nome.title()} {self._sobrenome.title()}"

    def __str__(self):
        return f"{self._primeiro_nome} {self._sobrenome} - {self._data_nasc.strftime('%d/%m/%Y')}"


endereco1 = Endereco("Mercês", "43", "casa", "123", "RJ", "RJ")
endereco1._estado
Contato1 = Contato("123","123","123","erikagascao@gmail.com")
pessoa1 = Pessoa("aaa","abc", date(2000,1,1),"058.784.477-97","123",endereco1, Contato1)
print("Olá Mundo")
pessoa1._primeiro_nome

type(date.today())
date(date.today().year, date.today().month, date.today().day)
formato_cpf = reg.compile('\d{3}\.\d{3}\.\d{3}\-\d{2}')
cpf = "58.784.477-97"
formato_cpf.search(cpf)

