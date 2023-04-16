from Apolice import Apolice, TipoApolice
from Beneficiario import Beneficiario
from Calculadora import Calculadora
from Corretor import Corretor   
from Endereco import Endereco
from Segurado import Segurado
from datetime import date
from Contato import Contato

     
endereco1 = Endereco("Merces", "43", "casa", "123", "RJ", "RJ")
endereco2 = Endereco("Tres Rios", "172", "casa", "22745160", "RJ", "RJ")
Contato1 = Contato("123","123","123","erikaabc@gmail.com")
benef1 = Beneficiario("Erika", "Gascao", date(2000, 1, 1), "123.456.789-99", "798", endereco1, Contato1, "filha")
benef2 = Beneficiario("Fernanda", "Muniz", date(1992, 7, 21), "123.456.789-99", "9878",endereco2, Contato1, "esposa")
corret1 = Corretor("Paloma", "Ferraz", "002", "15414612345678901", "774")            
seg1 = Segurado ("aaa", "Guerrieri", date(1987,11,30), "112.367.805-97", "1254877", endereco2, Contato1, [benef1, benef2], corret1, "apol1")
apol1 = Apolice (TipoApolice.Vida, 100, 1000000, seg1,corret1, date(2024, 1, 1), date(2023, 3, 30),"Ativa")
apol2 = Apolice (TipoApolice.Casa, 500, 5000000, seg1,corret1, date(2024, 2, 2), date(2023, 3, 30),"Cancelada")
apol1._numero
calc1 = Calculadora([apol1, apol2])
apol1._tipo.value
calc1.calcula()
print(benef1)
seg1._beneficiarios[0]._primeiro_nome
seg1._beneficiarios[0]
print(seg1)


