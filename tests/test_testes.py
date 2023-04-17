from Pessoa import Pessoa
from datetime import date
from Endereco import Endereco
from Contato import Contato


class Testclas:
    def test_quando_pessoa_recebe_Diego_Guerrieri_deve_retornar_Diego_Guerrieri_no_nome_completo(self):
        # Given - contexto
        nome = "Diego"
        sobrenome = "Guerrieri"
        esperado = "Diego Guerrieri"
        endereco1 = Endereco("Mercês", "43", "casa", "123", "RJ", "RJ")
        Contato1 = Contato("123","123","123","erikaabc@gmail.com")
        pessoa1 = Pessoa(nome, sobrenome, date(2000,1,1),"058.784.477-97","123",endereco1, Contato1)
        
        # when - ação
        resultado = pessoa1.nome_completo()
        
        # then - desfecho
        assert resultado == esperado
        
    
    