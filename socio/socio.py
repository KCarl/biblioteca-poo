import uuid
from livro.livro_fisico import LivroFisico
class Socio:
    def __init__(self, nome, telefone, endereco):
        self.id = uuid.uuid1()
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.livros_emprestados = []
    def emprestarLivro(self, livro: LivroFisico):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print("Livro emprestado com sucesso!")
        else:
            print("Livro indisponível!")

    def devolverLivro(self, livro: LivroFisico):
        if livro in self.livros_emprestados and livro.devolver():
            self.livros_emprestados.remove(livro)
            print("Livro devolvido com sucesso!")
        else:
            print("Livro não consta na lista ou já está disponível!")

    def __repr__(self):
        return f"Id: {self.id} \n" \
               f"Nome: {self.nome} \n" \
               f"Telefone: {self.telefone} \n" \
               f"Endereço: {self.endereco} \n" \
               f"Livros emprestados: {self.livros_emprestados}"

if __name__ == "__main__":
    livro = LivroFisico("Harry Potter", "J K Rolling", 1997, 300)
    socio = Socio("Luiz", "85988855", "Rua J")
    socio.emprestarLivro(livro)
    print(socio)