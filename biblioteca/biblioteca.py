from livro.livro_fisico import LivroFisico
from socio.socio import Socio
class Biblioteca:
    def __init__(self):
        self.livros = []
        self.socios = []

    def adicionarLivro(self, livro: LivroFisico):
        self.livros.append(livro)
        print("Livro adicionado com sucesso!")
    def removerLivro(self, id_livro):
        for livro in self.livros:
            if livro.id == id_livro:
                self.livros.remove(livro)
                return True
        return False
    def listarLivros(self):
        for livro in self.livros:
            print(livro)

    def adicionarSocio(self, socio: Socio):
        self.socios.append(socio)
        print("Socio adicionado com sucesso!")

    def removerSocio(self, socio_id):
        for socio in self.socios:
            if socio.id == socio_id:
                self.socios.remove(socio)
                return True
        return False

    def listarSocios(self):
        for socio in self.socios:
            print(socio)

    def socioExiste(self, socio_id):
        for socio in self.socios:
            if socio.id == socio_id:
                return True
        return False

if __name__ == "__main__":
    livro = LivroFisico("HP", "J K Rolling", 1997, 300)
    socio = Socio("João", "88888", "Rua A 19")
    biblioteca = Biblioteca()
    biblioteca.adicionarLivro(livro)
    biblioteca.adicionarSocio(socio)
    biblioteca.listarLivros()
    biblioteca.listarSocios()
    biblioteca.removerSocio(socio.id)
    biblioteca.removerLivro(livro.id)