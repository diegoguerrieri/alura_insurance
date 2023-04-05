from enum import Enum
from Segurado import Segurado
from datetime import date
from Corretor import Corretor

class TipoApolice(Enum):
    Vida = 1
    Carro = 2
    Casa = 3
    Viagem = 4
        
class Apolice():
    def __init__(self, numero, tipo: TipoApolice, valor_premio, valor_benef, segurado: Segurado, corretor: Corretor, vig: date, dt_criacao: date, status):
        self._numero = numero
        self._tipo = tipo
        self._valor_premio = valor_premio
        self._valor_benef = valor_benef
        self._segurado = segurado
        self._corretor = corretor
        self._vig = vig
        self._dt_criacao = dt_criacao
        self._status = status
    
    def __str__(self):
        return f"{self._numero} - {self._vig.strftime('%d/%m/%Y')} - {self._dt_criacao.strftime('%d/%m/%Y')}"