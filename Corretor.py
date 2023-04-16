from Contato import Contato
import regex as reg


class Corretor():
    def __init__(self, primeiro_nome, sobrenome, contato: Contato, num_susep, apolice):
        self._primeiro_nome = primeiro_nome
        if len(primeiro_nome) < 2 or primeiro_nome == '':
            raise print(f"{primeiro_nome} deve conter no mínimo 2 carcteres")
        
        
        self._sobrenome = sobrenome
        if len(sobrenome) < 2 or self._sobrenome == '':
            raise print(f"{self._sobrenome} deve conter no mínimo 2 carcteres")
        
        self._contato = contato
        self._num_susep= num_susep
        formato_num_susep = reg.compile('^154146[0-9]{11}')
        if formato_num_susep.search(self._num_susep) is None:
            raise print("Rever o formato do numero Susep")
        
        self._apolice = apolice


Contato1 = Contato("123","123","123","erikagascao@gmail.com")        
corret1 = Corretor("Paloma", "Ferraz", Contato1, "15414612345678901", "774")
