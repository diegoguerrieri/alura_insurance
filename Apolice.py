from enum import Enum
from Segurado import Segurado
from datetime import date
from Corretor import Corretor
from datetime import date
import uuid

class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4
        
class Apolice():
    def __init__(self, tipo: TipoApolice, valor_premio, valor_benef, segurado, corretor: Corretor, vig: date, dt_criacao: date, status):
        self._numero = uuid.uuid1() 
        self._tipo = tipo
        if tipo == TipoApolice.Vida:
            pass
        else:
            raise("Esse tipo não é válido!")
            
        self._valor_premio = valor_premio
        if valor_premio > 0:
            pass
        else:
            raise("Valor precisa ser maior do que 0")
        
        self._valor_benef = valor_benef
        if valor_benef > 0:
            pass
        else:
            raise("Valor precisa ser maior do que 0")
        
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        if date.today() < vig:
            pass
        else:
            raise("Vigência precisa ser futura!")
        
        self._dt_criacao = dt_criacao
        if date.today() > dt_criacao:
            pass
        else:
            raise("A data precisa ser no passado!")
        
        self._status = status
        if status in ['Ativa', 'Liquidada', 'Cancelada', 'Em_Sinistro']:
            pass
        else:
            raise("O status precisa ser válido!")
    
    def __str__(self):
        return f"{self._numero} - {self._vig.strftime('%d/%m/%Y')} - {self._dt_criacao.strftime('%d/%m/%Y')}"
    
