import os

from models.pessoa import Pessoa
from models.enums.generos import Generos
from models.endereco import Endereco

os.system("cls || clear")

# Instaciando classe:

pessoa1 = Pessoa("Marta", "74", Generos.FEMININO, 
                 Endereco("Avenida 8", "85"))

print(pessoa1)