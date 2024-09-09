from models.enums.generos import Generos
from models.endereco import Endereco
class Pessoa:
    def __init__(self, nome: str, idade: str, generos: Generos, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.generos = generos
        self.endereco = endereco

    def __str__(self) -> str:
        return(f"\nNome: {self.nome}"
               f"\nIdade: {self.idade}"
               f"\nGênero: {self.generos}"
               f"\nDados do endereço: {self.endereco}")